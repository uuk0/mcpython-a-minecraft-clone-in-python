import Item
import Blocks
import Random
import structures
import random
import time

class BiomeHandler:
    def __init__(self):
        self.biomes = {}
        self.prefixes = []

    def getBiome(self, name):
        if type(name) == str:
            if name in self.biomes:
                return self.biomes[name]
            for pre in self.prefixes:
                if pre+":"+name in self.biomes:
                    return self.biomes[pre+":"+name]
            return None
        else:
            return name

class Biome:
    def __init__(self, poslist, seed):
        self.poslist = poslist
        self.generated = []
        self.blocked = []
        self.seed = seed
        self.structurblocked = []

    def getTemperatur(self):
        return None

    def getStructures(self):
        return []

    def getStoneArgs(self): #!
        return ["minecraft:stone"]

    def getHighDiffrents(self, x, z):
        return 0

    def GenerateBiome(self, model):
        for p in self.poslist:
            if p not in self.generated:
                self.generated.append(p)
                x, z = p
                high = self.getHight(model, x, z)
                model.add_block((x, 0, z), "minecraft:bedrock", save=False, immediate=False)
                for y in range(1, 5):
                    if round(Random.randint(self.seed, (x, y, z)) * 4) == 1:
                        model.add_block((x, y, z), "minecraft:bedrock", save=False, immediate=False)
                    else:
                        model.add_block((x, y, z), self.getMaterial(x, y, z, high), save=False, immediate=False)
                for y in range(5, high):
                    if not self.hasOre(x, y, z, high):
                        model.add_block((x, y, z), self.getMaterial(x, y, z, high), save=False, immediate=False)
                    else:
                        model.add_block((x, y, z), self.getOre(x, y, z), save=False, immediate=False)
                struct = self.getStructur((x, y, z), high)
                if struct and not (x, y, z) in self.structurblocked:
                    struct.past(model, x, high, z)

    def getMaterial(self, x, y, z, high):
        pass

    def getOre(self, x, y, z):
        pass

    def getStructur(self, pos, high):
        return None

    def hasOre(self, x, y, z, high):
        return False

    def getName(self):
        return ""

    def getStartHigh(self):
        return 10

    def getHight(self, model, x, z):
        highdata = model.high_data
        if (x, z) in highdata: return highdata[(x, z)]
        sourounding = [(x-1, z-1), (x-1, z), (x-1, z+1), (x, z-1), (x, z), (x, z+1), (x+1, z-1), (x+1, z), (x+1, z+1)]
        high_data = []
        for e in sourounding:
            if e in highdata:
                high_data.append([e, highdata[e]])
        maxh = 0
        minh = 2000
        for e in high_data:
            e = e[1]
            if e > maxh:
                maxh = e
            if e < minh:
                minh = e
        if len(high_data)>0:
            y = round((maxh + minh) / 2)
        else:
            y = self.getStartHigh()
        hd = self.getHighDiffrents(x, z)
        if y + hd >= self.getMinHigh() and y + hd <= self.getMaxHigh(): y += hd
        elif hd > 0 and y + hd > self.getMaxHigh(): y -= hd
        elif hd < 0 and y + hd < self.getMinHigh(): y -= hd
        elif y > self.getMaxHigh(): y = self.getMaxHigh()
        elif y < self.getMinHigh(): y = self.getMinHigh()
        else: pass
        i = 0
        if y < 5:
            y = self.getStartHigh()
        y = round(y)
        model.high_data[(x, z)] = y
        return y

    def getMaxHigh(self):
        return 255

    def getMinHigh(self):
        return 3

class FlatBiomeSandstone(Biome):
    def getHighDiffrents(self, x, z):
        return 0

    def getMaterial(self, x, y, z, high):
        return "minecraft:sandstone"

    def getTemperatur(self):
        return 0

    def getHight(self, model, x, z):
        return 10

class FlatBiomeDirt(Biome):
    def getHighDiffrents(self, x, z):
        return 0

    def getMaterial(self, x, y, z, high):
        return "minecraft:dirt" if y != high else "minecraft:grass"

    def getTemperatur(self):
        return 0

    def getHight(self, model, x, z):
        return 10

