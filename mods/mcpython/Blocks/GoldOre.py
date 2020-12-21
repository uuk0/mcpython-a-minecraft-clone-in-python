from .Block import *


class GoldOre(Block):
    def getTex(self):
        return tex_coords((3, 4), (3, 4), (3, 4))

    def getName(self):
        return "minecraft:gold_ore"

    destroygroups = [destroyGroups.PIKAXE]

    def getBlastResistence(self):
        return 15

    def getHardness(self):
        return 3

    def getId(self):
        return 14


handler.register(GoldOre)
