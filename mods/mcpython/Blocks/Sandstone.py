from .Block import *


@handler
class Sandstone(Block):
    def getTex(self):
        return tex_coords((2, 2), (2, 2), (2, 2))

    def getName(self):
        return "minecraft:sandstone"

    destroygroups = [destroyGroups.PIKAXE]

    def getBlastResistence(self):
        return 4

    def getId(self):
        return 24

    def getHardness(self):
        return 0.8
