from .Item import *

class Pumpkin(Item):
    def getName(self):
        return "minecraft:pumpkin"

    def getTexturFile(self):
        return "./assets/textures/items/pumpkin.png"

handler.register(Pumpkin)
