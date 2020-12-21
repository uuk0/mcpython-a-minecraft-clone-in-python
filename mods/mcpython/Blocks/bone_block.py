from .Block import *
from . import wood_log


class BoneBlock(wood_log.WoodLog):
    def getName(self):
        return "minecraft:bone_block"

    def getTexturFront(self):
        return (13, 11)

    def getTexturSide(self):
        return (13, 12)

    def getTexturSideB(self):
        return (12, 15)

    def getBlastResistence(self):
        return 10

    def getHardness(self):
        return 2

    def getId(self):
        return 216


handler.register(BoneBlock)
