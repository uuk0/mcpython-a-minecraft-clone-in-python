import mods.mcpython.structures as structures
import globals as G

CONFIGS = {}


def convertOption(option_value):
    while option_value.startswith(" "):
        option_value = option_value[1:]
    if option_value == "True":
        option_value = True
    elif option_value == "False":
        option_value = False
    elif option_value.startswith("["):
        t = []
        for e in option_value[1:-1].split(","):
            t.append(e)
        option_value = []
        for e in t:
            option_value.append(convertOption(e))
        return option_value
    try:
        if option_value != True and option_value != False:
            option_value = int(option_value)
    except:
        try:
            option_value = float(option_value)
        except:
            pass
    return option_value


def loadConfig():
    f = open(G.local + "/config.txt")
    data = f.read()
    f.close()
    del f
    for e in data.split("\n"):
        if e != "":
            e.replace(" ", "", e.count(" "))
            option_name = e.split("=")[0][0:-1]
            option_value = convertOption(e.split("=")[1])
            CONFIGS[option_name] = option_value
    CONFIGS["init"] = {
        "GAME_STATES": [
            "game",
            "chat",
            "demo_info",
            "esc_menü",
            "start_menü",
            "loading",
            "inventory",
            "worldselect",
        ]
    }
    f = open(G.local + "/initscript.txt")
    data = f.read()[3:]
    f.close()
    exec(
        "from mods.mcpython.moduls import *\nclass keys:\n   FORWARD='forward:key'; BACKWARD='backward:key'; RIGHT='right:key';LEFT='left:key';JUMP='jump:key';escape='escape:key';toggleflying='togleflying:key';inventoryslots='inventoryslots:keys';openchat='openchat:key';openinventory='openinventory:key';MOVECAMERA='movecamera:key'\n"
        + data,
        CONFIGS["init"],
    )


loadConfig()
for e in CONFIGS["init"]["STRUCTURES"]:
    structures.Structure(e)
