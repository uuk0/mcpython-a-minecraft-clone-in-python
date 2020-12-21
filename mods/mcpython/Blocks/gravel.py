from .Block import *
from TickHandler import handler as tickhandler
from .fallingblock import *


@handler
class Gravel(FallingBlock):
    def getTex(self):
        return tex_coords((1, 5), (1, 5), (1, 5))

    def getName(self):
        return "minecraft:gravel"

    destroygroups = [destroyGroups.SHOVEL]

    def getBlastResistence(self):
        return 3

    def getDrop(self, item):
        return (
            self.getItemName()
        )  # TODO: add gravel 90% and flint 10%, fortune 1: 14%, 2: 25%, 3: 100%

    def getId(self):
        return 13

    def getDropBlock(self):
        return self.getName()

    def getHardness(self):
        return 0.6
