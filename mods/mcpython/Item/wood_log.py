from .Item import *
from oredictnames import *


class Wood_Log_0(Item):
    def getName(self):
        return "minecraft:wood_log_0"

    def getTexturFile(self):
        return "./assets/textures/items/log.png"

    def getOreDictNames(self):
        return [OreDict.WOOD_LOG, OreDict.AcaciaLogs]

    def getFuelAmount(self):
        return 20


handler.register(Wood_Log_0)


class Wood_Log_1(Item):
    def getName(self):
        return "minecraft:wood_log_1"

    def getTexturFile(self):
        return "./assets/textures/items/log_1.png"

    def getOreDictNames(self):
        return [OreDict.WOOD_LOG, OreDict.BirchLogs]

    def getFuelAmount(self):
        return 20


handler.register(Wood_Log_1)


class Wood_Log_2(Item):
    def getName(self):
        return "minecraft:wood_log_2"

    def getTexturFile(self):
        return "./assets/textures/items/log_2.png"

    def getOreDictNames(self):
        return [OreDict.WOOD_LOG, OreDict.DarkOakLogs]

    def getFuelAmount(self):
        return 20


handler.register(Wood_Log_2)


class Wood_Log_3(Item):
    def getName(self):
        return "minecraft:wood_log_3"

    def getTexturFile(self):
        return "./assets/textures/items/log_3.png"

    def getOreDictNames(self):
        return [OreDict.WOOD_LOG, OreDict.JungleLogs]

    def getFuelAmount(self):
        return 20


handler.register(Wood_Log_3)


class Wood_Log_4(Item):
    def getName(self):
        return "minecraft:wood_log_4"

    def getTexturFile(self):
        return "./assets/textures/items/log_4.png"

    def getOreDictNames(self):
        return [OreDict.WOOD_LOG, OreDict.OakLogs]

    def getFuelAmount(self):
        return 20


handler.register(Wood_Log_4)
