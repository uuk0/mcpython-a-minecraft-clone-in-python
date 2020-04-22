from moduls import *
import IDGenerator

CREATIV_TAB_UPPER = "mcpython:creativ_tab:uppertype"
CREATIV_TAB_LOWER = "mcpython:creativ_tab:lowertype"

class CreativTab:
    class_id = IDGenerator.handler.getRandom()
    def __init__(self, x, y, iconfile, type=CREATIV_TAB_UPPER):
        self.x, self.y = x, y
        self.iconfile = iconfile
        self.type = type
        self.icon = None
        if type == CREATIV_TAB_UPPER:
            self.icon = pyglet.sprite.Sprite(
                                            pyglet.image.load("./texturs/gui/container/creative_inventory/creativ_tab_upper.png"))
        elif type == CREATIV_TAB_LOWER:
            self.icon = pyglet.sprite.Sprite(
                                            pyglet.image.load("./texturs/gui/container/creative_inventory/creativ_tab_lower.png"))
        else:
            raise IOError("can't find correct image for creativ-tab")
        self.icon.x = x
        self.icon.y = y
        self.icon2 = pyglet.sprite.Sprite(pyglet.image.load(iconfile))
        self.id = IDGenerator.handler.getRandom()

    def draw(self):
        self.icon.x = x
        self.icon.y = y
        self.icon2.x = x + 3
        self.icon2.y = y + 3
        self.icon.draw()
        self.icon2.draw()
