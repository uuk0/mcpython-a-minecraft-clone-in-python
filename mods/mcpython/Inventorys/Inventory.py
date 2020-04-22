from moduls import *
import Item as Item_file
import texturGroups
from EventHandler import *
from config import CONFIGS
import traceback
import globals as G
import traceback
import states
import Item.Item as Item
import exceptionhandler

class InventoryHandler:
    def __init__(self):
        self.inventorys = []
        self.shown = []
        self.inventoryinst = {}
        self.inventoryslotsinst = {}
        self.window = None
        self.nextslotid = 0
        self.nextinvid = 0
        self.v1 = 0
        self.states = {}
        self.eventbinds = []
        self.active = []
        self.state = None

    def checkstates(self, eventname, statename):
        pass

    def register(self, klass):
        self.inventorys.append(klass)

    def show(self, id):
        if G.window:
            G.window.set_menü("minecraft:inventorys")
        else:
            G.statehandler.activate("minecraft:inventorys")
        self.state.show(self.inventoryinst[id])

    def hide(self, id):
        self.state.hide(self.inventoryinst[id])

    def registerInst(self, inst):
        print("[INFO] registering inventoryInst: "+str(inst))
        id = self.nextinvid
        self.states["inventory:open:" + str(id)] = inst
        inst.eventname = "inventory:open:" + str(id)
        print(inst, inst.eventname)
        CONFIGS["init"]["GAME_STATES"].append(inst.eventname)
        self.nextinvid += 1
        self.inventoryinst[id] = inst
        inst.id = id
        for e in inst.slots:
            self.registerSlotInst(e)
        if inst.getId() not in [0, 1, 2, 3]:
            self.active.append(inst.id)

    def registerSlotInst(self, slot):
        id = self.nextslotid
        self.nextslotid += 1
        self.inventoryslotsinst[id] = slot
        slot.id = id


    def changeId(self, invinst, id):
        key = None
        for e in self.inventoryinst.keys():
            if self.inventoryinst[e] == invinst:
                key = e
        invinst.id = id
        del self.inventoryinst[key]
        self.inventoryinst[id] = invinst

class InventoryState(G.State):
    def __init__(self):
        G.State.__init__(self)
        self.instevents = {}

    def getName(self):
        return "minecraft:inventorys"

    def activate(self):
        if G.window: G.window.set_exclusive_mouse(False)
        if G.player:
            self.events.append(
                eventhandler.on_event("on_mouse_press", G.player.inventory.on_mouse_press))
            self.events.append(
                eventhandler.on_event("on_mouse_motion", G.player.inventory.on_mouse_motion))
        self.events.append(eventhandler.on_event("on_key_press", self.key_press))

    def getDependencies(self):
        return ["minecraft:tilestate:world:model"]

    def show(self, inst):
        print("showing", inst)
        self.events.append(eventhandler.on_event("on_draw_2D", inst.draw))
        if not inst in self.instevents: self.instevents[inst] = []
        self.instevents[inst].append(self.events[-1])
        if G.window and not G.window.keyEvent == "minecraft:inventorys":
            G.window.set_menü("minecraft:inventorys")

    def hide(self, inst):
        if not inst in self.instevents: return
        for e in self.instevents[inst]:
            self.events.remove(e)
            eventhandler.unregister_on_event(e)
        del self.instevents[inst]
        if len(self.instevents) == 0:
            G.window.set_menü("minecraft:game")

    def key_press(self, eventname, symbol, modifiers):
        if symbol == key.ESCAPE:
            G.window.set_menü("minecraft:game")

G.statehandler.register(InventoryState)

handler = InventoryHandler()

handler.state = G.statehandler.instances["minecraft:inventorys"]

G.inventoryhandler = handler

def nonefunk(*args, **kwargs):
    pass

