from .Item import *

class Grass(Item):
    def getName(self):
        return "minecraft:grass"

    def getTexturFile(self):
        return "./assets/textures/items/grass_item.png"

handler.register(Grass)
