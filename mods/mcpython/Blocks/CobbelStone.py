from .Block import *


class CobbelStone(Block):
    def getTex(self):
        return tex_coords((6, 3), (6, 3), (6, 3))

    def getName(self):
        return "minecraft:cobblestone"

    destroygroups = [destroyGroups.PIKAXE]

    def getBlastResistence(self):
        return 30

    def getHardness(self):
        return 2

    def getId(self):
        return 4

handler.register(CobbelStone)
