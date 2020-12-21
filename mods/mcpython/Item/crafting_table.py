from .Item import *


class crafting_table(Item):
    def getName(self):
        return "minecraft:crafting_table"

    def getTexturFile(self):
        return "./assets/textures/items/crafting_table.png"

    def getFuelAmount(self):
        return 20


handler.register(crafting_table)
