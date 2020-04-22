from .Item import *

class StoneBrick(Item):
    def getName(self):
        return "minecraft:stone_brick"

    def getTexturFile(self):
        return "./assets/textures/items/stonebrick.png"

handler.register(StoneBrick)
