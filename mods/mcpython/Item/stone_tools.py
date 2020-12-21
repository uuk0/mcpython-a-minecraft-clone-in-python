from .Item import *
from destroyGroup import *
from oredictnames import OreDict


class StoneShovel(Item):
    def getName(self):
        return "minecraft:stone_shovel"

    def hasBlock(self):
        return False

    def getPossibleEnchantments(self):
        return []

    def getDestroyGroup(self):
        return destroyGroups.SHOVEL

    def getTexturFile(self):
        return "./assets/textures/items/stone_shovel.png"

    def getDestroyMultiplierWithTool(self, block):
        if destroyGroups.SHOVEL in block.getDestroyGroups():
            return 2
        return 3

    def getOreDictNames(self):
        return [OreDict.TOOL_SHOVEL]

    def getToolMaterial(self):
        return "minecraft:stone"


handler.register(StoneShovel)


class StonePickAxe(Item):
    def getTexturFile(self):
        return "./assets/textures/items/stone_pickaxe.png"

    def getName(self):
        return "minecraft:stone_pick_axe"

    def hasBlock(self):
        return False

    def getPossibleEnchantments(self):
        return []

    def getDestroyGroup(self):
        return destroyGroups.PIKAXE

    def getDestroyMultiplierWithTool(self, block):
        if destroyGroups.PIKAXE in block.getDestroyGroups():
            return 2
        return 3

    def getOreDictNames(self):
        return [OreDict.TOOL_PICKAXE]

    def getToolMaterial(self):
        return "minecraft:stone"


handler.register(StonePickAxe)


class StoneAxe(Item):
    def getTexturFile(self):
        return "./assets/textures/items/stone_axe.png"

    def getName(self):
        return "minecraft:stone_axe"

    def hasBlock(self):
        return False

    def getPossibleEnchantments(self):
        return []

    def getDestroyGroup(self):
        return destroyGroups.AXE

    def getDestroyMultiplierWithTool(self, block):
        if destroyGroups.AXE in block.getDestroyGroups():
            return 2
        return 3

    def getOreDictNames(self):
        return [OreDict.TOOL_AXE]

    def getToolMaterial(self):
        return "minecraft:stone"


handler.register(StoneAxe)


class StoneSword(Item):
    def getTexturFile(self):
        return "./assets/textures/items/stone_sword.png"

    def getName(self):
        return "minecraft:stone_sword"

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
        return "minecraft:stone"


handler.register(StoneSword)


class StoneHoe(Item):
    def getTexturFile(self):
        return "./assets/textures/items/stone_hoe.png"

    def getName(self):
        return "minecraft:stone_hoe"

    def hasBlock(self):
        return False

    def getPossibleEnchantments(self):
        return []

    def getDestroyGroup(self):
        return destroyGroups.HOE

    def getDestroyMultiplierWithTool(self, block):
        if destroyGroups.HOE in block.getDestroyGroups():
            return 2
        return 3

    def getOreDictNames(self):
        return [OreDict.TOOL_HOE]

    def getToolMaterial(self):
        return "minecraft:stone"


handler.register(StoneHoe)
