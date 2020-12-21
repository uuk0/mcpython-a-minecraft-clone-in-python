import biomes
import random
import globals as G
import Dimension
import EventHandler


class World:
    def __init__(self, model, seed, type, subtypes=[]):
        self.model = model
        self.seed = seed
        self.type = type
        self.subtypes = subtypes
        self.biomes = []
        self.spawnpoint = (random.randint(-8, 8), random.randint(-8, 8))
        self.chunkdata = None
        self.hubtype = 0  # 0:client, 1:client_op, 2:sever, 3:sever_op, 4:command_block
        G.player.dimension = Dimension.Overworld()
        print("preparing overworld...")
        G.player.dimension.prepare()
        print("finished")

    def generateChunk(self, x, z):
        G.player.dimension.generateChunk((x, z))
        EventHandler.eventhandler.call("on_chunk_generate", x, z, self, instant=True)
        G.model.generated.append((x, z))
