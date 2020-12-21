from .Block import *
from oredictnames import OreDict
from destroyGroup import *


@handler
class Grass(Block):
    def getTex(self):
        return tex_coords((1, 0), (0, 1), (0, 0))

    def getName(self):
        return "minecraft:grass"

    drops = ["minecraft:dirt"]
    oredictnames = [OreDict.DIRT, OreDict.GRASS]
    destroygroups = [destroyGroups.SHOVEL]

    def getBlastResistence(self):
        return 3

    def getHardness(self):
        return 0.6
