from .Block import *


FACES = [
    ( 0, 1, 0),
    ( 0,-1, 0),
    (-1, 0, 0),
    ( 1, 0, 0),
    ( 0, 0, 1),
    ( 0, 0,-1),
]

class redstone_block(Block):
    def getName(self):
        return "minecraft:redstone_block"

    def getTex(self):
        return tex_coords((14, 8), (14, 8), (14, 8))

    def defaultRedstoneLevel(self):
        return True

    def update(self, model, world):
        if self.updated: return
        (x, y, z) = self.pos
        for (dx, dy, dz) in FACES:
            npos = (x + dx, y + dy, z + dz)
            if npos in model.world:
                model.world[npos].redstoneStateUpdate(model, world)
        self.updated = True

    def __init__(self, *args, **kwargs):
        Block.__init__(self,  *args, **kwargs)
        self.updated = False

    destroygroups = [destroyGroups.PIKAXE]

handler.register(redstone_block)
