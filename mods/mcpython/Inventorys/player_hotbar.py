from .Inventory import *

import globals as G
import EventHandler

class hotbar(Inventory):
    def __init__(self):
        Inventory.__init__(self)
        EventHandler.eventhandler.on_event("on_draw_2D", self.draw)

    def getSlots(self):
        y = 27
        return [Slot(197, y), Slot(239, y), Slot(281, y), Slot(323, y), Slot(365, y),
                             Slot(407, y), Slot(449, y), Slot(491, y), Slot(533, y)]
    
    def getImage(self):
        return './assets/textures/gui/hotbar_image.png'

    def getImagePos(self):
        return (180, 10)

    def mouseOut(self):
        return False

    def drawBefore(self):
        return [1, 2]

    def getId(self):
        return 1

handler.register(hotbar)