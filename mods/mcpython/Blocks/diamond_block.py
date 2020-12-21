from .Block import *


class DiamondBlock(Block):
    def getTex(self):
        return tex_coords((7, 0), (7, 0), (7, 0))

    def getName(self):
        return "minecraft:diamond_block"

    destroygroups = [destroyGroups.PIKAXE]


handler.register(DiamondBlock)
