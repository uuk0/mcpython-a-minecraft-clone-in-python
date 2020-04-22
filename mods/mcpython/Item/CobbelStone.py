from .Item import *

class CobbelStone(Item):
    def getName(self):
        return "minecraft:cobblestone"

    def getTexturFile(self):
        return "./assets/textures/items/cobbelstone.png"

handler.register(CobbelStone)
