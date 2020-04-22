
from destroyGroup import *
#from Inventorys.Inventory import handler as invhandler
import globals as G

class ItemHandler:
    def __init__(self):
        self.nametoitem = {}
        self.prefixes = []

    def register(self, itemclass):
        name = itemclass().getName()
        self.nametoitem[name] = itemclass
        if not name.split(":")[0] in self.prefixes:
            self.prefixes.append(name.split(":")[0])

    def getClass(self, name):
        if type(name) == str:
            if name in self.nametoitem:
                return self.nametoitem[name]
            for pre in self.prefixes:
                if pre+":"+name in self.nametoitem:
                    return self.nametoitem[pre+":"+name]
            print("[ERROR] "+str(name)+" not found")
            return None
        return name()

handler = ItemHandler()

class LiquidBucketHandler:
    def __init__(self):
        self.liquids = {}
        self.holders = []

    def register(self, itemclass, liquidname):
        if not liquidname in self.liquids:
            self.liquids[liquidname] = []
        self.liquids[liquidname].append(itemclass)

    def registerHolder(self, itemclass):
        self.holders.append(itemclass)

liquidhandler = LiquidBucketHandler()

class Item:
    def __init__(self):
        self.blocknbt = {}
        self.mode = "ITEM"
        self.slot = None

    def getName(self):
        return "minecraft:none"

    def getTexturFile(self):
        return "./texturs/none.png"

    def hasBlock(self):
        return True

    def getMaxStackSize(self):
        return 64

    def getToolHardness(self):
        return 1 #1/n multiplier

    def getAttackDamage(self):
        return 1

    def getDestroyGroup(self):
        return []

    def getDestroyMultiplierWithTool(self, block):
        return 3

    def getOreDictNames(self):
        return []

    def __call__(self):
        obj =  self.__class__()
        obj.blocknbt = self.blocknbt.copy()
        return obj

    def getFuelAmount(self):
        return 0

    def on_right_click(self, block, previos, button, modifiers):
        if not block: return
        if G.model.world[block].hasInventory():
            invhandler.show(G.model.world[block].getInventoryID())
        else:
            block.on_right_click(block, previos, button, modifiers)

    def canDestroyBlock(self, block, button, modifiers):
        return True

    def on_left_click(self, window, block, previos, button, modifiers):
        window.model.world[block].on_left_click(block, previos, button, modifiers)

    def isEnchantAble(self):
        return False

    def getEnchantments(self):
        return []

    def getPossibleEnchantments(self):
        return []

    def getToolMaterial(self):
        return None

    def getOreMaterial(self): #used for in-placing
        return None

    def getLiquidHoldName(self):
        return ""

    def on_destroy_with(self, block):
        pass

    def getHoldAbleLiquids(self):
        return []

    def on_block_set(self, position):
        pass

    def getBlockName(self):
        return self.getName()

    def isEatAble(self): #!
        return False

    def getHungerReward(self): #!
        return 0

    def canInteractWith(self, block):
        return False

    def interactWith(self, block):
        pass

    def getStoreData(self):
        pass

    def setStoreData(self, data):
        pass