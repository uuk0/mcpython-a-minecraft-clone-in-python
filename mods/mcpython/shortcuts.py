import EventHandler
import time
import pyglet
import globals as G

LAST_PRESS = []
LAST_PRESS_TIME = []

@EventHandler.eventhandler.event
def on_key_press(eventname, symbol, modifiers):
    LAST_PRESS.append([symbol, modifiers])
    LAST_PRESS_TIME.append(time.time())
    while time.time() - LAST_PRESS_TIME[0] > 5: #time in which button must be pressed
        LAST_PRESS_TIME.pop(0)
        LAST_PRESS.pop(0)

    if symbol == 65471 and (modifiers & 17): #screenshot
        store = "scrennshot_"+str(round(time.time()))+".png"
        pyglet.image.get_buffer_manager().get_color_buffer().save(G.local+"/screenshots/"+store)
        print("screenshot saved as "+store)

    if (symbol == 97 and (modifiers & 17) and [65472, 17] in LAST_PRESS) or \
            (symbol == 65472 and (modifiers & 17) and [97, 17] in LAST_PRESS):
        print("reloading chunks...")
        for c in G.model.shown_sectors:
            G.model.hide_sector(c)
        G.model.change_sectors(None, G.window.sector)

    if (symbol == pyglet.window.key.N and (modifiers & 17) and [65472, 17] in LAST_PRESS) or \
            (symbol == 65472 and (modifiers & 17) and [pyglet.window.key.N, 17] in LAST_PRESS):
        if G.player.gamemode == 1:
            G.player.gamemode = 3
            print("[CHAT] changed your gamemode")
        elif G.player.gamemode == 3:
            G.player.gamemode = 1
            print("[CHAT] changed your gamemode")
        else:
            print("[CHAT] can't change gamemode because gamemode is not 1 or 3")



