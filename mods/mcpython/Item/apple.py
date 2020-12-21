from .Item import *


class Apple(Item):
    def getName(self):
        return "minecraft:apple"

    def getTexturFile(self):
        return "./assets/textures/items/apple.png"

    def hasBlock(self):
        return False

    def isEatAble(self):
        return True


handler.register(Apple)
