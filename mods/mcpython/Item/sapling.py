from .Item import *


class Sapling(Item):
    def getName(self):
        return "minecraft:sapling"

    def getTexturFile(self):
        return "./assets/textures/items/sapling.png"

    def hasBlock(self):
        return False


handler.register(Sapling)
