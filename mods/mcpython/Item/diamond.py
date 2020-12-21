from .Item import *
from oredictnames import OreDict


class Diamond(Item):
    def getName(self):
        return "minecraft:diamond"

    def getTexturFile(self):
        return "./assets/textures/items/diamond.png"

    def hasBlock(self):
        return False

    def getOreMaterial(self):
        return "diamond"

    def getOreDictNames(self):
        return [OreDict.ORE_DROP]


handler.register(Diamond)
