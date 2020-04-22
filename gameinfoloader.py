import config, pickle, globals as G

def loadData():
    with open(G.local+"/gameinfo.dat", mode="rb") as f:
        data = pickle.load(f)
    config.CONFIGS["info"] = data
    config.CONFIGS["GAME_VERSION"] = data["version_name"]
    config.CONFIGS["VERSION_ID"] = data["version_id"]