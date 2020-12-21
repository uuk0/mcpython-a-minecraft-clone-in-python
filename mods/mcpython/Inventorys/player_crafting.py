from .Inventory import *
from oredictnames import *


class crafting(Inventory):
    def getSlots(self):
        y = 27
        return [
            Slot(406, 312),
            Slot(448, 312),
            Slot(406, 270),
            Slot(448, 270),
            Slot(531, 287, mode="o"),
        ]

    def getImage(self):
        return None

    def getDepedens(self):
        return [2]

    def getId(self):
        return 2


handler.register(crafting)
