from .Item import *


class Bedrock(Item):
    def getName(self):
        return "minecraft:bedrock"

    def getTexturFile(self):
        return "./assets/textures/items/bedrock.png"


handler.register(Bedrock)
