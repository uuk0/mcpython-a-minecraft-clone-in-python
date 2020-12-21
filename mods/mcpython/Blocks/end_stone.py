from .Block import *
from oredictnames import OreDict
from destroyGroup import *


class Endstone(Block):
    def getTex(self):
        return tex_coords((12, 12), (12, 12), (12, 12))

    def getName(self):
        return "minecraft:endstone"

    destroygroups = [destroyGroups.PIKAXE]

    def getBlastResistence(self):
        return 45

    def getHardness(self):
        return 3

    def getId(self):
        return 121


handler.register(Endstone)


class Endbrick(Block):
    def getTex(self):
        return tex_coords((12, 11), (12, 11), (12, 11))

    def getName(self):
        return "minecraft:endbrick"

    destroygroups = [destroyGroups.PIKAXE]

    def getBlastResistence(self):
        return 4

    def getHardness(self):
        return 0.8

    def getId(self):
        return 206


handler.register(Endbrick)
