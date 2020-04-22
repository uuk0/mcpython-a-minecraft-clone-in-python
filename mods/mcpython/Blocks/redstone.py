from .Block import *
import random

class Redstone(Block):
    def on_creat(self):
        self.sides = {"N":None, "O":None, "S":None, "W":None}
        self.state = 0

    def getName(self):
        return "minecraft:redstone"

    def getNBTNames(self):
        return ["side_n", "side_o", "side_s", "side_w", "state"]

    def getTex(self):
        return tex_coords((2, 0), (2, 0), (2, 0))

    def getTexturFile(self):
        pass