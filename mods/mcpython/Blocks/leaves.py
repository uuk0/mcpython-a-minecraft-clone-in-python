from .Block import *
import random

class leave_0(Block):
    def getTex(self):
        return tex_coords((5, 2), (5, 2), (5, 2))

    def getName(self):
        return "minecraft:leave_0"

    drops = ["minecraft:sapling"]

    def getDropAmount(self, item):
        return 0 if random.randint(1, 7) < 6 else 1

    destroygroups = [destroyGroups.SHEER]

    def getBlastResistence(self):
        return 1

    def getHardness(self):
        return 0.2

    def getId(self):
        return 18

handler.register(leave_0)