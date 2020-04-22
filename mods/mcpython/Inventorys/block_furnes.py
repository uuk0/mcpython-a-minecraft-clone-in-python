from .Inventory import *
from oredictnames import *
import crafting
import globals as G


class furnes(Inventory):
    def getId(self):
        return 5

    def getSlots(self):
        s =    [Slot(310, 315), Slot(310, 230),
                Slot(0, 0, mode="o", stid="minecraft:slot:furnes:out")]
        return s

    def getImage(self):
        for e in self.slots:
            print(e, e.id)
        return './assets/textures/gui/furnace.png'

    def getDepedens(self):
        return [0, 1]

    def getImagePos(self):
        return (180, 10)

    def getInventoryDependence(self):
        return [0, 1, 2, 3]

    def on_show(self):
        for i in self.getInventoryDependence():
            G.inventoryhandler.show(i)



handler.register(furnes)