from .Item import *
from oredictnames import OreDict


class Dye0(Item):
    def getName(self):
        return "minecraft:ash"

    def getTexturFile(self):
        return "./assets/textures/items/ash.png"

    def hasBlock(self):
        return False

    def getOreDictNames(self):
        return [OreDict.DYE, OreDict.WHITE_DYE]

handler.register(Dye0)


class Dye1(Item):
    def getName(self):
        return "minecraft:bone_meel"

    def getTexturFile(self):
        return "./assets/textures/items/bonemeel.png"

    def hasBlock(self):
        return False

    def getOreDictNames(self):
        return [OreDict.DYE, OreDict.WHITE_DYE]

handler.register(Dye1)

class Dye2(Item):
    def getName(self):
        return "minecraft:brown_dye"

    def getTexturFile(self):
        return "./assets/textures/items/brown_dye.png"

    def hasBlock(self):
        return False

    def getOreDictNames(self):
        return [OreDict.DYE, OreDict.BROWN_DYE]

handler.register(Dye2)

class Dye3(Item):
    def getName(self):
        return "minecraft:green_dye"

    def getTexturFile(self):
        return "./assets/textures/items/green_dye.png"

    def hasBlock(self):
        return False

    def getOreDictNames(self):
        return [OreDict.DYE, OreDict.GREEN_DYE]

handler.register(Dye3)

class Dye4(Item):
    def getName(self):
        return "minecraft:grey_dye"

    def getTexturFile(self):
        return "./assets/textures/items/grey_dye.png"

    def hasBlock(self):
        return False

    def getOreDictNames(self):
        return [OreDict.DYE, OreDict.GREY_DYE]

handler.register(Dye4)

class Dye5(Item):
    def getName(self):
        return "minecraft:ink_sack"

    def getTexturFile(self):
        return "./assets/textures/items/ink_sack.png"

    def hasBlock(self):
        return False

    def getOreDictNames(self):
        return [OreDict.DYE, OreDict.BLACK_DYE]

handler.register(Dye5)

class Dye6(Item):
    def getName(self):
        return "minecraft:lapis"

    def getTexturFile(self):
        return "./assets/textures/items/lapis.png"

    def hasBlock(self):
        return False

    def getOreDictNames(self):
        return [OreDict.DYE, OreDict.BLUE_DYE]

handler.register(Dye6)

class Dye7(Item):
    def getName(self):
        return "minecraft:light_blue_dye"

    def getTexturFile(self):
        return "./assets/textures/items/light_blue_dye.png"

    def hasBlock(self):
        return False

    def getOreDictNames(self):
        return [OreDict.DYE, OreDict.LIGHT_BLUE_DYE]

handler.register(Dye7)

class Dye8(Item):
    def getName(self):
        return "minecraft:light_green_dye"

    def getTexturFile(self):
        return "./assets/textures/items/light_green_dye.png"

    def hasBlock(self):
        return False

    def getOreDictNames(self):
        return [OreDict.DYE, OreDict.LIGHT_GREEN_DYE]

handler.register(Dye8)

class Dye9(Item):
    def getName(self):
        return "minecraft:light_light_blue_dye"

    def getTexturFile(self):
        return "./assets/textures/items/light_light_blue_dye.png"

    def hasBlock(self):
        return False

    def getOreDictNames(self):
        return [OreDict.DYE, OreDict.LIGHT_LIGHT_BLUE_DYE]

handler.register(Dye9)

class Dye10(Item):
    def getName(self):
        return "minecraft:magenta_dye"

    def getTexturFile(self):
        return "./assets/textures/items/magenta_dye.png"

    def hasBlock(self):
        return False

    def getOreDictNames(self):
        return [OreDict.DYE, OreDict.MAGENTA_DYE]

handler.register(Dye10)

class Dye11(Item):
    def getName(self):
        return "minecraft:orange_dye"

    def getTexturFile(self):
        return "./assets/textures/items/orange_dye.png"

    def hasBlock(self):
        return False

    def getOreDictNames(self):
        return [OreDict.DYE, OreDict.ORANGE_DYE]

handler.register(Dye11)

class Dye12(Item):
    def getName(self):
        return "minecraft:pink_dye"

    def getTexturFile(self):
        return "./assets/textures/items/pink_dye.png"

    def hasBlock(self):
        return False

    def getOreDictNames(self):
        return [OreDict.DYE, OreDict.PINK_DYE]

handler.register(Dye12)

class Dye13(Item):
    def getName(self):
        return "minecraft:purpel_dye"

    def getTexturFile(self):
        return "./assets/textures/items/purpel_dye.png"

    def hasBlock(self):
        return False

    def getOreDictNames(self):
        return [OreDict.DYE, OreDict.PURPEL_DYE]

handler.register(Dye13)

class Dye14(Item):
    def getName(self):
        return "minecraft:red_dye"

    def getTexturFile(self):
        return "./assets/textures/items/red_dye.png"

    def hasBlock(self):
        return False

    def getOreDictNames(self):
        return [OreDict.DYE, OreDict.RED_DYE]

handler.register(Dye14)

class Dye15(Item):
    def getName(self):
        return "minecraft:yellow_dye"

    def getTexturFile(self):
        return "./assets/textures/items/yellow_dye.png"

    def hasBlock(self):
        return False

    def getOreDictNames(self):
        return [OreDict.DYE, OreDict.YELLOW_DYE]

handler.register(Dye15)

DYES = [Dye0, Dye1, Dye2, Dye3, Dye4, Dye5, Dye6, Dye7, Dye8, Dye9, Dye10, Dye11, Dye12, Dye13, Dye14, Dye15]