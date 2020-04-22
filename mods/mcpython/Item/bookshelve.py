from .Item import *

class Bookshelve(Item):
    def getName(self):
        return "minecraft:bookshelve"

    def getTexturFile(self):
        return "./assets/textures/items/bookshelve.png"

handler.register(Bookshelve)
