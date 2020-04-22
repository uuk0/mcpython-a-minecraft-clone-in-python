from .Block import *

class GoldBlock(Block):
    def getTex(self):
        return tex_coords((7, 1), (7, 1), (7, 1))

    def getName(self):
        return "minecraft:gold_block"

    destroygroups = [destroyGroups.PIKAXE]

handler.register(GoldBlock)
