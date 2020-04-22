from .Item import *

class GoldOre(Item):
    def getName(self):
        return "minecraft:gold_ore"

    def getTexturFile(self):
        return "./assets/textures/items/gold_ore.png"

handler.register(GoldOre)
