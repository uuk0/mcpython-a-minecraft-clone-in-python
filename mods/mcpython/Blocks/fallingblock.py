from .Block import *
from TickHandler import handler as tickhandler
import globals as G


class FallingBlock(Block):
    def update(self, model, window):
        if not (x, y - 1, z) in model.world:
            tickhandler.run(self.reupdate, 1, args=[model, window])

    def reupdate(self, model, window):
        (x, y, z) = self.pos
        if not (x, y - 1, z) in model.world:
            if model.move_block(self.pos, (x, y - 1, z), immediate=False) != False:
                model.updateNexts((x, y, z))
                model.updateNexts((x, y - 1, z))
        elif not model.world[(x, y - 1, z)].isFullBlock():
            G.player.addToFreePlace(self.getDropBlock())

    def getDropBlock(self):
        return self.getDrop(None)
