import Blocks
import Item
import biomes
import IDGenerator
import config
import random
import globals as G
import EventHandler
import time
import WorldSaver
import mathhelper
import pyfastnoisesimd


class DimensionHandler:
    def __init__(self):
        self.dimensions = {}
        self.dim = None

    def load(self, id):
        if self.dim:
            self.dim.unload()
        dim = self.dimensions[id]
        WorldSaver.cleanUpModel(G.model)
        dim.load()
        G.player.dimension = dim


handler = DimensionHandler()


class Dimension:
    def __init__(self):
        self.id = (
            IDGenerator.handler.getDimensionId() if not self.getId() else self.getId()
        )
        self.chunks = {}
        self.biome_data = {}
        self.height_data = {}
        self.biome_instances = {}
        self.world_data = {}
        handler.dimensions[self.id] = self

    def getBiomes(self):
        return []

    def getBiomeStepList(self):
        return {}

    def generateChunk(self, chunk):
        bios = []
        for x in range(chunk[0] * 16, chunk[0] * 16 + 16):
            for z in range(chunk[1] * 16, chunk[1] * 16 + 16):
                if not (x, z) in self.biome_data:
                    raise ValueError("getted an unprepared area-biome-data", x, z)
                self.biome_instances[self.biome_data[(x, z)]].poslist.append((x, z))
                if not self.biome_instances[self.biome_data[(x, z)]] in bios:
                    bios.append(self.biome_instances[self.biome_data[(x, z)]])
        for biome in bios:
            biome.GenerateBiome(G.model)
        if random.randint(1, 5) == 1 and config.CONFIGS["GENERATE_PERLIN"]:
            bpos = chunk[0] * 16, chunk[1] * 16
            pos = []
            for _ in range(random.randint(1, 5)):
                x, z = random.randint(bpos[0], bpos[0] + 15), random.randint(
                    bpos[1], bpos[1] + 15
                )
                y = G.model.high_data[(x, z)]
                pos.append((x, y, z))

            print("adding perlin...")
            data = pyfastnoisesimd.generate([255, 255, 255], start=pos, seed=G.seed)

            print("sorting them for generation...")
            dt = time.time()
            i = -1
            ch = []
            for xl in data:
                for zl in xl:
                    pos = zl[0]
                    cx, _, cz = mathhelper.sectorize((pos[0], pos[1], pos[2]))
                    self.perlin_positions[(zl[0][0], zl[0][2])] = zl
                    if not (cx, cz) in ch:
                        ch.append((cx, cz))
                    i += 1
                    if time.time() - dt > 1:
                        dt = time.time()
                        print(str(round(i / (255 * 255 * 255) * 100)) + "%")

            for e in ch:
                if e in G.model.generated:
                    print("applying perlins to chunk", e)
                    print(self.perlin_positions[chunk])
                    dt = time.time()
                    for x in range(chunk[0] * 16, chunk[0] * 16 + 16):
                        for z in range(chunk[1] * 16, chunk[1] * 16 + 16):
                            if (x, z) in self.perlin_positions:
                                for y, v in enumerate(self.perlin_positions[(x, z)]):
                                    if v >= 0 and (x, y, z) in G.model.world:
                                        G.model.remove_block(
                                            (x, y, z), immediate=False, save=False
                                        )
                                    if time.time() - dt > 1:
                                        dt = time.time()
                                        print(
                                            str(
                                                round(
                                                    i
                                                    / len(self.perlin_positions[chunk])
                                                    * 100
                                                )
                                            )
                                            + "%"
                                        )

            print("looking for perlin-positions for asked chunk", chunk)
            if not chunk in self.perlin_positions:
                print("[ERROR] generated perlin and found NONE in chunk")
            else:
                pass

    def getBiomeSize(self):  # Wahrscheinlichkeit, das es ein neues biom gibt
        return 10

    def prepare(self):
        # biomes = self.getBiomes()
        size = int(config.CONFIGS["HIGHMAPWORLDSIZE"])
        index = 0
        last = time.time()
        for x in range(-size, size + 1):
            for z in range(-size, size + 1):
                surrounding = []
                biome = None
                maxt = {}
                for p in [(x + 1, z), (x - 1, z), (x, z + 1), (x, z - 1)]:
                    if p in self.biome_data:
                        surrounding.append(self.biome_data[p])
                for e in surrounding:
                    if e in maxt:
                        maxt[e] += 1
                    else:
                        maxt[e] = 1
                max = (0, None)
                for e in maxt.keys():
                    if max[1] == None or maxt[e] > max[1]:
                        max = (maxt[e], e)

                if len(surrounding) == 0:
                    biome = random.choice(self.getBiomes())
                else:
                    w = random.randint(1, self.getBiomeSize()) == 1
                    if not w:
                        biome = max[1]
                    else:
                        biome = random.choice(self.getBiomeStepList()[max[1]])

                if biome == None:
                    biome = random.choice(self.getBiomes())

                if type(biome) != int:
                    biome = self.getBiomes().index(biome)
                if not biome in self.biome_instances:
                    self.biome_instances[biome] = self.getBiomes()[biome]([], G.seed)
                self.biome_instances[biome].getHight(G.model, x, z)
                self.biome_data[(x, z)] = biome
                index += 1
                if time.time() - last > 1:
                    print(round(index / ((size * 2 + 1) * (size * 2 + 1)) * 100), "%")
                    last = time.time()
                if biome not in self.getBiomeStepList():
                    print("error unknown biome added: ", biome)
        print("generating perlins")
        self.perlin_positions = {}

    def load(self):
        G.model.world = self.world_data

    def unload(self):
        self.world_data = G.model.world

    def getId(self):
        return None


class Overworld(Dimension):
    def getBiomes(self):
        return [
            biomes.ColdTaiga,
            biomes.ColdTaiga_M,
            biomes.ColdTaigaHills,
            biomes.ColdTaigaHillsBig,
            biomes.ColdTundra,
            biomes.ColdTundraIcicle,
        ]

    def getBiomeStepList(self):
        return {
            0: [1, 2, 4],
            1: [0, 2, 3],
            2: [0, 1, 3],
            3: [0, 1, 2],
            4: [0, 5],
            5: [4],
        }

    def getBiomeSize(self):
        return 20

    def getId(self):
        return 0
