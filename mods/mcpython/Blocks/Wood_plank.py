from .Block import *


class Plank(Block):
    def getBlastResistence(self):
        # todo add constant
        return -1

    def getHardness(self):
        return 2

    def getId(self):
        return 5


class wood_plank_0(Plank):
    def getName(self):
        return "minecraft:wood_plank_0"

    def getTex(self):
        return tex_coords((0, 7), (0, 7), (0, 7))

    def getDestroyGroups(self):
        return [destroyGroups.AXE]


handler.register(wood_plank_0)


class wood_plank_1(Plank):
    def getName(self):
        return "minecraft:wood_plank_1"

    def getTex(self):
        return tex_coords((1, 7), (1, 7), (1, 7))

    def getDestroyGroups(self):
        return [destroyGroups.AXE]


handler.register(wood_plank_1)


class wood_plank_2(Plank):
    def getName(self):
        return "minecraft:wood_plank_2"

    def getTex(self):
        return tex_coords((2, 7), (2, 7), (2, 7))

    def getDestroyGroups(self):
        return [destroyGroups.AXE]


handler.register(wood_plank_2)


class wood_plank_3(Plank):
    def getName(self):
        return "minecraft:wood_plank_3"

    def getTex(self):
        return tex_coords((3, 7), (3, 7), (3, 7))

    def getDestroyGroups(self):
        return [destroyGroups.AXE]


handler.register(wood_plank_3)
