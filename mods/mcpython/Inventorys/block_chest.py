from .Inventory import *
from oredictnames import *
import crafting


class chest(Inventory):
    def getId(self):
        return 6

    def getSlots(self):
        s = []
        pos = (
            [
                (197, 440),
                (239, 440),
                (281, 440),
                (323, 440),
                (365, 440),
                (407, 440),
                (449, 440),
                (491, 440),
                (533, 440),
            ]
            + [
                (197, 400),
                (239, 400),
                (281, 400),
                (323, 400),
                (365, 400),
                (407, 400),
                (449, 400),
                (491, 400),
                (533, 400),
            ]
            + [
                (197, 360),
                (239, 360),
                (281, 360),
                (323, 360),
                (365, 360),
                (407, 360),
                (449, 360),
                (491, 360),
                (533, 360),
            ]
            + [
                (197, 320),
                (239, 320),
                (281, 320),
                (323, 320),
                (365, 320),
                (407, 320),
                (449, 320),
                (491, 320),
                (533, 320),
            ]
            + [
                (197, 280),
                (239, 280),
                (281, 280),
                (323, 280),
                (365, 280),
                (407, 280),
                (449, 280),
                (491, 280),
                (533, 280),
            ]
            + [
                (197, 240),
                (239, 240),
                (281, 240),
                (323, 240),
                (365, 240),
                (407, 240),
                (449, 240),
                (491, 240),
                (533, 240),
            ]
        )
        for e in pos:
            s.append(Slot(*e))
        return s

    def getImage(self):
        return "./assets/textures/gui/chest.png"

    def getDepedens(self):
        return [0, 1]

    def getImagePos(self):
        return (180, 10)

    def getInventoryDependence(self):
        return [0, 1, 2, 3]


handler.register(chest)
