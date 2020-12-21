from .Item import *


class leave_0(Item):
    def getName(self):
        return "minecraft:leave_0"

    def getTexturFile(self):
        return "./assets/textures/items/leaves_0.png"

    def getFuelAmount(self):
        return 10


handler.register(leave_0)
