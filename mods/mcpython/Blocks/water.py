from .Block import *
import Item

class Water(Block):
    def getTex(self):
        return tex_coords((0, 2), (0, 2), (0, 2))

    def getName(self):
        return "minecraft:water"

    def hasHitbox(self, item): #basic holdable liquid system
        if not self.getName() in Item.liquidhandler.liquids:
            return False #have we buckets that can carry me?
        if item and self.getName() in item.getHoldAbleLiquids():
            return True
        return False

    drops = []

    def getBlastResistence(self):
        return -1

    def getHardness(self):
        return -1

    def getId(self):
        return 8

handler.register(Water)
