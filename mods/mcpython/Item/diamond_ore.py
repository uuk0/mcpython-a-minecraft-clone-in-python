from .Item import *

class DiamondOre(Item):
    def getName(self):
        return "minecraft:diamond_ore"

    def getTexturFile(self):
        return "./assets/textures/items/diamond_ore.png"

handler.register(DiamondOre)
