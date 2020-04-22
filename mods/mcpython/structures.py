import pickle
import globals as G
import Random
import random

STRUCTUR_VERSION = "0.0.5"
COMPATIBLE = [STRUCTUR_VERSION, "0.0.3", "0.0.4"]

""".structur file data:
pickled: {"version":"0.1.1",
          "size":(x, y, z),
          "blocks":[<blocklist>],
          "name":name}

block: [mode, ...]
mode = 0: add block with name at position
mode = 1: remove block at position
mode = 2: nbtchange x y z name data"""

class StructurHandler:
    def __init__(self):
        self.structurs = {}

    def register(self, structur):
        self.structurs[structur.name] = structur


handler = StructurHandler()

class Structur:
    def __init__(self, file):
        f = open(G.local+"/assets/structures/"+file+".structur", mode="rb")
        data = pickle.load(f)
        f.close()
        if not data["version"] in COMPATIBLE:
            print("[ERROR] can't load structur "+file+". structur version not compatible")
        else:
            self.size = data["size"]
            self.blocks = data["blocks"]
            self.name = data["name"]
            self.data = data
            #self.base = data[""]
            handler.register(self)

    def past(self, model, x, y, z):
        for e in self.blocks:
            if e[0] == 0:
                model.add_block((e[2][0]+x, e[2][1]+y, e[2][2]+z), e[1], save=False)
            elif e[0] == 1:
                model.remove_block((e[1][0]+x, e[1][1]+y, e[1][2]+z), save=False)
            elif e[0] == 2:
                model.world[(e[1][0]+x, e[1][1]+y, e[1][2]+z)].setNBT(e[2], e[3])

class GenerationStructur:
    def __init__(self):
        self.name = self.getName()
        handler.register(self)

    def past(self, model, x, y, z):
        raise RuntimeError("class "+str(self.__class__)+" has no past notation")

    def getName(self):
        return "minecraft:structur:none"

class SpruceTree(GenerationStructur):
    def getName(self):
        return "minecraft:structur:spruce_tree"

    def past(self, model, x, y, z):
        high = round(Random.randint(G.seed, [x, y, z, self.getName(), random.randint(0, 10)]) * 6) + 4
        for dy in range(0, high+1):
            yr = y + dy
            G.model.add_block((x, yr, z), "minecraft:wood_log_2", save=False, immediate=False)
            if dy > high / 4 and (((dy % 2 == 0 and high % 2 == 0) or (dy % 2 == 1 and high % 2 == 1)) or dy == high):
                G.model.add_block((x - 1, yr, z), "minecraft:leave_0", save=False, immediate=False)
                G.model.add_block((x + 1, yr, z), "minecraft:leave_0", save=False, immediate=False)
                G.model.add_block((x, yr, z - 1), "minecraft:leave_0", save=False, immediate=False)
                G.model.add_block((x, yr, z + 1), "minecraft:leave_0", save=False, immediate=False)
        G.model.add_block((x, y+high+1, z), "minecraft:leave_0", save=False, immediate=False)

SpruceTree = SpruceTree()

class BigSruceTree(GenerationStructur):
    def getName(self):
        return "minecraft:structur:big_spruce_tree"

    def past(self, model, x, y, z):
        high = round(Random.randint(G.seed, [x, y, z, self.getName(), random.randint(0, 10)]) * 12) + 4
        for dy in range(0, high+1):
            yr = y + dy
            G.model.add_block((x, yr, z), "minecraft:wood_log_2", save=False, immediate=False)
            if dy > high / 4 and (((dy % 2 == 0 and high % 2 == 0) or (dy % 2 == 1 and high % 2 == 1)) or dy == high):
                G.model.add_block((x - 1, yr, z), "minecraft:leave_0", save=False, immediate=False)
                G.model.add_block((x + 1, yr, z), "minecraft:leave_0", save=False, immediate=False)
                G.model.add_block((x, yr, z - 1), "minecraft:leave_0", save=False, immediate=False)
                G.model.add_block((x, yr, z + 1), "minecraft:leave_0", save=False, immediate=False)
        G.model.add_block((x, y+high+1, z), "minecraft:leave_0", save=False, immediate=False)

BigSruceTree = BigSruceTree()

class icicle(GenerationStructur):
    def getName(self):
        return "minecraft:structur:icicle"

    def past(self, model, x, y, z):
        a = x
        b = z
        c = z
        h = random.randint(3, 8)  # height of the hill
        s = random.randint(1, 3)  # 2 * s is the side length of the hill
        t = random.choice(["minecraft:ice", "minecraft:packed_ice", "minecraft:blue_ice"])
        for y in range(c, c + h):
            for x in range(a - s, a + s + 1):
                for z in range(b - s, b + s + 1):
                    if (x - a) ** 2 + (z - b) ** 2 > (s + 1) ** 2:
                        continue
                    if (x - 0) ** 2 + (z - 0) ** 2 < 5 ** 2:
                        continue
                    G.model.add_block((x, y, z), t, immediate=False, save=False)
            s -= round(random.randint(0, 15) / 15)

icicle = icicle()

class OakTree(GenerationStructur):
    def getName(self):
        return "minecraft:structur:oak_tree"

    def past(self, model, x, y, z):
        high = random.randint(3, 8)
        leavehigh = random.randint(2, 4)
        for yr in range(0, high):
            G.model.add_block((x, y+yr, z), "minecraft:wood_log_2", immediate=False, save=False)
        y += leavehigh
        for yr in range(y, y+(high-leavehigh)):
            for xr in range(-2, 3):
                for zr in range(-2, 3):
                    G.model.add_block((x+xr, yr, zr+z), "minecraft:leave_0", immediate=False, save=False)
        for xr in range(-1, 2):
            for zr in range(-1, 2):
                G.model.add_block((x+xr, y+high+1, z+zr), "minecraft:leave_0", immediate=False, save=False)


oaktree = OakTree()