import sys
import os
import time
import pickle
import traceback
import importlib
import globals as G
import gameinfoloader

gameinfoloader.loadData()

VERSION = "0.0.2"
COMPATIBLE = [VERSION]

"""version history:
0.0.1: added system
0.0.2: added name and version to mod-class
       added pre-loader (import)
       added data attribute to mod-class"""


class Mod:
    def __init__(
        self,
        dir,
        name,
        version,
        mcversion,
        mlversion,
        dependence,
        pre_init,
        post_init,
        data,
    ):
        self.dir = dir
        self.name = name
        self.version = version
        self.mcversion = mcversion
        self.mlversion = mlversion
        self.dependence = dependence
        self.pre_init_mods = pre_init
        self.post_init_mods = post_init
        self.data = data
        self.module = None

    def preload(self):
        try:
            sys.path.append(self.dir)
            self.module = importlib.import_module(self.data["MAIN_FILE"])
        except:
            traceback.print_exc()
            raise

    def init(self):
        self.module.init()

    def run(self):
        self.module.run()


def creatdModInst(dir):
    with open(dir + "/mcmod.info", mode="rb") as f:
        data = pickle.load(f)
    return Mod(
        dir,
        data["name"],
        data["MCPYTHON_VERSION"],
        data["MODLOADER_VERSION"],
        data["DEPENDENCE"] if "DEPENDENCE" in data else [],
        data["INIT_BEFORE"] if "INIT_BEFORE" in data else [],
        data["INIT_AFTER"] if "INIT_AFTER" in data else [],
        None,
        data,
    )


def printErrors(errors):
    if len(errors) == 0:
        return
    # 0:has no mcmod.info file, 1: Has the same name, 2: missing mod for dependence, 3: syntax error
    print(
        "SYSTEM IS NOT WORKING BECAUSE THE FOLLOWING ERRORS OCCUERS DURING LOADING THEM"
    )
    for modname in errors.keys():
        error = errors[modname]
        if len(error) > 0:
            print("Mod", modname, "is not working because:")
            for e in error:
                try:
                    if e[0] == 0:
                        print(" -it has no mcmod.info file")
                    elif e[0] == 1:
                        print(" -it has the same name as", e[1])
                    elif e[0] == 2:
                        print(" -is missing the following mod:", *e[1:])
                    elif e[0] == 3:
                        print(" -", *e[1:])
                except:
                    pass


def load(dir):
    localdir = dir
    print("[MODLOADER/INFO] modloader version", VERSION, "for mcpython")
    print("[MODLOADER/INFO] searching ./mods for compatible mods")
    items = os.listdir(localdir + "/mods")
    pmoddirs = []
    for e in items:
        if os.path.isdir(localdir + "/mods/" + e):
            pmoddirs.append(e)
    if len(pmoddirs) == 0:
        print("[MODLOADER/INFO] found nothing")
        return
    print(
        "[MODLOADER/INFO] found",
        len(pmoddirs),
        "possible mod-dir(s). Analysing",
        "them..." if len(pmoddirs) > 1 else "it...",
    )
    moddirs = []
    errors = {}
    for e in pmoddirs:
        errors[e] = []
        if os.path.isfile(localdir + "/mods/" + e + "/mcmod.info"):
            moddirs.append(e)
        else:
            errors[e].append(0)
    print(
        "[MODLOADER/INFO] found",
        len(moddirs),
        "mod(s).",
        "Starting loading" if len(moddirs) > 0 else "",
        "them..." if len(moddirs) > 1 else ("it..." if len(moddirs) > 0 else ""),
    )
    mods = {}
    for e in moddirs:
        print("[MODLOADER/INFO] initialisating mod", e)
        mod = creatdModInst(localdir + "mods/" + e)
        if mod.name in mods.keys():
            errors[mod.name].append([1, mods[mod.name]])
            mods[mod.name].append(mod)
        else:
            mods[mod.name] = [mod]

    print("[MODLOADER/INFO] initilisation finished")
    if len(mods) == 0:
        printErrors(errors)
        return
    rmods = {}
    rmodnames = []
    for name in mods.keys():
        for mod in mods[name]:
            rmodnames.append(mod.name)
            rmods[mod.name] = mod
    print("[MODLOADER/INFO] looking for dependence exceptions...")
    for name in mods.keys():
        for mod in mods[name]:
            error = []
            for dmod in mod.dependence:
                if type(dmod) == str:
                    if not dmod in rmodnames:
                        error.append([2, mod, dmod])
                elif type(dmod) == list:
                    if len(dmod) == 2:  # name, minversion
                        if (not dmod[0] in rmodnames) or (
                            rmods[dmod[0]].version < dmod[1]
                        ):
                            error.append([2, mod, dmod])
                    elif len(dmod) == 3:  # name, minversion, maxversion
                        if (not dmod[0] in rmodnames) or (
                            rmods[dmod[0]].version < dmod[1]
                            or rmods[dmod[0]].version > dmod[2]
                        ):
                            error.append([2, mod, dmod])
                    else:
                        error.append(
                            [3, mod, "these mod has an unknown dependency:", dmod]
                        )
            if not mod.name in errors.keys():
                errors[mod.name] = []
            errors[mod.name] += error
    print("[MODLOADER/INFO] resoloving init-dependences...")
    call_list = []
    for name in mods.keys():
        for mod in mods[name]:
            if mod.pre_init_mods == []:
                if mod.name == "moduls":
                    call_list.insert(0, mod)
                elif mod.name == "mcpython":
                    if len(call_list) == 0 or call_list[0].name != "moduls":
                        call_list.insert(0, mod)
                    else:
                        call_list.insert(1, mod)
                else:
                    call_list.append(mod)
            else:
                raise ValueError("this is not supported!!!")
    G.mods = call_list
    for e in call_list:
        G.modnames.append(e.name)
    print("[MODLOADER/INFO] pre-loading mods...")
    for e in call_list:
        e.preload()
    print("[MODLOADER/INFO] initing mods...")
    # print(call_list)
    for e in call_list:
        e.init()
    print("[MODLOADER/INFO] running main files...")
    mods["mcpython"][0].run()
