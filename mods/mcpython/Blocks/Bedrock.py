from .Block import *

@handler
class Bedrock(Block):
    def getTex(self):
        return tex_coords((3, 0), (3, 0), (3, 0))

    def getName(self):
        return "minecraft:bedrock"

    def isBreakAble(self):
        return False

    def getBlastResistence(self):
        return 18000000

    def getId(self):
        return 7

    drops = []

    def isMoveable(self):
        return False
