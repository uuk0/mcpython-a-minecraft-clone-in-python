import os
import importlib
import globals as G

for f in os.listdir(G.local + "/mods/mcpython/Item"):
    if os.path.isfile(G.local + "/mods/mcpython/Item/" + f) and not f in [
        "__init__.py"
    ]:
        name = f.split(".")[0]
        locals()[name] = importlib.import_module("Item." + name)
