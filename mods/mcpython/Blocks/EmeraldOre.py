from .Block import *
import globals as G

class EmeraldOre(Block):
    def getTex(self):
        return tex_coords((8, 5), (8, 5), (8, 5))

    def getName(self):
        return "minecraft:emerald_ore"

    drops = ["minecraft:emerald_ore"]
    dropamounts = [1]

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
        return 129

handler.register(EmeraldOre)
