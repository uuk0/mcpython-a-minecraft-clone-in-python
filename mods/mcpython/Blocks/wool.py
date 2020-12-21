from .Block import *

for i in range(0, 16):

    class Wool(Block):
        id = 0

        def getTex(self):
            return tex_coords((15, self.id), (15, self.id), (15, self.id))

        def getName(self):
            return "minecraft:wool_" + str(15 - self.id)

        destroygroups = [destroyGroups.SHEER]

        def getBlastResistence(self):
            return 4

        def getHardness(self):
            return 0.8

        def getId(self):
            return 35

    Wool.id = i
    handler.register(Wool)
