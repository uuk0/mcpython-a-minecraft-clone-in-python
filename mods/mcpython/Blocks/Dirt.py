from .Block import *
from oredictnames import OreDict
from destroyGroup import *


@handler
class Dirt(Block):
    def getTex(self):
        return tex_coords((0, 1), (0, 1), (0, 1))

    def getName(self):
        return "minecraft:dirt"

    oredictnames = [OreDict.DIRT]
    destroygroups = [destroyGroups.SHOVEL]

    def getBlastResistence(self):
        return 2.5

    def getId(self):
        return 3

    def getHardness(self):
        return 0.5
