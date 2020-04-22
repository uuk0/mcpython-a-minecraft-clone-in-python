from .Block import *


class Brick(Block):
    def getTex(self):
        return tex_coords((2, 0), (2, 0), (2, 0))

    def getName(self):
        return "minecraft:brick"

    destroygroups = [destroyGroups.PIKAXE]

    def getBlastResistence(self):
        return 30

    def getHardness(self):
        return 2

    def getId(self):
        return 45

handler.register(Brick)
