from moduls import *
import initgame
import chat


def start(window, creat=True):
    window.state = "StartMenü"
    window.model.world = {}
    window.set_exclusive_mouse(True)
    chat.window = window
    initgame.initgame(window, creat)
