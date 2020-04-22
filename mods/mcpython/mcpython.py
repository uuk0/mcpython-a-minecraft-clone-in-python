from __future__ import division


try:
    import globals as G

    import sys

    G.local = sys.argv[1]
    print(G.local)

    from EventHandler import eventhandler

    import shortcuts

    from moduls import *

    from constans import *

    from chat import *

    import TickHandler

    import texturGroups

    import Item

#    from Block import *

    import WorldHandler

    import destroyGroup

    import crafting

    import entity

    import oredictnames

    import pyperclip

    print("[INFO] loading configs and structures")
    import config

    import GameStartup

    for e in config.CONFIGS["init"]["STRUCTURES"]:
        structures.Structur(e)

    #FIXME: wood_log nbt / sides are not correct

    print("[INFO] preconfigurate python differents")

    if sys.version_info[0] >= 3:
        xrange = range

    print("[INFO] loading moduls for secound boot")

    from mathhelper import *

    from Model import *

    from Window import *

    import WorldSaver

    print("[INFO] setting up java random")

    import javarandom

    G.random = javarandom.Random()

    print("[INFO] definiting config-functions for game-init")

    def setup_fog():
        """ Configure the OpenGL fog properties.

        """
        # Enable fog. Fog "blends a fog color with each rasterized pixel fragment's
        # post-texturing color."
        glEnable(GL_FOG)
        # Set the fog color.
        glFogfv(GL_FOG_COLOR, (GLfloat * 4)(0.5, 0.69, 1.0, 1))
        # Say we have no preference between rendering speed and quality.
        glHint(GL_FOG_HINT, GL_DONT_CARE)
        # Specify the equation used to compute the blending factor.
        glFogi(GL_FOG_MODE, GL_LINEAR)
        # How close and far away fog starts and ends. The closer the start and end,
        # the denser the fog in the fog range.
        glFogf(GL_FOG_START, 60.0)
        glFogf(GL_FOG_END, 80.0)


    def setup():
        """ Basic OpenGL configuration.

        """
        # Set the color of "clear", i.e. the sky, in rgba.
        glClearColor(0.5, 0.69, 1.0, 1)
        # Enable culling (not rendering) of back-facing facets -- facets that aren't
        # visible to you.
        glEnable(GL_CULL_FACE)
        # Set the texture minification/magnification function to GL_NEAREST (nearest
        # in Manhattan distance) to the specified texture coordinates. GL_NEAREST
        # "is generally faster than GL_LINEAR, but it can produce textured images
        # with sharper edges because the transition between texture elements is not
        # as smooth."
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        setup_fog()

    eventhandler.call("on_game_inited")

    while len(eventhandler.callfunctions) > 0:
        eventhandler.update()

    print("[INFO] starting game")

    window = Window(width=config.CONFIGS["DEFAULT_WINDOW_SIZE"][0], height=config.CONFIGS["DEFAULT_WINDOW_SIZE"][1], caption="mcpython version "+config.CONFIGS["GAME_VERSION"], resizable=True)
    chat.window = window
    G.window = window
    G.model = window.model
    G.player = window.player
    import chat
    chat.register()
    GameStartup.start(window, creat=False)

    invhandler.show(0)
    invhandler.hide(1)
    invhandler.window = window
except:
    import exceptionhandler
    exceptionhandler.addTraceback()

def run():
    try:
        G.window.set_menu("minecraft:start_menü")

        eventhandler.call("on_game_started")

        while len(eventhandler.callfunctions) > 0:
            eventhandler.update()

        pyglet.app.run()
    except:
        import exceptionhandler
        exceptionhandler.addTraceback()

def init(): pass