from .Item import *
from oredictnames import OreDict


class Gold(Item):
    def getName(self):
        return "minecraft:gold"

    def getTexturFile(self):
        return "./assets/textures/items/gold_ingot.png"

    def hasBlock(self):
        return False

    def getOreMaterial(self):
        return "gold"

    def getOreDictNames(self):
        return [OreDict.ORE_DROP]


handler.register(Gold)
