from .Block import *
from destroyGroup import destroyGroups

@handler
class BlueIce(Block):
    def getTex(self):
        return tex_coords((13, 13), (13, 13), (13, 13))

    def getName(self):
        return "minecraft:blue_ice"

    def getDrop(self, item):
        return []

    def getBlastResistence(self):
        return 14

    def getId(self):
        return -1 #Can't find an ID

    def getHardness(self):
        return 2.8

    destroygroups = [destroyGroups.PIKAXE]

@handler
class Ice(Block):
    def getTex(self):
        return tex_coords((11, 13), (11, 13), (11, 13))

    def getName(self):
        return "minecraft:ice"

    def getDrop(self, item):
        return []

    def getBlastResistence(self):
        return 2.5

    def getId(self):
        return 79

    def getHardness(self):
        return 0.5

    destroygroups = [destroyGroups.PIKAXE]

@handler
class PackedIce(Block):
    def getTex(self):
        return tex_coords((11, 12), (11, 12), (11, 12))

    def getName(self):
        return "minecraft:packed_ice"

    def getDrop(self, item):
        return []

    def getBlastResistence(self):
        return 2.5

    def getId(self):
        return 174

    def getHardness(self):
        return 0.5

    destroygroups = [destroyGroups.PIKAXE]