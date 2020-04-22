from .Item import *

class redstone_lamp(Item):
    def getName(self):
        return "minecraft:redstone_lamp"

    def getTexturFile(self):
        return "./assets/textures/items/redstone_lamp.png"

handler.register(redstone_lamp)
