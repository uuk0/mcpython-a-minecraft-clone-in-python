from .Inventory import *
from oredictnames import *
import crafting


class craftingtable(Inventory):
    def getId(self):
        return 4

    def getSlots(self):
        s = [
            Slot(250, 315),
            Slot(290, 315),
            Slot(330, 315),
            Slot(250, 275),
            Slot(290, 275),
            Slot(330, 275),
            Slot(250, 233),
            Slot(290, 233),
            Slot(330, 233),
            Slot(464, 275, mode="o", stid="minecraft:slot:crafting_table:out"),
        ]
        return s

    def getImage(self):
        return "./assets/textures/gui/crafting_table.png"

    def getDepedens(self):
        return [0, 1]

    def getImagePos(self):
        return (180, 10)

    def getInventoryDependence(self):
        return [0, 1, 2, 3]


handler.register(craftingtable)
