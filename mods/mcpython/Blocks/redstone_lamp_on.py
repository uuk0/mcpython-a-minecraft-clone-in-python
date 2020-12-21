from .Block import *

FACES = [
    (0, 1, 0),
    (0, -1, 0),
    (-1, 0, 0),
    (1, 0, 0),
    (0, 0, 1),
    (0, 0, -1),
]


class redstone_lamp_on(Block):
    def getName(self):
        return "extra:redstone_lamp_on_private_instance"

    def getTex(self):
        return tex_coords((14, 10), (14, 10), (14, 10))

    def update(self, model, world):
        (x, y, z) = self.pos
        flag = False
        for (dx, dy, dz) in FACES:
            npos = (x + dx, y + dy, z + dz)
            if npos in model.world:
                if model.world[npos].redstone_level:
                    flag = True
        if not flag:
            model.add_block(self.pos, "minecraft:redstone_lamp")
            # print("[DEBUG] redstone lamp state change to low")

    def getItemName(self):
        return "minecraft:redstone_lamp"

    def getVisualName(self):
        return "minecraft:redstone_lamp"

    def redstoneStateUpdate(self, model, world):
        self.update(model, world)

    destroygroups = [destroyGroups.PIKAXE]


handler.register(redstone_lamp_on)
