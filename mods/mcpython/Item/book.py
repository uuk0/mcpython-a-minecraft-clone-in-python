from .Item import *


class Book(Item):
    def getName(self):
        return "minecraft:book"

    def getTexturFile(self):
        return "./assets/textures/items/book.png"

    def hasBlock(self):
        return False


handler.register(Book)
