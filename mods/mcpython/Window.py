print("[INFO] definiting Window-class")

from Model import *

from pyglet.window import key

# import Block

import Blocks

from chat import *

from TickHandler import handler as tickhandler

from player import *

import Item

import config

import EventHandler
import lootchest
import WorldHandler

import globals as G

import states

from constans import FACES


class Window(pyglet.window.Window):

    def __init__(self, *args, **kwargs):
        self.WorldName = ""
        super(Window, self).__init__(*args, **kwargs)
        self.state = ""

        # Whether or not the window exclusively captures the mouse.
        self.exclusive = False

        # When flying gravity has no effect and speed is increased.
        self.flying = False

        # Strafing is moving lateral to the direction you are facing,
        # e.g. moving to the left or right while continuing to face forward.
        #
        # First element is -1 when moving forward, 1 when moving back, and 0
        # otherwise. The second element is -1 when moving left, 1 when moving
        # right, and 0 otherwise.
        self.strafe = [0, 0]

        # Current (x, y, z) position in the world, specified with floats. Note
        # that, perhaps unlike in math class, the y-axis is the vertical axis.
        self.position = self.startpos = (0, 0, 0)

        # First element is rotation of the player in the x-z plane (ground
        # plane) measured from the z-axis down. The second is the rotation
        # angle from the ground plane up. Rotation is in degrees.
        #
        # The vertical plane rotation ranges from -90 (looking straight down) to
        # 90 (looking straight up). The horizontal rotation range is unbounded.
        self.rotation = (0, 0)

        # Which sector the player is currently in.
        self.sector = None

        # Velocity in the y (upward) direction.
        self.dy = 0

        # A list of blocks the player can place. Hit num keys to cycle.
        # self.inventory = [Blocks.Grass, Blocks.Sand, Blocks.Brick, Blocks.Stone, Blocks.Dirt, Blocks.CobbelStone]
        self.hotbarelement = 0

        # The current block the user can place. Hit num keys to cycle.
        # self.block = self.inventory[0]

        # Convenience list of num keys.
        self.num_keys = config.CONFIGS["init"]["KEYBINDS"]['inventoryslots:keys']
        self.num_keys = config.CONFIGS["init"]["KEYBINDS"]['inventoryslots:keys']

        # Instance of the model that handles the world.
        self.model = Model(self)

        self.chatlabel = pyglet.text.Label('', font_name='Arial', font_size=18,
                                           x=30, y=50, anchor_x='left', anchor_y='top',
                                           color=(0, 0, 0, 255))

        self.player = player(self)
        player.playerinst = self.player

        self.world = None

        # time to manage destroy-system
        self.mouseclicktime = 0
        self.isclicked = False
        self.clickingblock = None
        self.clickstarttime = 0

        # mousepos for playerinventory
        self.mousepos = (0, 0)

        # helper vars for braking system
        self.braking_start = None

        self.turning_strafe = [0, 0]

        # This call schedules the `update()` method to be called
        # TICKS_PER_SEC. This is the main game event loop.
        pyglet.clock.schedule_interval(self.update, 1.0 / TICKS_PER_SEC)
        pyglet.clock.schedule_interval(tickhandler._run, 0.5)
        pyglet.clock.schedule_interval(EventHandler.eventhandler.update, 1.0 / TICKS_PER_SEC)

        self.keyEvent = None
        self.last_generate = 1000

        self.menü = None
        self.menünames = config.CONFIGS["init"]["GAME_STATES"]
        self.menüeventbinds = []
        self.camerastate = 0  # 0: normal, 1: viewing player from out

        if config.CONFIGS["init"]["GAMETYPE"] != "FULL":
            eventhandler.on_event("on_draw_2D", self.on_draw_2d_demo_label)
            print("demo mode")

        self.worldname = None
        self.seed = 0

        self.gametime = 0  # a value between 0 and 2000 (0=2000)

        self.lastsize = (800, 600)

        self.demostarttime = time.time()

    def set_menu(self, name):
        self.keyEvent = name
        states.handler.activate(name)
        return

    def set_exclusive_mouse(self, exclusive):
        """ If `exclusive` is True, the game will capture the mouse, if False
        the game will ignore the mouse.

        """
        super(Window, self).set_exclusive_mouse(exclusive)
        self.exclusive = exclusive

    def get_sight_vector(self):
        """ Returns the current line of sight vector indicating the direction
        the player is looking.

        """
        x, y = self.rotation
        # y ranges from -90 to 90, or -pi/2 to pi/2, so m ranges from 0 to 1 and
        # is 1 when looking ahead parallel to the ground and 0 when looking
        # straight up or down.
        m = math.cos(math.radians(y))
        # dy ranges from -1 to 1 and is -1 when looking straight down and 1 when
        # looking straight up.
        dy = math.sin(math.radians(y))
        dx = math.cos(math.radians(x - 90)) * m
        dz = math.sin(math.radians(x - 90)) * m
        return (dx, dy, dz)

    def get_motion_vector(self):
        """ Returns the current motion vector indicating the velocity of the
        player.

        Returns
        -------
        vector : tuple of len 3
            Tuple containing the velocity in x, y, and z respectively.

        """
        if any(self.strafe):
            x, y = self.rotation
            strafe = math.degrees(math.atan2(*self.strafe))
            y_angle = math.radians(y)
            x_angle = math.radians(x + strafe)
            if self.flying:
                m = math.cos(y_angle)
                dy = math.sin(y_angle)
                if self.strafe[1]:
                    # Moving left or right.
                    dy = 0.0
                    m = 1
                if self.strafe[0] > 0:
                    # Moving backwards.
                    dy *= -1
                # When you are flying up or down, you have less left and right
                # motion.
                dx = math.cos(x_angle) * m
                dz = math.sin(x_angle) * m
            else:
                dy = 0.0
                dx = math.cos(x_angle)
                dz = math.sin(x_angle)
        else:
            dy = 0.0
            dx = 0.0
            dz = 0.0
        return (dx, dy, dz)

    def update(self, dt):
        """ This method is scheduled to be called repeatedly by the pyglet
        clock.

        Parameters
        ----------
        dt : float
            The change in time since the last call.

        """
        if config.CONFIGS["DoDayNightCyclus"]:
            self.gametime += int(dt / 10)
            if self.gametime > 2000:
                self.gametime -= 2000
            if self.gametime <= 1000:
                glClearColor((2000 - self.gametime) / 2000 * 0.5, (2000 - self.gametime) / 2000 * 0.69,
                             (2000 - self.gametime) / 2000, (2000 - self.gametime) / 2000)
            else:
                glClearColor(self.gametime / 2000 * 0.5, self.gametime / 2000 * 0.69, self.gametime / 2000,
                             self.gametime / 2000)
        if dt > 10:
            print("[ERROR] update-zyklus do need more time then normal (" + str(dt) + " secounds)")
        self.model.process_queue()
        sector = sectorize(self.position)
        if sector != self.sector:
            self.model.change_sectors(self.sector, sector)
            if self.sector is None:
                self.model.process_entire_queue()
            self.sector = sector
        m = 8
        dt = min(dt, 0.2)
        for _ in xrange(m):
            self._update(dt / m)

        """
        if self.position[1] < -150:
            self.position = (self.position[0], 300, self.position[2])
        if self.position[1] > 310:
            self.position = (self.position[0], -140, self.position[2])
        """
        if self.position[1] < -150:
            self.player.harts -= 1
        if normalize(self.position) in self.model.world:
            self.player.harts -= 0.5
        if self.player.harts < 0:
            self.kill("killed")
        WorldSaver.savePlayerData(self.worldname, self)

        op = self.position;
        ora = self.rotation
        self.player.update()
        eventhandler.call("on_player_move", self.position, self.rotation, instant=True)

        now = time.time()
        d = now - self.demostarttime
        if d >= 100 * 60:
            print("[INFO] demo time over")
            WorldSaver.saveWorld(self.model, self.worldname)
            WorldSaver.cleanUpModel(self.model)
            self.set_menu("start_menü")

        if self.keyEvent != "game":
            self.demostarttime += dt

        if self.braking_start != None:
            if self.player.gamemode == 1 and time.time() - self.braking_start > 0.2:
                vector = self.get_sight_vector()
                block, previous = self.model.hit_test(self.position, vector)
                if block:
                    b = self.model.world[block]
                    self.model.remove_block(b.pos)
                    if self.player.inventory.hotbar.slots[self.hotbarelement].item: self.player.inventory.hotbar.slots[
                        self.hotbarelement].item.on_destroy_with(b)
                self.braking_start = time.time()
                return
            d = time.time() - self.braking_start
            vector = self.get_sight_vector()
            block, previous = self.model.hit_test(self.position, vector)
            i = self.player.inventory.hotbar.slots[self.hotbarelement].item
            if not block: return
            b = self.model.world[block]
            id = i.getDestroyMultiplierWithTool(b) if i else 1
            if d / id > b.getHardness() / 5 and b.isBreakAbleWithItem(i) and b.isBreakAble():
                if b.getDrop(i) != None:
                    self.player.addToFreePlace(b.getDrop(i), b.getDropAmount(i))
                self.model.remove_block(b.pos)
                self.braking_start = time.time()
                if self.player.inventory.hotbar.slots[self.hotbarelement].item: self.player.inventory.hotbar.slots[
                    self.hotbarelement].item.on_destroy_with(b)
            elif not b.isBreakAbleWithItem(i) or not b.isBreakAble():
                self.braking_start = time.time()

    def _update(self, dt):
        """ Private implementation of the `update()` method. This is where most
        of the motion logic lives, along with gravity and collision detection.

        Parameters
        ----------
        dt : float
            The change in time since the last call.

        """
        if self.turning_strafe[0] and config.CONFIGS["ALLOW_CAMERA_MOVING_WITH_ARROWS"]:
            self.rotation = (self.rotation[0] + self.turning_strafe[0] / 4, self.rotation[1])
        if self.turning_strafe[1] and config.CONFIGS["ALLOW_CAMERA_MOVING_WITH_ARROWS"]:
            if (-90 < self.rotation[1] and self.turning_strafe[1] == -1) or (
                    90 > self.rotation[1] and self.turning_strafe[1] == 1):
                self.rotation = (self.rotation[0], self.rotation[1] + self.turning_strafe[1] / 4)
            else:
                self.turning_strafe[1] = None
        # walking
        speed = FLYING_SPEED if self.flying else WALKING_SPEED
        d = dt * speed  # distance covered this tick.
        dx, dy, dz = self.get_motion_vector()
        # New position in space, before accounting for gravity.
        dx, dy, dz = dx * d, dy * d, dz * d
        # gravity
        if not self.flying:
            # Update your vertical speed: if you are falling, speed up until you
            # hit terminal velocity; if you are jumping, slow down until you
            # start falling.
            self.dy -= dt * GRAVITY
            self.dy = max(self.dy, -TERMINAL_VELOCITY)
            ldy = dy
            dy += self.dy * dt
            if ldy < dy:
                self.player.falling = True
                self.player.fallhigh += ldy - dy
        # collisions
        x, y, z = self.position
        if self.player.gamemode != 3:
            x, y, z = self.collide((x + dx, y + dy, z + dz), PLAYER_HEIGHT)
        else:
            x, y, z = x + dx, y + dy, z + dz
        self.position = (x, y, z)

    def collide(self, position, height):
        """ Checks to see if the player at the given `position` and `height`
        is colliding with any blocks in the world.

        Parameters
        ----------
        position : tuple of len 3
            The (x, y, z) position to check for collisions at.
        height : int or float
            The height of the player.

        Returns
        -------
        position : tuple of len 3
            The new position of the player taking into account collisions.

        """
        # How much overlap with a dimension of a surrounding block you need to
        # have to count as a collision. If 0, touching terrain at all counts as
        # a collision. If .49, you sink into the ground, as if walking through
        # tall grass. If >= .5, you'll fall through the ground.
        pad = 0.1
        # pad = 0
        p = list(position)
        np = normalize(position)
        for face in FACES:  # check all surrounding blocks
            for i in xrange(3):  # check each dimension independently
                if not face[i]:
                    continue
                # How much overlap you have with this dimension.
                d = (p[i] - np[i]) * face[i]
                if d < pad:
                    (x, y, z) = self.position
                    (dx, dy, dz) = face
                    if (x + dx, y + dy, z + dz) in self.model.world: self.player.harts -= self.model.world[
                        (x + dx, y + dy, z + dz)].getPlayerDamage()
                    continue
                for dy in xrange(height):  # check each height
                    op = list(np)
                    op[1] -= dy
                    op[i] += face[i]
                    if tuple(op) not in self.model.world or not self.model.world[tuple(op)].hasHitbox(None):
                        continue
                    p[i] -= (d - pad) * face[i]
                    if face == (0, -1, 0) or face == (0, 1, 0):
                        # You are colliding with the ground or ceiling, so stop
                        # falling / rising.
                        self.dy = 0
                        if self.player.gamemode != 1 and self.player.falling and self.player.fallhigh > 1.8:
                            self.player.harts -= round((self.player.fallhigh - 2) / 3)
                    break
        return tuple(p)

    def on_mouse_press(self, x, y, button, modifiers):
        """ Called when a mouse button is pressed. See pyglet docs for button
        amd modifier mappings.

        Parameters
        ----------
        x, y : int
            The coordinates of the mouse click. Always center of the screen if
            the mouse is captured.
        button : int
            Number representing mouse button that was clicked. 1 = left button,
            4 = right button.
        modifiers : int
            Number representing any modifying keys that were
            pressed when the
            mouse button was clicked.

        """
        EventHandler.eventhandler.call("on_mouse_press", x, y, button, modifiers, instant=True)

    def on_mouse_release(self, x, y, button, modifiers):
        self.braking_start = None

    def on_mouse_motion(self, x, y, dx, dy):
        """ Called when the player moves the mouse.

        Parameters
        ----------
        x, y : int
            The coordinates of the mouse click. Always center of the screen if
            the mouse is captured.
        dx, dy : float
            The movement of the mouse.

        """
        EventHandler.eventhandler.call("on_mouse_motion", x, y, dx, dy, instant=True)

    def on_key_press(self, symbol, modifiers):
        """ Called when the player presses a key. See pyglet docs for key
        mappings.

        Parameters
        ----------
        symbol : int
            Number representing the key that was pressed.
        modifiers : int
            Number representing any modifying keys that were pressed.

        """
        EventHandler.eventhandler.call("on_key_press", symbol, modifiers, instant=True)

    def on_key_release(self, symbol, modifiers):
        """ Called when the player releases a key. See pyglet docs for key
        mappings.

        Parameters
        ----------
        symbol : int
            Number representing the key that was pressed.
        modifiers : int
            Number representing any modifying keys that were pressed.

        """
        EventHandler.eventhandler.call("on_key_release", symbol, modifiers, instant=True)

    def on_resize(self, width, height):
        """ Called when the window is resized to a new `width` and `height`.

        """
        ls = self.lastsize
        dx = ls[0] - width
        dy = ls[1] - height
        self.lastsize = (width, height)
        EventHandler.eventhandler.call("on_resize", dx, dy, width, height)

    def set_2d(self):
        """ Configure OpenGL to draw in 2d.

        """
        width, height = self.get_size()
        glDisable(GL_DEPTH_TEST)
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0, width, 0, height, -1, 1)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def set_3d(self):
        """ Configure OpenGL to draw in 3d.

        """
        width, height = self.get_size()
        glEnable(GL_DEPTH_TEST)
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(65.0, width / float(height), 0.1, 60.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        x, y = self.rotation
        glRotatef(x, 0, 1, 0)
        glRotatef(-y, math.cos(math.radians(x)), 0, math.sin(math.radians(x)))
        x, y, z = self.position
        glTranslatef(-x, -y, -z)

    def on_draw_2d_demo_label(self, eventname, obj):
        """if config.CONFIGS["init"]["GAMETYPE"] != "FULL":
            now = time.time()
            d = now - self.demostarttime
            u = 100 * 60 - d
            self.demolabel.text = str(round_down(u/60)) + " min "
            self.demolabel.text += str(round_down(u-round_down(u/60)*60))
            self.demolabel.text += " sec"
        self.demolabel.draw()"""
        if (100 * 60 - time.time() - self.demostarttime) / 60 > 100:
            print("demo time over!!!")
            self.close()

    def on_draw(self):
        """ Called by pyglet to draw the canvas.

        """
        self.clear()
        self.set_3d()
        glColor3d(1, 1, 1)
        EventHandler.eventhandler.call("on_draw_3D", self, instant=True)
        self.set_2d()
        EventHandler.eventhandler.call("on_draw_2D", self, instant=True)

    def draw_reticle(self):
        """ Draw the crosshairs in the center of the screen.

        """

    def kill(self, msg):
        y = 4
        while (0, y, 0) in self.model.world:
            y += 1
        self.position = self.startpos
        chat.println(msg)
        self.player.harts = 20

    def openInventory(self, id):
        invhandler.show(id)

    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        if 2 not in invhandler.shown:
            if self.hotbarelement + scroll_x > 8:
                if self.hotbarelement + 1 > 1:
                    scroll_x -= 1
                    self.hotbarelement = 0
                while self.hotbarelement + scroll_x > 8:
                    scroll_x -= 9
            self.hotbarelement += scroll_x
        if self.braking_start: self.braking_start = time.time()
