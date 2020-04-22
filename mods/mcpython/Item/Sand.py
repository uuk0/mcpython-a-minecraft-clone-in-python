from .Item import *

class Sand(Item):
    def getName(self):
        return "minecraft:sand"

    def getTexturFile(self):
        return "./assets/textures/items/sand.png"

handler.register(Sand)
