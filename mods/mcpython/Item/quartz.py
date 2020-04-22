from .Item import *

class Quartz(Item):
    def getName(self):
        return "minecraft:quartz"

    def getTexturFile(self):
        return "./assets/textures/items/quartz.png"

    def hasBlock(self):
        return False

handler.register(Quartz)
