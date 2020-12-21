print("[INFO] definiting Model-class")

from moduls import *

from mathhelper import *

from chat import chat

from Blocks import *
import Blocks

import texturGroups

import WorldHandler
import WorldSaver

import traceback
import entity

if sys.version_info[0] >= 3:
    xrange = range


class Model(object):
    def __init__(self, window):
        self.window = window

        # A Batch is a collection of vertex lists for batched rendering.
        self.batch = pyglet.graphics.Batch()

        # A TextureGroup manages an OpenGL texture.
        # self.group = TextureGroup(image.load(TEXTURE_PATH).get_texture())

        # A mapping from position to the texture of the block at that position.
        # This defines all the blocks that are currently in the world.
        self.world = {}

        self.entitys = {}

        # Same mapping as `world` but only contains blocks that are shown.
        self.shown = {}

        # Mapping from position to a pyglet `VertextList` for all shown blocks.
        self._shown = {}

        # Mapping from sector to a list of positions inside that sector.
        self.sectors = {}

        self.shown_sectors = []

        # Simple function queue implementation. The queue is populated with
        # _show_block() and _hide_block() calls
        self.queue = deque()
        self.generated = [(0, 0, 0)]
        self.togenerate = []
        self.high_data = {}

        self._initialize()

    def _initialize(self):
        """Initialize the world by placing all the blocks."""
        # changed to worldhandler

    def hit_test(self, position, vector, max_distance=8):
        """Line of sight search from current position. If a block is
        intersected it is returned, along with the block previously in the line
        of sight. If no block is found, return None, None.

        Parameters
        ----------
        position : tuple of len 3
            The (x, y, z) position to check visibility from.
        vector : tuple of len 3
            The line of sight vector.
        max_distance : int
            How many blocks away to search for a hit.

        """
        m = 8
        x, y, z = position
        dx, dy, dz = vector
        previous = None
        for _ in xrange(max_distance * m):
            key = normalize((x, y, z))
            if (
                key != previous
                and key in self.world
                and self.world[key].hasHitbox(
                    self.window.player.inventory.hotbar.slots[
                        self.window.hotbarelement
                    ].item
                )
            ):
                return key, previous
            previous = key
            x, y, z = x + dx / m, y + dy / m, z + dz / m
        return None, None

    def exposed(self, position):
        """Returns False is given `position` is surrounded on all 6 sides by
        blocks, True otherwise.

        """
        x, y, z = position
        for dx, dy, dz in FACES:
            if (x + dx, y + dy, z + dz) not in self.world:
                return True
        return False

    def add_block(
        self,
        position,
        block,
        immediate=True,
        inst=False,
        creat=False,
        hitblock=None,
        save=True,
    ):
        """Add a block with the given `texture` and `position` to the world.

        Parameters
        ----------
        position : tuple of len 3
            The (x, y, z) position of the block to add.
        texture : list of len 3
            The coordinates of the texture squares. Use `tex_coords()` to
            generate.
        immediate : bool
            Whether or not to draw the block immediately.

        """
        if block == None:
            self.remove_block(position)
            return
        if not position:
            return
        if position[1] > 256 or position[1] < 0:
            return False
        if not inst:
            oblock = block
            import Blocks.Block as Block

            block = Block.handler.getByName(block)
            if not block:
                print("[ERROR] block not found", oblock)
                return
            block = block(position, hitblock=hitblock)
        block.pos = position
        if not creat:
            block.update(self, self.window)
        if not creat:
            self.updateNexts(position)
        if position in self.world:
            self.remove_block(position, immediate, save=save)
        self.world[position] = block
        self.sectors.setdefault(sectorize(position), []).append(position)
        if immediate:
            if self.exposed(position):
                self.show_block(position)
            self.check_neighbors(position)
        if self.window.worldname and save:
            WorldSaver.saveToChunk(
                sectorize(position),
                self.window.worldname,
                [0, position, self.world[position].getName()],
            )
        return True

    def add_entity(self, name, position):
        inst = entity.entityhandler.getByName(name)(position)
        self.entitys[position] = inst

    def remove_block(self, position, immediate=True, save=True, call=True):
        """Remove the block at the given `position`.

        Parameters
        ----------
        position : tuple of len 3
            The (x, y, z) position of the block to remove.
        immediate : bool
            Whether or not to immediately remove block from canvas.

        """
        if not position in self.world:
            return
        if call:
            self.world[position].on_destroy()
        if immediate:
            if position in self.shown:
                self.hide_block(position)
        del self.world[position]
        self.sectors[sectorize(position)].remove(position)
        if immediate:
            self.check_neighbors(position)
            self.updateNexts(position)
        if self.window.worldname and save:
            WorldSaver.saveToChunk(
                sectorize(position), self.window.worldname, [2, position]
            )

    def move_block(self, startpos, endpos, immediate=True):
        if endpos[1] < -100:
            return
        if not startpos in self.world:
            return False
        block = self.world[startpos]
        if startpos in self.shown:
            self.hide_block(startpos)
        self.remove_block(startpos, immediate=False)
        self.add_block(endpos, block, immediate=False, inst=True)
        self.show_block(endpos)
        block.pos = endpos
        self.check_neighbors(startpos)
        self.check_neighbors(endpos)

    def updateTex(self, position):
        state = position in self.shown
        self.hide_block(position)
        if state:
            self.show_block(position)

    def check_neighbors(self, position):
        """Check all blocks surrounding `position` and ensure their visual
        state is current. This means hiding blocks that are not exposed and
        ensuring that all exposed blocks are shown. Usually used after a block
        is added or removed.

        """
        x, y, z = position
        for dx, dy, dz in FACES:
            key = (x + dx, y + dy, z + dz)
            if key not in self.world:
                continue
            if self.exposed(key):
                if key not in self.shown:
                    self.show_block(key)
            else:
                if key in self.shown:
                    self.hide_block(key)

    def show_block(self, position, immediate=True):
        """Show the block at the given `position`. This method assumes the
        block has already been added with add_block()

        Parameters
        ----------
        position : tuple of len 3
            The (x, y, z) position of the block to show.
        immediate : bool
            Whether or not to show the block immediately.

        """
        texture = self.world[position].getTex()
        self.shown[position] = texture
        if immediate:
            self._show_block(position, texture)
        else:
            self._enqueue(self._show_block, position, texture)

    def _show_block(self, position, texture):
        """Private implementation of the `show_block()` method.

        Parameters
        ----------
        position : tuple of len 3
            The (x, y, z) position of the block to show.
        texture : list of len 3
            The coordinates of the texture squares. Use `tex_coords()` to
            generate.

        """
        if not position in self.world:
            return
        self.world[position].show(self, self.window, texture)

    def hide_block(self, position, immediate=True):
        """Hide the block at the given `position`. Hiding does not remove the
        block from the world.

        Parameters
        ----------
        position : tuple of len 3
            The (x, y, z) position of the block to hide.
        immediate : bool
            Whether or not to immediately remove the block from the canvas.

        """
        if immediate:
            self._hide_block(position)
        else:
            self._enqueue(self._hide_block, position)

    def _hide_block(self, position):
        """Private implementation of the 'hide_block()` method."""
        if not position in self.world:
            return
        self.world[position].hide(self, self.window)
        if position in self.shown:
            self.shown.pop(position)

    def show_sector(self, sector):
        """Ensure all blocks in the given sector that should be shown are
        drawn to the canvas.

        """
        self.shown_sectors.append(sector)
        for position in self.sectors.get(sector, []):
            if position not in self.shown and self.exposed(position):
                self.show_block(position, False)

    def hide_sector(self, sector):
        """Ensure all blocks in the given sector that should be hidden are
        removed from the canvas.

        """
        for position in self.sectors.get(sector, []):
            if position in self.shown:
                self.hide_block(position, False)
        self.shown_sectors.remove(sector)

    def change_sectors(self, before, after):
        """Move from sector `before` to sector `after`. A sector is a
        contiguous x, y sub-region of world. Sectors are used to speed up
        world rendering.

        """
        before_set = set()
        after_set = set()
        pad = 4
        for dx in xrange(-pad, pad + 1):
            for dy in [0]:  # xrange(-pad, pad + 1):
                for dz in xrange(-pad, pad + 1):
                    if dx ** 2 + dy ** 2 + dz ** 2 > (pad + 1) ** 2:
                        continue
                    if before:
                        x, y, z = before
                        before_set.add((x + dx, y + dy, z + dz))
                    if after:
                        x, y, z = after
                        after_set.add((x + dx, y + dy, z + dz))
        show = after_set - before_set
        hide = before_set - after_set
        for i, sector in enumerate(show):
            self.show_sector(sector)

        for sector in hide:
            self.hide_sector(sector)

    def _enqueue(self, func, *args):
        """Add `func` to the internal queue."""
        self.queue.append((func, args))

    def _dequeue(self):
        """Pop the top function from the internal queue and call it."""
        func, args = self.queue.popleft()
        if False and func == WorldHandler._generate:
            print("[INFO] generating chunk ", args[0:1])
            for e in func(*args):
                self.add_block(*e)
        else:
            func(*args)

    def process_queue(self):
        """Process the entire queue while taking periodic breaks. This allows
        the game loop to run smoothly. The queue contains calls to
        _show_block() and _hide_block() so this method should be called if
        add_block() or remove_block() was called with immediate=False

        """
        start = time.time()
        while self.queue and time.time() - start < 1.0 / TICKS_PER_SEC:
            self._dequeue()

    def process_entire_queue(self):
        """Process the entire queue with no breaks."""
        while self.queue:
            self._dequeue()

    def updateNexts(self, position):
        if not position:
            return
        x, y, z = position
        for dx, dy, dz in FACES:
            key = (x + dx, y + dy, z + dz)
            if key not in self.world:
                continue
            self.world[key].update(self, self.window)
