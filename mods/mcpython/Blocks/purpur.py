from .Block import *
from .wood_log import WoodLog


class purpur_block(Block):
    def getTex(self):
        return tex_coords((12, 10), (12, 10), (12, 10))

    def getName(self):
        return "minecraft:purpur_block"

    destroygroups = [destroyGroups.PIKAXE]

    def getBlastResistence(self):
        return 30

    def getHardness(self):
        return 1.5

    def getId(self):
        return 201

handler.register(purpur_block)

class purpur_pillar(WoodLog):
    def getName(self):
        return "minecraft:purpur_pillar"

    def getTexturFront(self):
        return (12, 7)

    def getTexturSide(self):
        return (12, 9)

    def getTexturSideB(self):
        return (12, 8)

    destroygroups = [destroyGroups.PIKAXE]

    def getBlastResistence(self):
        return 30

    def getHardness(self):
        return 1.5

    def getId(self):
        return 201

handler.register(purpur_pillar)
