from .Block import *
from .fallingblock import FallingBlock


for id in range(0, 16):
    class Concret(Block):
        def getTexturFile(self):
            return 1

        def getTex(self):
            return tex_coords((0, id), (0, id), (0, id))

        def getName(self):
            return "minecraft:concret_"+str(id)

        destroygroups = [destroyGroups.PIKAXE]

    handler.register(Concret)


    class ConcretPowder(FallingBlock):
        def getTexturFile(self):
            return 1

        def getTex(self):
            return tex_coords((1, id), (1, id), (1, id))

        def getName(self):
            return "minecraft:concret_powder_" + str(id)

        destroygroups = [destroyGroups.SHOVEL]


    handler.register(ConcretPowder)
