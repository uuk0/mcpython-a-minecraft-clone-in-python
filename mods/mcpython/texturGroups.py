from moduls import *
import globals as G


class handler:
    def __init__(self):
        self.files = []
        self.groups = {}

    def register(self, file, id=None, type=0):
        of = file
        file = G.local + file[1:]
        if id == None:
            id = of
        if not file in self.files:
            if type == 0:  # structur-file for block-rendering
                print("[texturhandler/INFO] adding textur file: " + file)
                self.files.append(file)
                self.groups[id] = TextureGroup(pyglet.image.load(file).get_texture())
            elif type == 1:  # image-file for sprites
                image = pyglet.image.load(file)
                self.files.append(file)
                self.groups[id] = image

    def getGroup(self, id):
        return self.groups[id]


handler = handler()
handler.register("./assets/textures/blocks/texture.png", id=0)
handler.register("./assets/textures/blocks/texture2.png", id=1)

handler.register("./assets/textures/blocks/texture.png", type=1)
handler.register("./assets/textures/blocks/texture2.png", type=1)

handler.register("./assets/textures/gui/chest.png", type=1)
handler.register("./assets/textures/gui/crafting_table.png", type=1)
handler.register("./assets/textures/gui/furnace.png", type=1)
handler.register("./assets/textures/gui/hotbar_image.png", type=1)
handler.register("./assets/textures/gui/inventory_clear.png", type=1)

for e in os.listdir(G.local + "/assets/textures/items"):
    if e.endswith(".png"):
        handler.register("./assets/textures/items/" + e, type=1)

handler.register("./assets/textures/gui/demomsg.png", type=1)
handler.register("./assets/textures/gui/optionbackground_A.png", type=1)
handler.register("./assets/textures/gui/optionbackground_F.png", type=1)
handler.register("./assets/textures/mob/player/char.png", type=1)
handler.register("./assets/textures/gui/options_background.png", type=1)
handler.register("./assets/textures/gui/startgui_singelplayer.png", type=1)
handler.register("./assets/textures/gui/startgui_quitgame.png", type=1)
handler.register("./assets/textures/gui/worldselect_creat_new.png", type=1)
handler.register("./assets/textures/gui/worldselect_cancel.png", type=1)

handler.register("./assets/textures/gui/icons/hart_full.png", type=1)
handler.register("./assets/textures/gui/icons/hart_half.png", type=1)
handler.register("./assets/textures/gui/icons/harts_no.png", type=1)

handler.register("./assets/textures/gui/mousetrigger.png", type=1)
