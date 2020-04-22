from .Item import *

class melon_block(Item):
    def getName(self):
        return "minecraft:melon_block"

    def getTexturFile(self):
        return "./assets/textures/items/melon_block.png"

handler.register(melon_block)
