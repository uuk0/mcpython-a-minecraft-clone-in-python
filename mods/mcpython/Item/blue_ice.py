from .Item import *


class BlueIce(Item):
    def getName(self):
        return "minecraft:blue_ice"

    def getTexturFile(self):
        return "./assets/textures/items/blue_ice.png"


handler.register(BlueIce)


class Ice(Item):
    def getName(self):
        return "minecraft:ice"

    def getTexturFile(self):
        return "./assets/textures/items/ICE.png"


handler.register(Ice)


class PackedIce(Item):
    def getName(self):
        return "minecraft:packed_ice"

    def getTexturFile(self):
        return "./assets/textures/items/PACKED_ICE.png"


handler.register(PackedIce)
