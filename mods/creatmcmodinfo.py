import pickle

file = input("file? ")
name = input("name? ")
mcversion = input("mcversion id? ")
mlversion = "0.0.2"
mainfile = input("main file? ")


with open(file, mode="wb") as f:
    pickle.dump(
        {
            "name": name,
            "MCPYTHON_VERSION": mcversion,
            "MODLOADER_VERSION": mlversion,
            "MAIN_FILE": mainfile,
        },
        f,
    )
