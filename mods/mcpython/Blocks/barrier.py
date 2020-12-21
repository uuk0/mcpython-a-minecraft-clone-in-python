from .Block import *
import globals as G


class Barrier(Block):
    def getTex(self):
        return None

    def getName(self):
        return "minecraft:barrier"

    def isBreakAble(self):
        return G.player.gamemode == 1

    def show(self, model, window, texture):
        pass

    def hide(self, model, window):
        pass


handler.register(Barrier)
