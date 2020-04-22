from .Block import *

class IronBlock(Block):
    def getTex(self):
        return tex_coords((9, 0), (9, 0), (9, 0))

    def getName(self):
        return "minecraft:iron_block"

    destroygroups = [destroyGroups.PIKAXE]

handler.register(IronBlock)
