from .Block import *
import player
import EventHandler
import texturGroups
import pyglet
import entity.boxmodel as boxmodel
import globals as G


class Slab(Block):
    def on_creat(self):
        self.modelsys = []
        self.models = []
        self.side = "D"
        self.boxmodelA = boxmodel.BoxModel(
            1,
            1,
            0.5,
            pyglet.image.load("./assets/textures/blocks/texture.png"),
            64,
            64,
            32,
        )
        self.boxmodelA.position = (
            self.pos[0] - 0.5,
            self.pos[1] - 0.5,
            self.pos[2] - 0.5,
        )
        self.boxmodelA.update_texture_data([self.getTexPos()] * 6)
        self.boxmodelB = boxmodel.BoxModel(
            1,
            1,
            0.5,
            pyglet.image.load("./assets/textures/blocks/texture.png"),
            64,
            64,
            32,
        )
        self.boxmodelB.position = (self.pos[0] - 0.5, self.pos[1], self.pos[2] - 0.5)
        self.boxmodelB.update_texture_data(
            [(self.getTexPos()[0], self.getTexPos()[1] + 32)] * 6
        )

    def getTexPos(self):
        return (0, 0)

    def show(self, model, window, texture):
        if self.side == "A":
            Block.show(self, model, window, texture)
            return
        self.modelsys.append(
            EventHandler.eventhandler.on_event("on_draw_3D", self.draw)
        )
        self.models = []
        if self.side == "D":
            self.models.append(self.boxmodelA)
        if self.side == "U":
            self.models.append(self.boxmodelB)

    def hide(self, model, window):
        if self.side == "A":
            Block.hide(self, model, window)
            return
        for e in self.modelsys:
            EventHandler.eventhandler.unregister_on_event(e)

    def draw(self, *args):
        for e in self.models:
            e.draw()

    def getTex(self):
        return tex_coords(
            *[(int(self.getTexPos()[0] / 64), int(self.getTexPos()[1] / 64))] * 3
        )

    def getNBTNames(self):
        return ["side"]

    def setNBT(self, name, value):
        if name == "side":
            if self.side != value:
                self.hide(G.window.model, G.window)
                self.side = value
                self.show(G.window.model, G.window, self.getTex())

    def getDropAmount(self, item):
        return 2 if self.side == "A" else 1


class Wood_0_Slab(Slab):
    def getTexPos(self):
        return (64, 448)

    def getName(self):
        return "minecraft:wood_slab_0"


handler.register(Wood_0_Slab)
