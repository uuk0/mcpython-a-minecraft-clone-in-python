from .Item import *


class chest(Item):
    def getName(self):
        return "minecraft:chest"

    def getTexturFile(self):
        return "./assets/textures/items/chest.png"

    def getFuelAmount(self):
        return 20


handler.register(chest)
