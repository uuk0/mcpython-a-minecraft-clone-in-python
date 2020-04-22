from .Item import *

class Barrier(Item):
    def getName(self):
        return "minecraft:barrier"

    def getTexturFile(self):
        return "./assets/textures/items/barrier.png"

handler.register(Barrier)
