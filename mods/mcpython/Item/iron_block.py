from .Item import *

class IronBlock(Item):
    def getName(self):
        return "minecraft:iron_block"

    def getTexturFile(self):
        return "./assets/textures/items/iron_block.png"

handler.register(IronBlock)
