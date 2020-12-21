from .Item import *


class furnes(Item):
    def getName(self):
        return "minecraft:furnes"

    def getTexturFile(self):
        return "./assets/textures/items/furnace.png"


handler.register(furnes)
