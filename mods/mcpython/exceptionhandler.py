import traceback
import globals as G
import time
import config
import sys


def addTraceback(printexc=True):
    if printexc:
        traceback.print_exc()
    f = open(G.local + "/exceptions.txt", mode="a")
    f.write(
        "\n["
        + str(time.time())
        + "] argv="
        + str(sys.argv)
        + ", platform="
        + str(sys.platform)
        + ", mcpythonversion="
        + str(config.CONFIGS["GAME_VERSION"])
        + ", gameid="
        + str(config.CONFIGS["VERSION_ID"])
        + " \ntraceback:\n"
    )
    traceback.print_exc(file=f)
    f.write("mods: " + str(G.modnames) + "\n")
    f.close()
