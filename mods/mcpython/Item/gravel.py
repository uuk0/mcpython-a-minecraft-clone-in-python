from .Item import *


class Gravel(Item):
    def getName(self):
        return "minecraft:gravel"

    def getTexturFile(self):
        return "./assets/textures/items/gravel.png"


handler.register(Gravel)
