from .Block import *
import random


class Melon(Block):
    def getTex(self):
        return tex_coords((4, 3), (4, 3), (4, 2))

    def getName(self):
        return "minecraft:melon_block"

    def getDropAmount(self, item):
        return random.randint(1, 3)

    drops = ["minecraft:melon"]
    destroygroups = [destroyGroups.AXE]


handler.register(Melon)
