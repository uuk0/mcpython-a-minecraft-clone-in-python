from .Block import *
from oredictnames import *

@handler
class Obsidian(Block):
    def getTex(self):
        return tex_coords((3, 0), (3, 0), (3, 0))

    def getName(self):
        return "minecraft:obsidian"

    destroygroups = [destroyGroups.PIKAXE]

    def getDrop(self, item):
        return self.getName() if item.getDestroyGroup() == destroyGroups.PIKAXE and item.getToolMaterial() == "minecraft:diamond" else []

    def getBlastResistence(self):
        return 6000

    def getId(self):
        return 49

    def getHardness(self):
        return 50

