import os
import importlib
import globals as G

for f in os.listdir(G.local + "/mods/mcpython/Commands"):
    if os.path.isfile(G.local + "/mods/mcpython/Commands/" + f) and not f in [
        "__init__.py"
    ]:
        name = f.split(".")[0]
        locals()[name] = importlib.import_module("Commands." + name)
