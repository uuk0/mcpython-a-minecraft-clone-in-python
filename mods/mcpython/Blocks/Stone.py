from .Block import *


@handler
class Stone(Block):
    def getTex(self):
        return tex_coords((2, 1), (2, 1), (2, 1))

    def getName(self):
        return "minecraft:stone"

    drops = ["minecraft:cobblestone"]
    destroygroups = [destroyGroups.PIKAXE]

    def getBlastResistence(self):
        return 30

    def getId(self):
        return 1

    def getHardness(self):
        return 1.5


@handler
class Diorit(Block):
    def getTex(self):
        return tex_coords((11, 15), (11, 15), (11, 15))

    def getName(self):
        return "minecraft:diorite"

    destroygroups = [destroyGroups.PIKAXE]

    def getBlastResistence(self):
        return 30

    def getId(self):
        return "1:3"

    def getHardness(self):
        return 1.5


@handler
class PolishedDiorit(Diorit):
    def getTex(self):
        return tex_coords((11, 14), (11, 14), (11, 14))

    def getName(self):
        return "minecraft:polished_diorite"
