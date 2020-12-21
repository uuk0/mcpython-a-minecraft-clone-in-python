from .Block import *
import random
import TickHandler

FACES = [
    (0, 1, 0),
    (-1, 0, 0),
    (1, 0, 0),
    (0, 0, 1),
    (0, 0, -1),
]


class Cactus(Block):
    def getTex(self):
        return tex_coords((7, 5), (7, 3), (7, 4))

    def getName(self):
        return "minecraft:cactus"

    def update(self, model, window):
        (x, y, z) = self.pos
        for dx, dy, dz in FACES:
            key = (x + dx, y + dy, z + dz)
            if key in model.world:
                window.player.addToFreePlace(
                    self.getItemName(), amount=self.getDropAmount(None)
                )
                try:
                    model.remove_block((x, y, z))
                except:
                    pass
                return
        if (x, y - 1, z) in model.world and model.world[
            (x, y - 1, z)
        ].getName() == "minecraft:cactus":
            model.world[(x, y - 1, z)].update(model, window)
            self.high = model.world[(x, y - 1, z)].high + 1
            if self.high < 4:
                TickHandler.handler.run(
                    model.add_block,
                    random.randint(1, 1),
                    args=[(x, y + 1, z), "minecraft:cactus"],
                )
        elif (x, y - 1, z) in model.world and model.world[
            (x, y - 1, z)
        ].getName() != "minecraft:sand":
            window.player.addToFreePlace(
                self.getItemName(), amount=self.getDropAmount(None)
            )
            try:
                model.remove_block((x, y, z))
            except:
                pass
            return

    def on_creat(self):
        self.high = 0

    def getPlayerDamage(self):
        return 1

    def getBlastResistence(self):
        return 2

    def getHardness(self):
        return 0.4

    def getId(self):
        return 81


handler.register(Cactus)
