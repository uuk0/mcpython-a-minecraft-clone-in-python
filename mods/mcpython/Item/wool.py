from .Item import *

for i in range(0, 16):
    class Wool(Item):
        id = 0

        def getName(self):
            return "minecraft:wool_"+str(self.id)

        def getTexturFile(self):
            return "./assets/textures/items/WOOL#"+str(self.id)+".png"

        def getFuelAmount(self):
            return 10


    Wool.id = i
    handler.register(Wool)
