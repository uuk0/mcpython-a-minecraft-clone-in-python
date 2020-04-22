from .Item import *

class Wood_0_Slab(Item):
    def __init__(self):
        Item.__init__(self)
        self.block = None

    def getName(self):
        return "minecraft:wood_slab_0"

    def getTexturFile(self):
        return "./assets/textures/items/wood_slab_0.png"

    def canInteractWith(self, block):
        if block.getName() == "minecraft:wood_slab_0" and block.side != "A":
            self.block = block
            return True

    def interactWith(self, item):
        self.block.setNBT("side", "A")


handler.register(Wood_0_Slab)
