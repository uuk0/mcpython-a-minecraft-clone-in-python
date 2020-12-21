from .Item import *


class Leather(Item):
    def getName(self):
        return "minecraft:leather"

    def getTexturFile(self):
        return "./assets/textures/items/leather.png"


handler.register(Leather)
