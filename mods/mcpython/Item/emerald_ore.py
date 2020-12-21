from .Item import *


class Bedrock(Item):
    def getName(self):
        return "minecraft:emerald_ore"

    def getTexturFile(self):
        return "./assets/textures/items/emerald_ore.png"


handler.register(Bedrock)
