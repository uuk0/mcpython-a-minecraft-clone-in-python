from .Block import *
from entity import boxmodel
import EventHandler
import globals as G


@handler
class Snow(Block):
    def getTex(self):
        return tex_coords((12, 13), (12, 13), (12, 13))

    def getName(self):
        return "minecraft:snow_block"

    destroygroups = [destroyGroups.SHOVEL]
    drops = ["minecraft:snow"]
    dropamounts = [4]

    def getBlastResistence(self):
        return -1  # can't find it

    def getId(self):
        return 80

    def getHardness(self):
        return -1  # can't find it


@handler
class SnowLayer(Block):
    def on_creat(self):
        self.models = []
        for e in range(8):
            self.models.append(
                boxmodel.BoxModel(
                    1,
                    1,
                    0.125,
                    pyglet.image.load("./assets/textures/blocks/texture.png"),
                    64,
                    64,
                    4,
                )
            )
            self.models[-1].position = (
                self.pos[0] - 0.5,
                self.pos[1] - 0.5 + 0.125 * e - 1 / 16,
                self.pos[2] - 0.5,
            )
        self.layer = 1
        self.registert = []

    drops = ["minecraft:snow"]

    def getDropAmount(self, item):
        return self.layer

    def show(self, model, window, texture):
        self.registert.append(
            EventHandler.eventhandler.on_event("on_draw_3D", self.draw)
        )

    def hide(self, model, window):
        for e in self.registert:
            EventHandler.eventhandler.unregister_on_event(e)

    def getTex(self):
        return tex_coords((12, 13), (12, 13), (12, 13))

    def draw(self, *args):
        for e in self.models[: self.layer]:
            e.draw()
            print(e.position)

    def update(self, model, window):
        if (
            not (self.pos[0], self.pos[1] - 1, self.pos[2]) in model.world
            and self.layer != 8
        ):
            model.remove_block(self.pos)
            G.player.addToFreePlace(self.getDrop(None), self.getDropAmount(None))

    destroygroups = [destroyGroups.SHOVEL]

    def getBlastResistence(self):
        return 1

    def getId(self):
        return 78

    def getHardness(self):
        return 0.1
