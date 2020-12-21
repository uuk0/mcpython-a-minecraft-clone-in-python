from .Item import *
from destroyGroup import *
from oredictnames import OreDict


class goldShovel(Item):
    def getName(self):
        return "minecraft:gold_shovel"

    def hasBlock(self):
        return False

    def getPossibleEnchantments(self):
        return []

    def getDestroyGroup(self):
        return destroyGroups.SHOVEL

    def getTexturFile(self):
        return "./assets/textures/items/gold_shovel.png"

    def getDestroyMultiplierWithTool(self, block):
        if destroyGroups.SHOVEL in block.getDestroyGroups():
            return 1.4
        return 3

    def getOreDictNames(self):
        return [OreDict.TOOL_SHOVEL]

    def getToolMaterial(self):
        return "minecraft:gold"


handler.register(goldShovel)


class goldPickAxe(Item):
    def getTexturFile(self):
        return "./assets/textures/items/gold_pickaxe.png"

    def getName(self):
        return "minecraft:gold_pick_axe"

    def hasBlock(self):
        return False

    def getPossibleEnchantments(self):
        return []

    def getDestroyGroup(self):
        return destroyGroups.PIKAXE

    def getDestroyMultiplierWithTool(self, block):
        if destroyGroups.PIKAXE in block.getDestroyGroups():
            return 1.4
        return 3

    def getOreDictNames(self):
        return [OreDict.TOOL_PICKAXE]

    def getToolMaterial(self):
        return "minecraft:gold"


handler.register(goldPickAxe)


class goldAxe(Item):
    def getTexturFile(self):
        return "./assets/textures/items/gold_axe.png"

    def getName(self):
        return "minecraft:gold_axe"

    def hasBlock(self):
        return False

    def getPossibleEnchantments(self):
        return []

    def getDestroyGroup(self):
        return destroyGroups.AXE

    def getDestroyMultiplierWithTool(self, block):
        if destroyGroups.AXE in block.getDestroyGroups():
            return 1.4
        return 3

    def getOreDictNames(self):
        return [OreDict.TOOL_AXE]

    def getToolMaterial(self):
        return "minecraft:gold"


handler.register(goldAxe)


class goldSword(Item):
    def getTexturFile(self):
        return "./assets/textures/items/gold_sword.png"

    def getName(self):
        return "minecraft:gold_sword"

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
        return "minecraft:gold"


handler.register(goldSword)


class goldHoe(Item):
    def getTexturFile(self):
        return "./assets/textures/items/gold_hoe.png"

    def getName(self):
        return "minecraft:gold_hoe"

    def hasBlock(self):
        return False

    def getPossibleEnchantments(self):
        return []

    def getDestroyGroup(self):
        return destroyGroups.HOE

    def getDestroyMultiplierWithTool(self, block):
        if destroyGroups.HOE in block.getDestroyGroups():
            return 1.4
        return 3

    def getOreDictNames(self):
        return [OreDict.TOOL_HOE]

    def getToolMaterial(self):
        return "minecraft:gold"


handler.register(goldHoe)
