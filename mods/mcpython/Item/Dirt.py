from .Item import *


class Dirt(Item):
    def getName(self):
        return "minecraft:dirt"

    def getTexturFile(self):
        return "./assets/textures/items/dirt.png"


handler.register(Dirt)
