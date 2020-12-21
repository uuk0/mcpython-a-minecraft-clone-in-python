import Inventorys
from .Block import *

# from player import Slot
import crafting


class crafting_table(Block):
    def __init__(self, *args, **kwargs):
        Block.__init__(self, *args, **kwargs)
        self.stored = []

    def getTex(self):
        return tex_coords((14, 11), (14, 11), (14, 12))

    def getName(self):
        return "minecraft:crafting_table"

    def getNBTNames(self):
        names = []
        for e in range(10):
            names.append("inventory_" + str(e) + "_x")
            names.append("inventory_" + str(e) + "_y")
            names.append("inventory_" + str(e) + "_item")

        return names

    def drawInventory(self):
        pass

    def setNBT(self, name, value):
        pass

    def getNBT(self, name):
        pass

    def getAllNBT(self):
        return []

    def getAllItemNBT(self):
        return {}

    def setAllNBT(self, nbt):
        pass

    def hasInventory(self):
        return True

    def getInventoryID(self):
        return self.inv.id

    def on_creat(self):
        self.inv = Inventorys.craftingtable()
        self.inv.eventname = "inventory:open:" + str(self.inv.id)
        self.inv.block = self
        self.crafting_recipi = None
        self.crafting_recipi_slots = []
        for e in self.inv.slots:
            e.update = self.crafting_update

    def crafting_update(self, slot, item, amount):
        if item == None:
            if slot.stid != "minecraft:slot:crafting_table:out":
                if slot in self.stored:
                    self.stored.remove(slot)
                    self.crafting_output_check()
            else:
                self.remove_output()
                self.crafting_output_check()
        else:
            if slot.stid != "minecraft:slot:crafting_table:out":
                if not slot.item and item:
                    slot.setItem(item.getName(), amount)
                self.crafting_output_check()
                slot.setItem(item.getName(), amount, update=False)
                if not slot in self.stored:
                    self.stored.append(slot)

    def check_stored(self):
        self.stored = []
        for e in self.inv.slots[:-1]:
            if e.item:
                self.stored.append(e)

    def crafting_output_check(self):
        self.check_stored()
        si = []
        for e in self.inv.slots:
            si.append([e])
        if self.check_crafting(
            crafting.Grid.crafting_1x1,
            crafting.craftinghandler.recipis[crafting.Grid.crafting_1x1],
            si,
        ):
            return
        if self.check_crafting(
            crafting.Grid.crafting_1x2,
            crafting.craftinghandler.recipis[crafting.Grid.crafting_1x2],
            [
                [self.inv.slots[0], self.inv.slots[3]],
                [self.inv.slots[1], self.inv.slots[4]],
                [self.inv.slots[2], self.inv.slots[5]],
                [self.inv.slots[3], self.inv.slots[6]],
                [self.inv.slots[4], self.inv.slots[7]],
                [self.inv.slots[5], self.inv.slots[8]],
            ],
        ):
            return
        if self.check_crafting(
            crafting.Grid.crafting_2x1,
            crafting.craftinghandler.recipis[crafting.Grid.crafting_2x1],
            [
                self.inv.slots[0:1],
                self.inv.slots[1:2],
                self.inv.slots[3:4],
                self.inv.slots[4:5],
                self.inv.slots[6:7],
                self.inv.slots[7:8],
            ],
        ):
            return
        if self.check_crafting(
            crafting.Grid.crafting_2x2,
            crafting.craftinghandler.recipis[crafting.Grid.crafting_2x2],
            [
                self.inv.slots[0:2] + self.inv.slots[3:5],
                self.inv.slots[1:3] + self.inv.slots[4:6],
                self.inv.slots[3:5] + self.inv.slots[6:8],
                self.inv.slots[4:6] + self.inv.slots[7:9],
            ],
        ):
            return
        if self.check_crafting(
            crafting.Grid.crafting_1x3,
            crafting.craftinghandler.recipis[crafting.Grid.crafting_1x3],
            [
                [self.inv.slots[0], self.inv.slots[3], self.inv.slots[6]],
                [self.inv.slots[1], self.inv.slots[4], self.inv.slots[7]],
                [self.inv.slots[2], self.inv.slots[5], self.inv.slots[8]],
            ],
        ):
            return
        if self.check_crafting(
            crafting.Grid.crafting_3x1,
            crafting.craftinghandler.recipis[crafting.Grid.crafting_3x1],
            [self.inv.slots[0:3], self.inv.slots[3:6], self.inv.slots[6:9]],
        ):
            return
        if self.check_crafting(
            crafting.Grid.crafting_3x2,
            crafting.craftinghandler.recipis[crafting.Grid.crafting_3x2],
            [self.inv.slots[0:6], self.inv.slots[3:9]],
        ):
            return
        if self.check_crafting(
            crafting.Grid.crafting_2x3,
            crafting.craftinghandler.recipis[crafting.Grid.crafting_2x3],
            [
                self.inv.slots[0:2] + self.inv.slots[3:5] + self.inv.slots[6:8],
                self.inv.slots[1:3] + self.inv.slots[4:6] + self.inv.slots[7:9],
            ],
        ):
            return
        if self.check_crafting(
            crafting.Grid.crafting_3x3,
            crafting.craftinghandler.recipis[crafting.Grid.crafting_3x3],
            [self.inv.slots[:9]],
        ):
            return
        inv = self.inv
        Grid = crafting.Grid
        items = []
        itemnames = {}
        a = inv.slots[:9]
        for i, e in enumerate(a):
            if e.item:
                items.append(e)
                if not e.item.getName() in itemnames:
                    itemnames[e.item.getName()] = []
                itemnames[e.item.getName()].append(e)
        for c in self.recipis[Grid.crafting_shapeless]:
            rclist = itemnames.copy()
            if len(c.input) <= 9 and len(c.input) == len(items):
                flag = True
                for i, e in enumerate(c.input):
                    if not e in rclist.keys():
                        flag = False
                    elif len(rclist[e]) == 0:
                        flag = False
                    else:
                        rclist[e].pop(0)
                if flag:
                    rcitems = []
                    for e in items:
                        flag = True
                        for rc in rclist.keys():
                            if e in rclist[rc]:
                                flag = False
                        if flag:
                            rcitems.append(e)
                    self.crafting_recipi = c
                    self.crafting_recipi_slots = rcitems
                    inv.slots[4].setItem(c.output[0])
                    inv.slots[4].amount = c.outputamount[0]
                    return
        self.crafting_recipi = None
        self.crafting_recipi_slots = []
        self.inv.slots[8].setItem(None)

    def remove_output(self):
        if not self.crafting_recipi:
            return
        for i, e in enumerate(self.crafting_recipi.inputamount):
            self.crafting_recipi_slots[i].amount -= e
            if self.crafting_recipi_slots[i] == 0:
                self.crafting_recipi_slots[i].setItem(None)
        self.inv.slots[9].setPos(464, 275, update=False)

    def check_crafting(self, grid, recipis, slotgroups):
        try:
            for c in recipis:
                sll = slotgroups
                for si in range(0, len(sll)):
                    sl = sll[si]
                    flag = (
                        len(self.stored) == len(slotgroups[0])
                        if grid != crafting.Grid.crafting_3x3
                        else True
                    )
                    for i, s in enumerate(sl):
                        if i < 9:
                            try:
                                if (
                                    not (
                                        s.item
                                        and s.item.getName() == c.input[i]
                                        and s.amount >= c.inputamount[i]
                                    )
                                    and flag
                                ) or (c.input[i] == None and flag):
                                    if (not s.item and c.input[i]) or (
                                        s.item
                                        and not c.input[i] in s.item.getOreDictNames()
                                    ):
                                        flag = False
                            except:
                                raise
                    if flag:
                        self.crafting_recipi = c
                        self.crafting_recipi_slots = sl
                        self.inv.slots[9].setItem(c.output[0])
                        self.inv.slots[9].amount = c.outputamount[0]
                        return True
        except:
            print(recipis)
            raise

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


handler.register(crafting_table)
