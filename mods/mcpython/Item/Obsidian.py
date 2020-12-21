from .Item import *


class Obsidian(Item):
    def getName(self):
        return "minecraft:obsidian"

    def getTexturFile(self):
        return "./assers/textures/items/obsidian.png"


handler.register(Obsidian)
