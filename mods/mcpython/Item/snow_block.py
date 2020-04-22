from .Item import *
import globals as G

class SnowBlock(Item):
    def getName(self):
        return "minecraft:snow_block"

    def getTexturFile(self):
        return "./assets/textures/items/snow.png"

handler.register(SnowBlock)

class Snow(Item):
    def __init__(self):
        Item.__init__(self)
        self.block = None

    def getName(self):
        return "minecraft:snow"

    def getTexturFile(self):
        return "./assets/textures/items/snowball.png"

    def canInteractWith(self, block):
        if block.getName() == self.getName() and block.layer < 8 and G.player.gamemode != 2:
            self.block = block
            return True

    def interactWith(self, item):
        self.block.layer += 1
        if G.player.gamemode != 1:
            self.slot.amount -= 1
            if self.slot.amount == 0:
                self.slot.setItem(None)

handler.register(Snow)

