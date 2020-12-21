from moduls import *

from oredictnames import *

from Inventorys import *

import Item

import crafting as cb
import config

from Inventorys import *
from Inventorys.Inventory import Slot, handler as invhandler, InventoryHandler

import EventHandler
import entity


class player:
    def __init__(self, window):
        self.inventory = PlayerInventory(window, self)
        self.mode = 1  # 0:nichts, 1:hotbar, 2:survival_inventory, 3:creativ_inventory, 4: creativ_tab [self.creativ_tab_id], 5: crafting_table
        self.gamemode = config.CONFIGS[
            "DEFAULT_GAMEMODE"
        ]  # 0:surivival, 1:creativ, 2:hardcore, 3:spectator
        self.falling = False
        self.fallhigh = 0
        self.harts = 20
        self.hartholder = PlayerHartHandler(self)
        self.window = window
        self.creativ_tab_id = None
        self.block = None
        invhandler.show(0)
        self.dimension = 0
        self.inventorys = [
            self.inventory.hotbar,
            self.inventory.rows,
            self.inventory.armor,
            self.inventory.crafting,
        ]

        self.xp = 0
        self.hunger = 8
        self.model = entity.PlayerModel(self.window.position)
        self.model.player = self
        EventHandler.eventhandler.on_event("on_draw_3D", self.model.eventdraw)
        EventHandler.eventhandler.on_event("on_player_move", self.model.eventmove)

    def addToFreePlace(self, name, amount=1, start=0):
        if type(name) == list:
            for i, e in enumerate(name):
                self.addToFreePlace(e, amount[i], start)
            return True
        for i in self.inventorys:
            for e in i.slots:
                if e.id < start:
                    pass
                elif e.item and e.item.getName() == name:
                    if e.amount + amount - 1 < e.item.getMaxStackSize():
                        e.amount += amount
                        return True
                    elif e.amount < e.item.getMaxStackSize():
                        amount = amount - (e.item.getMaxStackSize() - e.amount)
                        e.amount = e.item.getMaxStackSize()
        for i in self.inventorys:
            for e in i.slots:
                if e.id < start:
                    pass
                elif not e.item:
                    print("setting ", 1)
                    e.setItem(name)
                    if e.item.getMaxStackSize() < amount and False:
                        e.amount = e.item.getMaxStackSize()
                        amount -= e.item.getMaxStackSize()
                    else:
                        e.amount = amount
                        return True
        print("[ERROR] no inventor place found")
        return False

    def setPlace(self, id, name):
        invhandler.sfromid[id].setItem(name)

    def getPlace(self, id):
        return invhandler.sfromid[id].item

    def getSlot(self, id):
        return invhandler.inventoryslotsinst[id]

    def update(self):
        if self.harts == 0 and self.gamemode != 3 and self.gamemode != 1:
            self.window.kill("player hearts go down")


