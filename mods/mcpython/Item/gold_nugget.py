from .Item import *

class gold_nugget(Item):
    def getName(self):
        return "minecraft:gold_nugget"

    def getTexturFile(self):
        return "./assets/textures/items/gold_nugget.png"

    def hasBlock(self):
        return False

handler.register(gold_nugget)
