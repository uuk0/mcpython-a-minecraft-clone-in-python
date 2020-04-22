from .Block import *
from TickHandler import handler as tickhandler
from .fallingblock import *

@handler
class Sand(FallingBlock):
    def getTex(self):
        return tex_coords((1, 1), (1, 1), (1, 1))

    def getName(self):
        return "minecraft:sand"

    destroygroups = [destroyGroups.SHOVEL]

    def getBlastResistence(self):
        return 2.5

    def getId(self):
        return 12

    def getHardness(self):
        return 0.5
