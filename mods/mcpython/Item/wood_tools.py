from .Item import *
from destroyGroup import *
from oredictnames import OreDict

class WoodShovel(Item):
    def getName(self):
        return "minecraft:wood_shovel"

    def hasBlock(self):
        return False

    def getPossibleEnchantments(self):
        return []

    def getDestroyGroup(self):
        return destroyGroups.SHOVEL

    def getTexturFile(self):
        return "./assets/textures/items/wood_shovel.png"

    def getDestroyMultiplierWithTool(self, block):
        if destroyGroups.SHOVEL in block.getDestroyGroups():
            return 2.3
        return 3

    def getOreDictNames(self):
        return [OreDict.TOOL_SHOVEL]

    def getToolMaterial(self):
        return "minecraft:wood"

    def getFuelAmount(self):
        return 10

handler.register(WoodShovel)

class WoodPickAxe(Item):
    def getTexturFile(self):
        return "./assets/textures/items/wood_pickaxe.png"

    def getName(self):
        return "minecraft:wood_pick_axe"

    def hasBlock(self):
        return False

    def getPossibleEnchantments(self):
        return []

    def getDestroyGroup(self):
        return destroyGroups.PIKAXE

    def getDestroyMultiplierWithTool(self, block):
        if destroyGroups.PIKAXE in block.getDestroyGroups():
            return 2.3
        return 3

    def getOreDictNames(self):
        return [OreDict.TOOL_PICKAXE]

    def getToolMaterial(self):
        return "minecraft:wood"

    def getFuelAmount(self):
        return 10

handler.register(WoodPickAxe)

class WoodAxe(Item):
    def getTexturFile(self):
        return "./assets/textures/items/wood_axe.png"

    def getName(self):
        return "minecraft:wood_axe"

    def hasBlock(self):
        return False

    def getPossibleEnchantments(self):
        return []

    def getDestroyGroup(self):
        return destroyGroups.AXE

    def getDestroyMultiplierWithTool(self, block):
        if destroyGroups.AXE in block.getDestroyGroups():
            return 2.3
        return 3

    def getOreDictNames(self):
        return [OreDict.TOOL_AXE]

    def getToolMaterial(self):
        return "minecraft:wood"

    def getFuelAmount(self):
        return 10

handler.register(WoodAxe)

class WoodSword(Item):
    def getTexturFile(self):
        return "./assets/textures/items/wood_sword.png"

    def getName(self):
        return "minecraft:wood_sword"

    def hasBlock(self):
        return False

    def getPossibleEnchantments(self):
        return []

    def getDestroyGroup(self):
        return destroyGroups.SWORD

    def getDestroyMultiplierWithTool(self, block):
        return 3

    def getOreDictNames(self):
        return [OreDict.TOOL_SWORD]

    def getToolMaterial(self):
        return "minecraft:wood"

    def getFuelAmount(self):
        return 10

handler.register(WoodSword)

class WoodHoe(Item):
    def getTexturFile(self):
        return "./assets/textures/items/wood_hoe.png"

    def getName(self):
        return "minecraft:wood_hoe"

    def hasBlock(self):
        return False

    def getPossibleEnchantments(self):
        return []

    def getDestroyGroup(self):
        return destroyGroups.HOE

    def getDestroyMultiplierWithTool(self, block):
        if destroyGroups.HOE in block.getDestroyGroups():
            return 2.3
        return 3

    def getOreDictNames(self):
        return [OreDict.TOOL_HOE]

    def getToolMaterial(self):
        return "minecraft:wood"

    def getFuelAmount(self):
        return 10


handler.register(WoodHoe)