class Slot:
    def __init__(self, x, y, oredictallow=None, mode="a", stid=None, onupdate=nonefunk):
        self.image = None
        self.item = None
        self.x = x
        self.y = y
        self.startpos = (x, y)
        self.amount = 0
        self.id = 0
        self.stid = stid
        self.oredictallow = oredictallow
        self.update = onupdate
        self.debug = False
        if self.oredictallow != None and type(self.oredictallow) != list:
            self.oredictallow = [self.oredictallow]
        self.amountlabel = pyglet.text.Label('', font_name='Arial', font_size=10,
            x=self.x + 53, y=self.y - 3, anchor_x='left', anchor_y='top',
            color=(0, 0, 0, 255))
        self.mode = mode

    def setItem(self, item, amount=1, update=True):
        if item == None:
            self.image = None
            self.amount = 0
        else:
            if type(item) == str:
                try:
                    import Item.Item as Item
                    item = Item.handler.getClass(item)()
                except:
                    exceptionhandler.addTraceback()
                    return
            if self.oredictallow != None:
                flag = False
                for e in self.oredictallow:
                    if e in item.getOreDictNames():
                        flag = True
                if not flag:
                    print("[ERROR] try to add a item that is not definited to inventory", self, item.getName(), self.item.getOreDictNames() if self.item else None, self.id)
                    return False
            import Item.Item as Item
            if not isinstance(item, Item.Item):
                item = item()
            if not item or item.getTexturFile() == None:
                print("[ERROR] setting item -> item is None")
                return
            try:
                self.image = pyglet.sprite.Sprite(
                       texturGroups.handler.groups[item.getTexturFile()])
            except AttributeError:
                item = Item_file.handler.getClass(item)()
                self.image = pyglet.sprite.Sprite(
                    texturGroups.handler.groups[item.getTexturFile()])
            self.image.x = self.x
            self.image.y = self.y
            self.image.scale = 0.25
        self.item = item
        self.amount = amount
        if self.item: self.item.slot = self
        if item == None:
            self.amount = 0
        if update: self.update(self, item, amount)
        return True

    def draw(self):
        if self.amount == 0 and self.item:
            self.setItem(None)
        if not self.item:
            self.amount = 0
        if self.image != None:
            self.image.draw()
            self.amountlabel.x = self.x + 33
            self.amountlabel.y = self.y + 2
            self.amountlabel.text = str(self.amount)
            self.amountlabel.draw()
        if self.debug:
            print("[DEBUG/INFO] dawing slot", self.image, self.amount, self.item)

    def setPos(self, x, y, update=True):
        if update: self.update(self, self.item, self.amount)
        self.x = x
        self.y = y
        if self.image != None:
            self.image.x = x
            self.image.y = y

    def getData(self):
        return (self.item, self.amount)

    def setAmount(self, amount, update=True):
        if update: self.update(self, self.item, self.amount)
        if amount == 0:
            self.setItem(None)
        else:
            self.amount = amount

    def getDestroyHardness(self):
        if self.item == None:
            return 1
        else:
            return self.item.getToolHardness()

    def reset(self, update=True):
        self.setPos(self.startpos[0], self.startpos[1], update=update)

class Inventory:
    def __init__(self):
        self.slots = self.getSlots()
        self.id = 0
        self.eventname = None
        handler.registerInst(self)
        self.block = None
        if self.getImage():
            try:
                self.image = pyglet.sprite.Sprite(texturGroups.handler.groups[self.getImage()]) if self.getImage() != None else None
                if self.getImage() != None: self.image.x, self.image.y = self.getImagePos()
            except:
                print(self.getImage(), self.getId(), self)
                self.image = None
                print(traceback.print_exc())
                f = open(G.local + "/exceptions.txt", mode="a")
                f.write("\n[" + str(time.time()) + "] argv=" + str(sys.argv) + ", platform=" + str(sys.platform) +
                        ", mcpythonversion=" + str(config.CONFIGS["GAME_VERSION"]) + ", gameid=" + \
                        str(config.CONFIGS["VERSION_ID"]) + " \ntraceback:\n")
                f.write(str(traceback.extract_stack()))
                f.close()
        else:
            self.image = None

    def draw(self, *args, image=True):
        if self.image and image:
            self.image.draw()
        for e in self.slots:
            e.draw()

    def getSlots(self):
        return []

    def getImage(self):
        return None

    def getOverwrites(self):
        return []

    def getDepedens(self):
        return []

    def getImagePos(self):
        return (0, 0)

    def mouseOut(self):
        return True

    def drawBefore(self):
        return []

    def drawAfter(self):
        return []

    def drawWithoutImage(self):
        return []

    def getId(self):
        return None

    def getInventoryDependence(self):
        return []

    def on_show(self):
        pass