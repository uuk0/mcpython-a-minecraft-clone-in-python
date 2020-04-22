from .Item import *
from oredictnames import OreDict

class Coal(Item):
    def getName(self):
        return "minecraft:coal"

    def getTexturFile(self):
        return "./assets/textures/items/coal.png"

    def hasBlock(self):
        return False

    def getOreDictNames(self):
        return [OreDict.ORE_DROP, OreDict.Coal]

    def getOreMaterial(self):
        return "coal"

    def getFuelAmount(self):
        return 40

handler.register(Coal)
