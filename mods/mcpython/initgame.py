from WorldHandler import *
from moduls import *
from constans import *
from config import CONFIGS


def initgame(window, creat=True):
    # configurate opengl
    glClearColor(0.5, 0.69, 1.0, 1)
    glEnable(GL_CULL_FACE)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glEnable(GL_FOG)
    glFogfv(GL_FOG_COLOR, (GLfloat * 4)(0.5, 0.69, 1.0, 1))
    glHint(GL_FOG_HINT, GL_DONT_CARE)
    glFogi(GL_FOG_MODE, GL_LINEAR)
    glFogf(GL_FOG_START, 20.0)
    glFogf(GL_FOG_END, 60.0)
    if creat:
        window.set_menu("start_menü")
        y = 0
        while (0, y, 0) in window.model.world:
            y += 1
        window.position = window.startpos = (0, y + 1, 0)
        print("[INFO] finsih!")
