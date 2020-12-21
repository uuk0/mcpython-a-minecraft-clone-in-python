from .Item import *
from destroyGroup import *
from oredictnames import OreDict


class diamondShovel(Item):
    def getName(self):
        return "minecraft:diamond_shovel"

    def hasBlock(self):
        return False

    def getPossibleEnchantments(self):
        return []

    def getDestroyGroup(self):
        return destroyGroups.SHOVEL

    def getTexturFile(self):
        return "./assets/textures/items/diamond_shovel.png"

    def getDestroyMultiplierWithTool(self, block):
        if destroyGroups.SHOVEL in block.getDestroyGroups():
            return 1
        return 3

    def getOreDictNames(self):
        return [OreDict.TOOL_SHOVEL]

    def getToolMaterial(self):
        return "minecraft:diamond"


handler.register(diamondShovel)


class diamondPickAxe(Item):
    def getTexturFile(self):
        return "./assets/textures/items/diamond_pickaxe.png"

    def getName(self):
        return "minecraft:diamond_pick_axe"

    def hasBlock(self):
        return False

    def getPossibleEnchantments(self):
        return []

    def getDestroyGroup(self):
        return destroyGroups.PIKAXE

    def getDestroyMultiplierWithTool(self, block):
        if destroyGroups.PIKAXE in block.getDestroyGroups():
            return 1
        return 3

    def getOreDictNames(self):
        return [OreDict.TOOL_PICKAXE]

    def getToolMaterial(self):
        return "minecraft:diamond"


handler.register(diamondPickAxe)


class diamondAxe(Item):
    def getTexturFile(self):
        return "./assets/textures/items/diamond_axe.png"

    def getName(self):
        return "minecraft:diamond_axe"

    def hasBlock(self):
        return False

    def getPossibleEnchantments(self):
        return []

    def getDestroyGroup(self):
        return destroyGroups.AXE

    def getDestroyMultiplierWithTool(self, block):
        if destroyGroups.AXE in block.getDestroyGroups():
            return 1
        return 3

    def getOreDictNames(self):
        return [OreDict.TOOL_AXE]

    def getToolMaterial(self):
        return "minecraft:diamond"


handler.register(diamondAxe)


class diamondSword(Item):
    def getTexturFile(self):
        return "./assets/textures/items/diamond_sword.png"

    def getName(self):
        return "minecraft:diamond_sword"

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
        return "minecraft:diamond"


handler.register(diamondSword)


class diamondHoe(Item):
    def getTexturFile(self):
        return "./assets/textures/items/diamond_hoe.png"

    def getName(self):
        return "minecraft:diamond_hoe"

    def hasBlock(self):
        return False

    def getPossibleEnchantments(self):
        return []

    def getDestroyGroup(self):
        return destroyGroups.HOE

    def getDestroyMultiplierWithTool(self, block):
        if destroyGroups.HOE in block.getDestroyGroups():
            return 1
        return 3

    def getOreDictNames(self):
        return [OreDict.TOOL_HOE]

    def getToolMaterial(self):
        return "minecraft:diamond"


handler.register(diamondHoe)
