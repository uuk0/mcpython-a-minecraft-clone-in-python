from .Item import *
from destroyGroup import *
from oredictnames import OreDict


class IronShovel(Item):
    def getName(self):
        return "minecraft:iron_shovel"

    def hasBlock(self):
        return False

    def getPossibleEnchantments(self):
        return []

    def getDestroyGroup(self):
        return destroyGroups.SHOVEL

    def getTexturFile(self):
        return "./assets/textures/items/iron_shovel.png"

    def getDestroyMultiplierWithTool(self, block):
        if destroyGroups.SHOVEL in block.getDestroyGroups():
            return 1.4
        return 3

    def getOreDictNames(self):
        return [OreDict.TOOL_SHOVEL]

    def getToolMaterial(self):
        return "minecraft:iron"


handler.register(IronShovel)


class IronPickAxe(Item):
    def getTexturFile(self):
        return "./assets/textures/items/iron_pickaxe.png"

    def getName(self):
        return "minecraft:iron_pick_axe"

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
        return "minecraft:iron"


handler.register(IronPickAxe)


class IronAxe(Item):
    def getTexturFile(self):
        return "./assets/textures/items/iron_axe.png"

    def getName(self):
        return "minecraft:iron_axe"

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
        return "minecraft:iron"


handler.register(IronAxe)


class IronSword(Item):
    def getTexturFile(self):
        return "./assets/textures/items/iron_sword.png"

    def getName(self):
        return "minecraft:iron_sword"

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
        return "minecraft:iron"


handler.register(IronSword)


class IronHoe(Item):
    def getTexturFile(self):
        return "./assets/textures/items/iron_hoe.png"

    def getName(self):
        return "minecraft:iron_hoe"

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
        return "minecraft:iron"


handler.register(IronHoe)
