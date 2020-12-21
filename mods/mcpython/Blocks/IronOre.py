from .Block import *


class IronOre(Block):
    def getTex(self):
        return tex_coords((1, 4), (1, 4), (1, 4))

    def getName(self):
        return "minecraft:iron_ore"

    destroygroups = [destroyGroups.PIKAXE]

    def getBlastResistence(self):
        return 15

    def getHardness(self):
        return 3

    def getId(self):
        return 15


handler.register(IronOre)
