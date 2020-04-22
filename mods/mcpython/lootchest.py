import Blocks
import Item
import Random
import globals as G
import random


class LootChest:
    def __init__(self):
        pass

    def getItems(self):
        return [] #element: [name, amount]

    def getID(self):
        return "minecraft:loottable:null"

    def past(self, pos):
        G.model.add_block(pos, "minecraft:chest")
        chest = G.model.world[pos]
        il = self.getItems()
        while len(il) < 9 * 6:
            il.append(None)
        if self.isRandomCalc():
            random.shuffle(il)
        for i, e in enumerate(chest.inv.slots):
            if il[i]:
                e.setItem(il[i][0], amount=il[i][1])
            else:
                e.setItem(None)

    def isRandomCalc(self):
        return True

class StartChest(LootChest):
    def getItems(self):
        return [["minecraft:wood_shovel", 1], ["minecraft:wood_axe", 1], ["minecraft:wood_pick_axe", 1],
                ["minecraft:stick", 4], ["minecraft:wood_log_0", 10]]

    def getID(self):
        return "minecraft:loottable:startchest"

LOOTCHESTS = {StartChest().getID():StartChest}