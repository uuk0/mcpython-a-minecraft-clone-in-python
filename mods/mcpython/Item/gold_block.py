from .Item import *

class GoldBlock(Item):
    def getName(self):
        return "minecraft:gold_block"

    def getTexturFile(self):
        return "./assets/textures/items/gold_block.png"

handler.register(GoldBlock)
