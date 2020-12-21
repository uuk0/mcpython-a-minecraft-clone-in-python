from .Item import *


class BakedPortato(Item):
    def getName(self):
        return "minecraft:baked_portato"

    def getTexturFile(self):
        return "./assets/textures/items/baked_portato.png"

    def hasBlock(self):
        return False

    def isEatAble(self):
        return True


handler.register(BakedPortato)
