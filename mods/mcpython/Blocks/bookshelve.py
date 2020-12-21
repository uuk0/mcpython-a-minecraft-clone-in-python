from .Block import *
import random


class Bookshelve(Block):
    def getTex(self):
        return tex_coords((1, 7), (1, 7), (4, 7))

    def getName(self):
        return "minecraft:bookshelve"

    drops = ["minecraft:book"]

    def getDropAmount(self, item):
        return [3]

    destroygroups = [destroyGroups.AXE]

    def getBlastResistence(self):
        return 7.5

    def getHardness(self):
        return 1.5

    def getId(self):
        return 47


handler.register(Bookshelve)
