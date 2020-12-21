from .Item import *


class IronOre(Item):
    def getName(self):
        return "minecraft:iron_ore"

    def getTexturFile(self):
        return "./assets/textures/items/iron_ore.png"


handler.register(IronOre)
