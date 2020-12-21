import Inventorys
from .Block import *
from player import Slot
import crafting


class chest(Block):
    def getTex(self):
        return total_tex_coords((8, 4), (8, 2), (8, 3), (8, 3), (8, 3), (8, 3))

    def getName(self):
        return "minecraft:chest"

    def getNBTNames(self):
        names = []
        for e in range(6 * 9):
            names.append("inventory_" + str(e) + "_x")
            names.append("inventory_" + str(e) + "_y")
            names.append("inventory_" + str(e) + "_item")

        return names

    def hasInventory(self):
        return True

    def getInventoryID(self):
        return self.inv.id

    def on_creat(self):
        self.inv = Inventorys.block_chest.chest()
        self.inv.block = self

    def getInventoryID(self):
        return self.inv.id

    destroygroups = [destroyGroups.AXE]

    def getDrop(self, item):
        items = [self.getName()]
        for e in self.inv.slots:
            if e.item:
                items.append(e.item.getName())
        return items

    def getDropAmount(self, item):
        items = [1]
        for e in self.inv.slots:
            if e.item:
                items.append(e.amount)
        return items

    def getInventorys(self):
        return [self.inv]


handler.register(chest)
