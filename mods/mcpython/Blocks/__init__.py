import os
import importlib
import globals as G

print(G.local)
for f in os.listdir(G.local + "/mods/mcpython/Blocks"):
    if os.path.isfile(G.local + "/mods/mcpython/Blocks/" + f) and not f in [
        "__init__.py"
    ]:
        print("[FILELOADER/INFO] loading file", f)
        name = f.split(".")[0]
        locals()[name] = importlib.import_module("Blocks." + name)

"""
missing:

bubble column
clay
terracotta
coarse dirt
mycellium
podzol
red sand
granit
andesit
lapis ore
redstoen ore
glowstone
magma block
netherrack
soul sand
nether quartz ore
carpet
mossy cobbelstone
cobbelstone wall
cobweb
end portal frame
fence
fire
flower pot
glass
glass pane
grass path
iron bars
ladder
monsteregg blocks
spawner
polished andersit
polished granit
prismarin
prismarin brick
dark prismarin
sea latern
cut sandstone
chiseled sandstone
sponge
wet sponge
cracked stonebrick
mossy stonebrick
chiseled stonebrick
nether brick
nether brick fence
nether portal
nether wart
dragon egg
end gateway
end portal
ender rod
stained glass
beetrod
carot
chorus plant
chorus flower
cocoa
dead bush
fern
large fern
flowers
grass
tall grass
kelp
dried kelp
more leaves
lily pad
strpped log
more wod logs?
melon
melon stam
potato
pumkin
pumkin stam
sea grass
tall sea grass
sugar cane
vines
wheat
turtel egg
coral
sea pickle
mushroom
banner
... 
"""
# TODO add these blocks
# TODO add emeralds to emerald ore
