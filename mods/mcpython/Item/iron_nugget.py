from .Item import *


class iron_nugget(Item):
    def getName(self):
        return "minecraft:iron_nugget"

    def getTexturFile(self):
        return "./assets/textures/items/iron_nugget.png"

    def hasBlock(self):
        return False


handler.register(iron_nugget)
