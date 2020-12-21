from .Item import *


class purpur_block(Item):
    def getName(self):
        return "minecraft:purpur_block"

    def getTexturFile(self):
        return "./assets/textures/items/purpur_block.png"


handler.register(purpur_block)


class purpur_pillar(Item):
    def getName(self):
        return "minecraft:purpur_pillar"

    def getTexturFile(self):
        return "./assets/textures/items/purpur_pillar.png"


handler.register(purpur_pillar)
