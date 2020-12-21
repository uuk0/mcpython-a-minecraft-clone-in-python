from .Block import *
import Inventorys
import crafting
import time
import TickHandler
import globals as G


class furnes(Block):
    def on_creat(self):
        self.inv = None
        self.fueltime = 0
        self.fuelamount = 0  # the value of stored fuel
        self.storedfuel = 0  # the value of fuel that is used for crafting
        self.maxstoreablefuel = 100  # the value of fuel that can be stored max
        self.inv = Inventorys.furnes()
        self.inv.block = self
        self.inv.eventname = "inventory:open:" + str(self.inv.id)
        self.crafting_recipi = None
        for e in self.inv.slots:
            e.update = self.crafting_update
        self.burnstarttime = None  #
        self.running = False
        self.outputstoredxp = 0

    def crafting_update(self, slot, item, amount):
        if slot == self.inv.slots[0] and slot.item:
            for e in crafting.craftinghandler.recipis[crafting.Grid.crafting_smelting]:
                if (
                    e.input[0] == self.inv.slots[0].item.getName()
                    or e.input[0] in self.inv.slots[0].item.getOreDictNames()
                ):
                    if e.inputamount[0] >= self.inv.slots[0].amount and (
                        not self.inv.slots[2].item
                        or self.inv.slots[2].item.getName() == e.output[0]
                    ):
                        if e != self.crafting_recipi:
                            self.crafting_recipi = e
                            self.burnstarttime = time.time()
                            self.storedfuel = 0
                        if not self.running:
                            TickHandler.handler.run(self.tickUpdate, 1)
                        return
            self.crafting_recipi = None
            self.burnstarttime = None
        elif (
            slot == self.inv.slots[1]
            and slot.item
            and self.crafting_recipi
            and not self.running
        ):
            TickHandler.handler.run(self.tickUpdate, 1)
        elif slot == self.inv.slots[2]:
            G.player.xp += self.outputstoredxp
            self.outputstoredxp = 0

    def tickUpdate(self):
        if not self.inv.slots[1].item:
            self.running = False
            return
        if not self.crafting_recipi:
            if self.storedfuel > 0:
                self.storedfuel -= 5
            return
        if self.storedfuel >= self.crafting_recipi.kwargs["fuel"]:
            if not self.inv.slots[2].item:
                self.inv.slots[2].setItem(self.crafting_recipi.output[0])
                self.inv.slots[2].amount = self.crafting_recipi.outputamount[0]
                self.inv.slots[0].amount -= self.crafting_recipi.inputamount[0]
                self.storedfuel = 0
                self.running = False
                self.outputstoredxp += self.crafting_recipi.kwargs["xp"]
                return
            elif self.inv.slots[2].item.getName() == self.crafting_recipi.output[0]:
                self.inv.slots[2].amount += self.crafting_recipi.outputamount[0]
                self.inv.slots[0].amount -= self.crafting_recipi.inputamount[0]
                self.running = False
                self.storedfuel = 0
                self.outputstoredxp += self.crafting_recipi.kwargs["xp"]
                return
            else:
                print(
                    "[ERROR] during checking furnes recipi: furnes recipi is set but output is incorrect"
                )
                self.crafting_recipi = None
                self.running = False
                return
            if self.inv.slots[0].amount == 0:
                self.inv.slots[0].setItem(None)
                self.crafting_recipi = None
                self.running = False
                return
        else:
            if self.inv.slots[1].item:
                if (
                    self.inv.slots[1].item.getFuelAmount() > 0
                    and self.fuelamount + self.inv.slots[1].item.getFuelAmount()
                    <= self.maxstoreablefuel
                ):
                    self.fuelamount += self.inv.slots[1].item.getFuelAmount()
                    self.inv.slots[1].amount -= 1
                    if self.inv.slots[1].amount == 0:
                        self.inv.slots[1].setItem(None)
            if time.time() >= self.fueltime + 0.5:
                self.fueltime = time.time()
                fuel = (
                    5
                    if not "fuelpertime" in self.crafting_recipi.kwargs
                    else self.crafting_recipi.kwargs["fuelpertime"]
                )
                if self.fuelamount >= fuel:
                    self.fuelamount -= fuel
                    self.storedfuel += fuel
        if self.slots[0].item == None:
            self.running = False
            return
        self.running = True
        TickHandler.handler.run(self.tickUpdate, 1)

    def getTex(self):
        if self.fueltime > 0:
            return total_tex_coords(
                (13, 14), (13, 14), (14, 15), (13, 15), (13, 15), (13, 15)
            )
        else:
            return total_tex_coords(
                (13, 14), (13, 14), (14, 14), (13, 15), (13, 15), (13, 15)
            )

    def getName(self):
        return "minecraft:furnes"

    destroygroups = [destroyGroups.PIKAXE]

    def hasInventory(self):
        return True

    def getInventorys(self):
        return [self.inv]

    def getInventoryID(self):
        return self.inv.id

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


handler.register(furnes)
