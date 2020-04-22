from .Item import *

class Cactus(Item):
    def getName(self):
        return "minecraft:cactus"

    def getTexturFile(self):
        return "./assets/textures/items/cactus.png"

handler.register(Cactus)
