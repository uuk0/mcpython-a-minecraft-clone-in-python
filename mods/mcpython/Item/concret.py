from .Item import *

for id in range(0, 16):
    class Concret(Item):
        def getName(self):
            return "minecraft:concret_" + str(id)

        def getTexturFile(self):
            return "./assets/textures/items/concret_"+str(id)+".png"

    handler.register(Concret)

    class ConcretPowder(Item):
        def getName(self):
            return "minecraft:concret_powder_" + str(id)

        def getTexturFile(self):
            return "./assets/textures/items/concret_powder_"+str(id)+".png"

    handler.register(ConcretPowder)
