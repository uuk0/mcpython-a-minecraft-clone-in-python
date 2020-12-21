from .Item import *


class Endstone(Item):
    def getName(self):
        return "minecraft:endstone"

    def getTexturFile(self):
        return "./assets/textures/items/end_stone.png"


handler.register(Endstone)


class Endbrick(Item):
    def getName(self):
        return "minecraft:endbrick"

    def getTexturFile(self):
        return "./assets/textures/items/end_brick.png"


handler.register(Endbrick)
