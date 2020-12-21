from .Item import *


class Redstone(Item):
    def getName(self):
        return "minecraft:redstone"

    def getTexturFile(self):
        return "./assets/textures/items/redstone.png"


handler.register(Redstone)
