from .Item import *


class DiamondBlock(Item):
    def getName(self):
        return "minecraft:diamond_block"

    def getTexturFile(self):
        return "./assets/textures/items/diamond_block.png"


handler.register(DiamondBlock)
