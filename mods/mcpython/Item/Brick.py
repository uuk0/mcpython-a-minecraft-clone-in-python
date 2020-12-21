from .Item import *


class Brick(Item):
    def getName(self):
        return "minecraft:brick"

    def getTexturFile(self):
        return "./assets/textures/items/brick.png"


handler.register(Brick)
