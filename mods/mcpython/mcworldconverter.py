import nbt
import globals as G
import WorldSaver
import os
import traceback
import Dimension

MinecraftIdToBlockName = {0: None, 1: "minecraft:stone"}


def convert(folder):  # MINECRAFT WORLD 1.12
    print("loading minecraft-world", folder)
    WorldSaver.cleanUpModel(G.model)
    if not os.path.isdir(folder):
        folder = "./saves/" + folder
    file = nbt.nbt.NBTFile(folder + "/level.dat")

    G.seed = file.tags[0].tags[0]
    G.window.seed = G.seed

    print("new world seed:", G.seed)

    G.window.gametime = file.tags[0]["Time"].value

    for region_file in os.listdir(folder + "/region"):
        file = nbt.nbt.NBTFile(folder + "/" + region_file)

    raise RuntimeError("can't load mc-world: mcworldloader is not added")
