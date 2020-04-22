from .Block import *
import random
import globals as G


class DiamondOre(Block):
    def getTex(self):
        return tex_coords((2, 4), (2, 4), (2, 4))

    def getName(self):
        return "minecraft:diamond_ore"

    def getDrop(self, item):
        return "minecraft:diamond"

    def getDropAmount(self, item):
        return 1

    def on_destroy(self):
        G.player.xp += random.randint(3, 7)

    def isBreakAbleWithItem(self, item):
        if item and (item.getName() == "minecraft:iron_pick_axe" or item.getName() == "minecraft:diamond_pick_axe"):
            return True
        if G.player.gamemode == 1:
            return True
        return False

    destroygroups = [destroyGroups.PIKAXE]

    def getBlastResistence(self):
        return 15

    def getHardness(self):
        return 3

    def getId(self):
        return 56

handler.register(DiamondOre)
