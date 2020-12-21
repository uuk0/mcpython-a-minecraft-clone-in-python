from .Item import *
from oredictnames import *


class wood_plank_0(Item):
    def getName(self):
        return "minecraft:wood_plank_0"

    def getTexturFile(self):
        return "./assets/textures/items/plank.png"

    def getOreDictNames(self):
        return [OreDict.WOOD_PLANK]

    def getFuelAmount(self):
        return 20


handler.register(wood_plank_0)


class wood_plank_1(Item):
    def getName(self):
        return "minecraft:wood_plank_1"

    def getTexturFile(self):
        return "./assets/textures/items/plank_1.png"

    def getOreDictNames(self):
        return [OreDict.WOOD_PLANK]

    def getFuelAmount(self):
        return 20


handler.register(wood_plank_1)


class wood_plank_2(Item):
    def getName(self):
        return "minecraft:wood_plank_2"

    def getTexturFile(self):
        return "./assets/textures/items/plank_2.png"

    def getOreDictNames(self):
        return [OreDict.WOOD_PLANK]

    def getFuelAmount(self):
        return 20


handler.register(wood_plank_2)


class wood_plank_3(Item):
    def getName(self):
        return "minecraft:wood_plank_3"

    def getTexturFile(self):
        return "./assets/textures/items/plank_3.png"

    def getOreDictNames(self):
        return [OreDict.WOOD_PLANK]

    def getFuelAmount(self):
        return 20


handler.register(wood_plank_3)
