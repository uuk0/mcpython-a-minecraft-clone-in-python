from .Item import *

class Water(Item):
    def getName(self):
        return "minecraft:water"

    def getTexturFile(self):
        return "./assets/textures/items/water.png"

handler.register(Water)
