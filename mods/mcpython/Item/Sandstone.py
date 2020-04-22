from .Item import *

class Sandstone(Item):
    def getName(self):
        return "minecraft:sandstone"

    def getTexturFile(self):
        return "./assets/textures/items/sandstone.png"

handler.register(Sandstone)
