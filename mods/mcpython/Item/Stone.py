from .Item import *


class Stone(Item):
    def getName(self):
        return "minecraft:stone"

    def getTexturFile(self):
        return "./assets/textures/items/stone.png"


handler.register(Stone)


class Diorit(Item):
    def getName(self):
        return "minecraft:diorit"

    def getTexturFile(self):
        return "./assets/textures/items/diorite.png"


handler.register(Diorit)


class PolishedDiorit(Item):
    def getName(self):
        return "minecraft:polished_diorit"

    def getTexturFile(self):
        return "./assets/textures/items/polished_diorit.png"


handler.register(PolishedDiorit)
