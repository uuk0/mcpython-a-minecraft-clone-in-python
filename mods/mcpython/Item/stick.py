from .Item import *

class Stick(Item):
    def getName(self):
        return "minecraft:stick"

    def getTexturFile(self):
        return "./assets/textures/items/stick.png"

    def hasBlock(self):
        return False

    def getFuelAmount(self):
        return 20

handler.register(Stick)
