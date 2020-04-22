from .Inventory import *

class rows(Inventory):
    def getSlots(self):
        rows = []
        y = 27
        rows +=  [Slot(197, y), Slot(239, y), Slot(281, y), Slot(323, y), Slot(365, y),
                      Slot(407, y), Slot(449, y), Slot(491, y), Slot(533, y)]

        y = 120
        rows += [Slot(197, y), Slot(239, y), Slot(281, y), Slot(323, y), Slot(365, y),
                      Slot(407, y), Slot(449, y), Slot(491, y), Slot(533, y)]

        y = 164
        rows += [Slot(197, y), Slot(239, y), Slot(281, y), Slot(323, y), Slot(365, y),
                      Slot(407, y), Slot(449, y), Slot(491, y), Slot(533, y)]
        return rows

    def getImage(self):
        return './assets/textures/gui/inventory_clear.png'

    def getDepedens(self):
        return [0]

    def getImagePos(self):
        return (180, 10)

    def drawAfter(self):
        return [0]

    def drawWithoutImage(self):
        return [0]

    def getId(self):
        return 0

handler.register(rows)