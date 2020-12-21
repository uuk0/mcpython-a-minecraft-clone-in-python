from .Item import *


class CoalOre(Item):
    def getName(self):
        return "minecraft:coal_ore"

    def getTexturFile(self):
        return "./assets/textures/items/coal_ore.png"


handler.register(CoalOre)
