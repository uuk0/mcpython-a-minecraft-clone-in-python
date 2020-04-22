from .Item import *

class melon(Item):
    def getName(self):
        return "minecraft:melon"

    def getTexturFile(self):
        return "./assets/textures/items/melon.png"

    def hasBlock(self):
        return False

handler.register(melon)