class ColdTaiga(Biome): #missing: snow layers, snowing, grass, farn, flowers, mushrooms, wolfs, kaninchen
    def getName(self):
        return "minecraft:biome:cold_taiga"

    def getStructures(self):
        return ["minecraft:structur:spruce_tree"]

    def getHighDiffrents(self, x, z):
        return round(Random.randint(self.seed, [x, z, 123]) * 4 - 2) if round(Random.randint(self.seed, [x, z, 0]) * 3) == 1 else 0

    def getTemperatur(self):
        return 1

    def getOre(self, x, y, z):
        return random.choice(["minecraft:iron_ore", "minecraft:coal_ore", "minecraft:diamond_ore", "minecraft:gold_ore", "minecraft:emerald_ore"])

    def hasOre(self, x, y, z, high):
        r = round(Random.randint(self.seed, [x, y, z, high]) * 15) == 1 and high / 1.5 > y
        return r

    def getMaterial(self, x, y, z, high):
        return "minecraft:stone" if high / 1.5 > y else ("minecraft:dirt" if y != high - 1 else "minecraft:grass")

    def getStructur(self, pos, high):
        r = round(Random.randint(self.seed, [pos, high]) * 30)
        if r == 1:
            return structures.handler.structurs[self.getStructures()[0]]
        return None

    def getStartHigh(self):
        return 20

    def getMaxHigh(self):
        return 100

    def getMinHigh(self):
        return 30

class ColdTaiga_M(ColdTaiga):
    def getHighDiffrents(self, x, z):
        return round(Random.randint(self.seed, [x, z, 123]) * 8 - 4) if round(Random.randint(self.seed, [x, z, 0]) * 3) == 1 else 0

    def getName(self):
        return "minecraft:biome:cold_taiga_m"

    def getMaxHigh(self):
        return 200

    def getMinHigh(self):
        return 30

class ColdTaigaHills(ColdTaiga):
    def getHighDiffrents(self, x, z):
        return round(Random.randint(self.seed, [x, z, 123]) * 6 - 3) if round(Random.randint(self.seed, [x, z, 0]) * 3) == 1 else 0

    def getName(self):
        return "minecraft:biome:cold_taiga_hills"

    def getMaxHigh(self):
        return 150

    def getMinHigh(self):
        return 30

class ColdTaigaHillsBig(ColdTaigaHills):
    def getStructures(self):
        return ["minecraft:structur:big_spruce_tree"]

    def getName(self):
        return "minecraft:biome:cold_taiga_hills_big"

class ColdTundra(Biome):
    def getName(self):
        return "minecraft:biome:cold_tundra"

    def getStructures(self):
        return ["minecraft:structur:spruce_tree"]

    def getHighDiffrents(self, x, z):
        return round(Random.randint(self.seed, [x, z, 123]) * 4 - 2) if round(Random.randint(self.seed, [x, z, 0]) * 3) == 1 else 0

    def getTemperatur(self):
        return 1

    def getOre(self, x, y, z):
        return random.choice(["minecraft:iron_ore", "minecraft:coal_ore", "minecraft:diamond_ore", "minecraft:gold_ore", "minecraft:emerald_ore"])

    def hasOre(self, x, y, z, high):
        r = round(Random.randint(self.seed, [x, y, z, high]) * 15) == 1 and high / 1.5 > y
        return r

    def getMaterial(self, x, y, z, high):
        return "minecraft:stone" if high / 1.5 > y else ("minecraft:dirt" if y != high - 1 else "minecraft:grass")

    def getStructur(self, pos, high):
        r = round(Random.randint(self.seed, [pos, high]) * 60)
        if r == 1:
            return structures.handler.structurs[self.getStructures()[0]]
        return None

    def getStartHigh(self):
        return 20

    def getMaxHigh(self):
        return 100

    def getMinHigh(self):
        return 30

class ColdTundraIcicle(ColdTundra):
    def getStructures(self):
        return ["minecraft:structur:spruce_tree", "minecraft:structur:icicle",
                "minecraft:structur:oak_tree"]

    def getStructur(self, pos, high):
        random.seed(time.time())
        r = random.randint(1, 60)
        if r == 1:
            return structures.handler.structurs[self.getStructures()[0]]
        elif r in range(2, 5):
            return structures.handler.structurs[self.getStructures()[1]]
        elif r == 5:
            return structures.handler.structurs[self.getStructures()[2]]
        return None