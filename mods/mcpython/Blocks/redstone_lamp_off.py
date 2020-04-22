from .Block import *

FACES = [
    ( 0, 1, 0),
    ( 0,-1, 0),
    (-1, 0, 0),
    ( 1, 0, 0),
    ( 0, 0, 1),
    ( 0, 0,-1),
]

class redstone_lamp_off(Block):
    def getName(self):
        return "minecraft:redstone_lamp"

    def getTex(self):
        return tex_coords((14, 9), (14, 9), (14, 9))

    def update(self, model, world):
        (x, y, z) = self.pos
        for (dx, dy, dz) in FACES:
            npos = (x + dx, y + dy, z + dz)
            if npos in model.world:
                if model.world[npos].redstone_level:
                    model.add_block(self.pos, "extra:redstone_lamp_on_private_instance")
                    #print("[DEBUG] redstone lamp state change to high")

    def redstoneStateUpdate(self, model, world):
        self.update(model, world)

    destroygroups = [destroyGroups.PIKAXE]

handler.register(redstone_lamp_off)
