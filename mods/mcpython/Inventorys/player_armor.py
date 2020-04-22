from .Inventory import *
from oredictnames import *


class armor(Inventory):
    def getId(self):
        return 3

    def getSlots(self):
        y = 27
        return [Slot(197, 210, oredictallow=OreDict.ARMOR_FOOT),
                      Slot(197, 250, oredictallow=OreDict.ARMOR_LEG),
                      Slot(197, 291, oredictallow=OreDict.ARMOR_BODY),
                      Slot(197, 333, oredictallow=OreDict.ARMOR_HEAD),
                Slot(354, 210)]

    def getImage(self):
        return None

    def getDepedens(self):
        return [2]


handler.register(armor)