from .Item import *


class Lava(Item):
    def getName(self):
        return "minecraft:lava"

    def getTexturFile(self):
        return "./assets/textures/items/lava.png"


handler.register(Lava)
