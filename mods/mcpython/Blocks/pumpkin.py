from .Block import *


class Pumpkin(Block):
    def getTex(self):
        return tex_coords((2, 5), (2, 5), (3, 5))

    def getName(self):
        return "minecraft:pumpkin"

    destroygroups = [destroyGroups.AXE]


handler.register(Pumpkin)
