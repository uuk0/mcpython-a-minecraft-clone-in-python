from .Block import *
import Item


class Lava(Block):
    def getTex(self):
        return tex_coords((12, 14), (12, 14), (12, 14))

    def getName(self):
        return "minecraft:lava"

    def hasHitbox(self, item):  # basic holdable liquid system
        if not self.getName() in Item.liquidhandler.liquids:
            return False  # have we buckets that can carry me?
        if item and self.getName() in item.getHoldAbleLiquids():
            return True
        return False

    drops = []

    def getBlastResistence(self):
        return -1

    def getHardness(self):
        return -1

    def getId(self):
        return 11


handler.register(Lava)
