from .Item import *

class Bone(Item):
    def getName(self):
        return "minecraft:bone"

    def getTexturFile(self):
        return "./assets/textures/items/bone.png"

handler.register(Bone)
