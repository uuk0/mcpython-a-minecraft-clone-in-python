from .Item import *

class BoneBlock(Item):
    def getName(self):
        return "minecraft:bone_block"

    def getTexturFile(self):
        return "./assets/textures/items/bone_block.png"

handler.register(BoneBlock)
