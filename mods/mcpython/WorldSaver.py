import pickle
import os
import shutil
import time
import Inventorys
import chat
import config
from EventHandler import eventhandler
import globals as G

SAVE_VERSION = "0.2.2"
COMPATIBLE = [SAVE_VERSION]


def loadWorld(model, name):
    if not os.path.isdir("./saves/" + name):
        print("[ERROR] no save found named " + name)
        return
    f = open("./saves/" + name + "/world.dat", mode="rb")
    worlddata = pickle.load(f)
    f.close()
    if not worlddata[0] in COMPATIBLE or worlddata[1] > config.CONFIGS["VERSION_ID"]:
        return
    cleanUpModel(model)
    f = open("./saves/" + name + "/player.dat", mode="rb")
    playerdata = pickle.load(f)
    f.close()
    model.window.player.mode = playerdata[0]
    model.window.player.gamemode = playerdata[1]
    model.window.player.harts = playerdata[2]
    model.window.player.xp = playerdata[3]
    model.window.player.hunger = playerdata[4]
    model.window.hotbarelement = playerdata[5]
    model.window.demostarttime = time.time() - playerdata[6]
    model.window.position = playerdata[7]
    model.window.rotation = playerdata[8]

    f = open("./saves/" + name + "/level.dat", mode="rb")
    leveldata = pickle.load(f)
    f.close()
    model.window.world.chunkdata = leveldata
    for e in leveldata:
        pos = e[0]
        lenght = e[1]
        id = e[2]
        print("[WORLDLOADER/INFO] loading chunk ", pos, lenght, id)
        f = open("./saves/" + name + "/sectors/sector_" + str(id) + ".chunk", mode="rb")
        blocklist = pickle.load(f)
        f.close()
        for e in blocklist.keys():
            e = [e] + blocklist[e]
            model.add_block(e[0], e[1], save=False, immediate=False)
            block = model.world[e[0]]
            block.setAllNBT(e[2])
            block.redstone_level = e[3]
            block.setStoreData(e[4])
    f = open("./saves/" + name + "/inventory.dat", mode="rb")
    invdata = pickle.load(f)
    f.close()
    if (
        worlddata[0] != SAVE_VERSION or worlddata[1] != config.CONFIGS["GAME_VERSION"]
    ):  #
        saveWorld(model, name)


def saveWorld(model, name):
    if not name:
        return
    if not os.path.isdir("./saves/" + name):
        os.makedirs("./saves/" + name)
    playerdata = [
        model.window.player.mode,
        model.window.player.gamemode,
        model.window.player.harts,
        model.window.player.xp,
        model.window.player.hunger,
        model.window.hotbarelement,
        time.time() - model.window.demostarttime,
        model.window.position,
        model.window.rotation,
    ]
    f = open("./saves/" + name + "/player.dat", mode="wb")
    pickle.dump(playerdata, f)
    f.close()
    sectors = model.sectors.keys()
    sectordata = []
    sid = 0
    if not os.path.isdir("./saves/" + name + "/sectors/"):
        os.makedirs("./saves/" + name + "/sectors/")
    for e in sectors:
        sectordata.append([e, len(model.sectors[e]), sid])
        sid += 1
        blocklist = {}
        for pos in model.sectors[e]:
            block = model.world[pos]
            blocklist[pos] = [
                block.getName(),
                block.getAllNBT(),
                block.redstone_level,
                block.getStoreData(),
            ]
        f = open(
            "./saves/" + name + "/sectors/sector_" + str(sid - 1) + ".chunk", mode="wb"
        )
        pickle.dump(blocklist, f)
        f.close()
    model.window.world.chunkdata = sectordata
    f = open("./saves/" + name + "/level.dat", mode="wb")
    pickle.dump(sectordata, f)
    f.close()
    inventorydata = []
    for inst in Inventorys.handler.inventoryinst.values():
        linvdata = [inst.id, None if not inst.block else inst.block.pos]
        for e in inst.slots:
            linvdata.append(
                [
                    None if not e.item else e.item.getName(),
                    None if not e.item else e.amount,
                    None if not e.item else e.item.getStoreData(),
                ]
            )
        inventorydata.append(linvdata)
    f = open("./saves/" + name + "/inventory.dat", mode="wb")
    pickle.dump(inventorydata, f)
    f.close()
    entitydata = []
    for entity in model.entitys:
        entitydata.append([entity.position])
        for e in entity.getBoxModels():
            entitydata[-1].append([e.position, e.rotation])
    f = open("./saves/" + name + "/entity.dat", mode="wb")
    pickle.dump(entitydata, f)
    f.close()
    f = open("./saves/" + name + "/world.dat", mode="wb")
    pickle.dump(
        [SAVE_VERSION, config.CONFIGS["GAME_VERSION"], config.CONFIGS["VERSION_ID"]], f
    )
    f.close()


def savePlayerData(name, window):
    if not name:
        return
    if not os.path.isfile("./saves/" + name + "/player.dat"):
        return
    model = window.model
    playerdata = [
        model.window.player.mode,
        model.window.player.gamemode,
        model.window.player.harts,
        model.window.player.xp,
        model.window.player.hunger,
        model.window.hotbarelement,
        time.time() - model.window.demostarttime,
        model.window.position,
        model.window.rotation,
    ]
    f = open("./saves/" + name + "/player.dat", mode="wb")
    pickle.dump(playerdata, f)
    f.close()


def saveCommandToTMP(worldname, commands):
    raise ValueError()


def saveToChunk(chunk, name, command):
    for e in G.window.world.chunkdata:
        if e[0] == chunk:
            id = e[2]
            f = open(
                "./saves/" + name + "/sectors/sector_" + str(id) + ".chunk", mode="rb"
            )
            cdata = pickle.load(f)
            f.close()
            if command[0] == 0:
                block = G.model.world[command[1]]
                cdata[command[1]] = [
                    block.getName(),
                    block.getAllNBT(),
                    block.redstone_level,
                    block.getStoreData(),
                ]
            elif command[0] == 2:
                del cdata[command[1]]
            else:
                raise RuntimeError(command)
            f = open(
                "./saves/" + name + "/sectors/sector_" + str(id) + ".chunk", mode="wb"
            )
            pickle.dump(cdata, f)
            f.close()
            return
    saveWorld(G.model, name)


def cleanUpModel(model):
    for e in list(model.world.keys())[:]:
        model.remove_block(e, immediate=False, save=False)
    model.entitys = []
    state = model.window.keyEvent
    eventhandler.call("on_model_cleaned_start")
    for e in eventhandler.events["on_draw_3D"]:
        eventhandler.unregister_on_event(e if type(e) == int else e[0])
    for e in eventhandler.events["on_draw_2D"]:
        eventhandler.unregister_on_event(e if type(e) == int else e[0])
    # for e in Inventorys.handler.
    eventhandler.call("on_model_cleaned_end")
    model.window.set_menu(state)
    chat.chat.chattext = ""
    chat.chat.opened = False
