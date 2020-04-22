from .Item import *
from oredictnames import OreDict

class Iron(Item):
    def getName(self):
        return "minecraft:iron"

    def getTexturFile(self):
        return "./assets/textures/items/iron_ingot.png"

    def hasBlock(self):
        return False

    def getOreMaterial(self):
        return "iron"

    def getOreDictNames(self):
        return [OreDict.ORE_DROP]

handler.register(Iron)
