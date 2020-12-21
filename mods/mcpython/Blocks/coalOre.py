from .Block import *
import random
import globals as G


@handler
class CoalOre(Block):
    def getTex(self):
        return tex_coords((0, 4), (0, 4), (0, 4))

    def getName(self):
        return "minecraft:coal_ore"

    drops = ["minecraft:coal"]

    destroygroups = [destroyGroups.PIKAXE]

    def on_destroy(self):
        G.player.xp += random.randint(0, 2)

    def getBlastResistence(self):
        return 15

    def getId(self):
        return 16

    def getHardness(self):
        return 3