class PlayerInventory:
    def __init__(self, window, master):
        self.window = window
        self.master = master
        self.hotbar = player_hotbar.hotbar()
        self.rows = player_rows.rows()
        self.armor = player_armor.armor()
        self.crafting = player_crafting.crafting()
        self.moving_slot = None
        self.moving_start = None
        self.none_slot = Slot(0, 0)

    def draw(self):
        pass

    def resetMovingSlot(self):
        self.moving_slot.setPos(*self.moving_start)

    def on_mouse_press(self, eventname, x, y, button, modifiers):
        if button == mouse.LEFT:
            if not self.moving_slot:
                # self.moving_slot = self.none_slot
                self.moving_slot = self.getPress(x, y)
                if self.moving_slot:
                    if invhandler.inventoryslotsinst[self.moving_slot.id].item:
                        self.moving_start = (
                            invhandler.inventoryslotsinst[self.moving_slot.id].x,
                            invhandler.inventoryslotsinst[self.moving_slot.id].y,
                        )
                        self.moving_slot = invhandler.inventoryslotsinst[
                            self.moving_slot.id
                        ]
                    else:
                        self.moving_slot = None
                else:
                    self.moving_slot = None
            else:
                end = self.getPress(x, y)
                if end and end.mode == "o":
                    return
                if end == None:
                    (self.moving_slot.x, self.moving_slot.y) = self.moving_start
                    self.moving_slot = None
                    return
                itemA = self.moving_slot.item
                itemB = end.item
                amountA = self.moving_slot.amount
                amountB = end.amount
                if (
                    self.moving_slot == self.crafting.slots[4]
                    or self.moving_slot.stid == "minecraft:slot:crafting_table:out"
                ):
                    cb.craftinghandler.removeOutput_player(self.master)
                    self.moving_slot.x, self.moving_slot.y = 531, 287
                    self.resetMovingSlot()
                if end.id in list(range(0, 9)):
                    self.rows.slots[end.id].setItem(end.item)
                    self.rows.slots[end.id].amount = end.amount
                if not itemB:
                    end.setItem(itemA)
                    end.amount = amountA
                    self.resetMovingSlot()
                    self.moving_slot.setItem(None)
                    self.moving_slot = None
                    cb.craftinghandler.updateOutput_player(self.master)
                    return
                elif itemA and itemB and itemA.getName() == itemB.getName():
                    if amountA + amountB <= itemA.getMaxStackSize():
                        end.amount = amountA + amountB
                        self.resetMovingSlot()
                        self.moving_slot.item = None
                        self.moving_slot = None
                        cb.craftinghandler.updateOutput_player(self.master)
                        return
                    else:
                        d = itemA.getMaxStackSize() - end.amount
                        end.amount = itemA.getMaxStackSize()
                        self.moving_slot.amount -= d
                        cb.craftinghandler.updateOutput_player(self.master)
                        return
                else:
                    end.setItem(itemA)
                    end.amount = amountA
                    self.moving_slot.setItem(itemB)
                    self.moving_slot.amount = amountB
                    self.moving_slot = None
                    cb.craftinghandler.updateOutput_player(self.master)
                    return
        elif button == mouse.RIGHT:
            if self.moving_slot:
                slot = self.getPress(x, y)
                if slot and (
                    (
                        slot.item
                        and slot.item.getName() == self.moving_slot.item.getName()
                    )
                    or not slot.item
                ):
                    if slot.amount + 1 <= self.moving_slot.item.getMaxStackSize():
                        slot.amount += 1
                        slot.setItem(self.moving_slot.item.getName())
                        self.moving_slot.amount -= 1
                        if self.moving_slot.amount == 0:
                            self.moving_slot.x, self.moving_slot.y = self.moving_start
                            self.moving_slot = None
                            cb.craftinghandler.updateOutput_player(self.master)
        elif (
            button == mouse.MIDDLE
            and not self.moving_slot
            and self.master.gamemode == 1
        ):
            slot = self.getPress(x, y)
            if not slot.item:
                return
            self.moving_slot = self.none_slot
            self.moving_start = (0, 0)
            self.moving_slot.setItem(slot.item)
            self.moving_slot.amount = slot.item.getMaxStackSize()

    def on_mouse_motion(self, eventname, x, y, dx, dy):
        if self.moving_slot:
            self.moving_slot.x, self.moving_slot.y = x, y

    def on_mouse_release(self, x, y, button, modifiers):
        pass

    def getPress(self, x, y, debug=False):
        self.scor = []
        for e in invhandler.shown:
            for e in invhandler.inventoryinst[e].slots:
                self.scor.append(e)

        slothigh, slotwight = 50, 40

        for s in self.scor:
            if x >= s.x:
                if x <= s.x + slotwight:
                    if y >= s.y:
                        if y <= s.y + slothigh:
                            if self.moving_slot == None or self.moving_slot.id != s.id:
                                return s
                            elif debug:
                                print(5, s, s.id)
                        elif debug:
                            print(4, s, s.id)
                    elif debug:
                        print(3, s, s.id)
                elif debug:
                    print(2, s, s.id)
            elif debug:
                print(1, s, s.id)
        return None

    def on_shift(self):
        pass


playerinst = None

import texturGroups


class PlayerHartHandler:
    def __init__(self, player):
        self.player = player
        res = texturGroups.handler.groups["./assets/textures/gui/icons/harts_no.png"]
        self.sprites = [
            pyglet.sprite.Sprite(res),
            pyglet.sprite.Sprite(res),
            pyglet.sprite.Sprite(res),
            pyglet.sprite.Sprite(res),
            pyglet.sprite.Sprite(res),
            pyglet.sprite.Sprite(res),
            pyglet.sprite.Sprite(res),
            pyglet.sprite.Sprite(res),
            pyglet.sprite.Sprite(res),
            pyglet.sprite.Sprite(res),
        ]  # pyglet.sprite.Sprite(texturGroups.handler.groups[imagefile])
        for i, e in enumerate(self.sprites):
            x = i * 20 + 190
            y = 80
            e.position = (x, y)

    def draw(self):
        if self.player.gamemode == 1 or self.player.gamemode == 3:
            return
        harts = self.player.harts
        for i, e in enumerate(self.sprites):
            if 2 * (i + 1) > harts:
                e.image = texturGroups.handler.groups[
                    "./assets/textures/gui/icons/harts_no.png"
                ]
            elif i * 2 < harts or (harts % 2 == 0 and i * 2 == harts):
                e.image = texturGroups.handler.groups[
                    "./assets/textures/gui/icons/hart_full.png"
                ]
            else:
                e.image = texturGroups.handler.groups[
                    "./assets/textures/gui/icons/hart_half.png"
                ]
            e.draw()
