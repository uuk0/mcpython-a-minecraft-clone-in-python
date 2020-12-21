from .Block import *


class StoneBrick(Block):
    def getTex(self):
        return tex_coords((0, 3), (0, 3), (0, 3))

    def getName(self):
        return "minecraft:stone_brick"

    destroygroups = [destroyGroups.PIKAXE]

    def getBlastResistence(self):
        return 30

    def getHardness(self):
        return 1.5

    def getId(self):
        return 98


handler.register(StoneBrick)
