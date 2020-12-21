from .Item import *


class redstone_block(Item):
    def getName(self):
        return "minecraft:redstone_block"

    def getTexturFile(self):
        return "./assets/textures/items/redstone_block.png"


handler.register(redstone_block)
