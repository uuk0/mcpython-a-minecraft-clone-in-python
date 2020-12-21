from .Block import *

from oredictnames import OreDict


class TexturError(Exception):
    pass


SIDES = {
    "N": "mcpython:side:N",
    "O": "mcpython:side:O",
    "S": "mcpython:side:S",
    "W": "mcpython:side:W",
    "U": "mcpython:side:U",
    "D": "mcpython:side:D",
    "A": "mcpython:side:A",
}


class WoodLog(Block):
    def __init__(self, *args, side=None, **kwargs):
        Block.__init__(self, *args, **kwargs)
        hitblock = kwargs["hitblock"] if "hitblock" in kwargs else (0, 0, 0)
        pos = kwargs["pos"] if "pos" in kwargs else (0, 0, 0)
        self.side = side
        if self.side == None:
            if hitblock == None:
                hitblock = (pos[0], pos[1] + 1, pos[2])
            if hitblock[1] > pos[1]:
                self.side = SIDES["U"]
            elif hitblock[1] < pos[1]:
                self.side = SIDES["D"]
            elif hitblock[0] > pos[0]:
                self.side = SIDES["N"]
            elif hitblock[0] < pos[0]:
                self.side = SIDES["S"]
            elif hitblock[2] > pos[2]:
                self.side = SIDES["O"]
            elif hitblock[2] < pos[2]:
                self.side = SIDES["W"]
            else:
                self.side = SIDES["U"]
        self.generateTEX()

    def generateTEX(self):
        if self.side == SIDES["U"] or self.side == SIDES["D"]:
            self.tex = total_tex_coords(
                self.getTexturFront(),
                self.getTexturFront(),
                self.getTexturSide(),
                self.getTexturSide(),
                self.getTexturSide(),
                self.getTexturSide(),
            )
        elif self.side == SIDES["N"] or self.side == SIDES["S"]:
            self.tex = total_tex_coords(
                self.getTexturSideB(),
                self.getTexturSide(),
                self.getTexturFront(),
                self.getTexturFront(),
                self.getTexturSide(),
                self.getTexturSide(),
            )
        elif self.side == SIDES["O"] or self.side == SIDES["W"]:
            self.tex = total_tex_coords(
                self.getTexturSide(),
                self.getTexturSideB(),
                self.getTexturSide(),
                self.getTexturSide(),
                self.getTexturFront(),
                self.getTexturFront(),
            )
        elif self.side == SIDES["A"]:
            self.tex = total_tex_coords(
                self.getTexturSide(),
                self.getTexturSide(),
                self.getTexturSide(),
                self.getTexturSide(),
                self.getTexturSide(),
                self.getTexturSide(),
            )
        else:
            print("[ERROR] side is incorrect by wood_log")
            print("-> reseting sides...")
            self.side = SIDES["U"]
            self.generateTEX()

    def getTexturFront(self):
        return

    def getTexturSide(self):
        return

    def getTexturSideB(self):
        return

    def getTex(self):
        return self.tex

    def getInfoData(self):
        return (
            self.getName()
            + "/instance/"
            + str(id(self))
            + "/{tex="
            + str(self.tex)
            + ", side="
            + str(self.side)
            + "}"
        )

    def getNBTNames(self):
        return ["side", "tex"]

    def setNBT(self, name, value):
        if name == "side":
            if value in SIDES.keys():
                value = SIDES[value]
            self.side = str(value)
            self.generateTEX()

    def getNBT(self, name):
        if name == "side":
            return self.side
        elif name == "tex":
            return self.tex

    def getAllNBT(self):
        return {"side": self.side}

    def getAllItemNBT(self):
        return {"side": self.side}

    def setAllNBT(self, nbt):
        # print(nbt, "side" in nbt.keys())
        if "side" in nbt.keys():
            self.side = nbt["side"]
            self.generateTEX()

    destroygroups = [destroyGroups.AXE]

    def getBlastResistence(self):
        # todo add constant
        return -1

    def getHardness(self):
        return 2

    def getId(self):
        return 17


class Wood_Log_0(WoodLog):
    def getTexturFront(self):
        return (10, 2)

    def getTexturSide(self):
        return (10, 0)

    def getTexturSideB(self):
        return (10, 1)

    def getName(self):
        return "minecraft:wood_log_0"

    def getOreDictNames(self):
        return [OreDict.AcaciaLogs]


handler.register(Wood_Log_0)


class Wood_Log_1(WoodLog):
    def getTexturFront(self):
        return (11, 2)

    def getTexturSide(self):
        return (11, 0)

    def getTexturSideB(self):
        return (11, 1)

    def getName(self):
        return "minecraft:wood_log_1"

    def getOreDictNames(self):
        return OreDict.BirchLogs


handler.register(Wood_Log_1)


class Wood_Log_2(WoodLog):
    def getTexturFront(self):
        return (12, 2)

    def getTexturSide(self):
        return (12, 0)

    def getTexturSideB(self):
        return (12, 1)

    def getName(self):
        return "minecraft:wood_log_2"

    def getOreDictNames(self):
        return [OreDict.DarkOakLogs]


handler.register(Wood_Log_2)


class Wood_Log_3(WoodLog):
    def getTexturFront(self):
        return (10, 3)

    def getTexturSide(self):
        return (11, 3)

    def getTexturSideB(self):
        return (12, 3)

    def getName(self):
        return "minecraft:wood_log_3"

    def getOreDictNames(self):
        return [OreDict.JungleLogs]


handler.register(Wood_Log_3)


class Wood_Log_4(WoodLog):
    def getTexturFront(self):
        return (11, 10)

    def getTexturSide(self):
        return (11, 11)

    def getTexturSideB(self):
        return (11, 11)

    def getName(self):
        return "minecraft:wood_log_4"

    def getOreDictNames(self):
        return [OreDict.OakLogs]


handler.register(Wood_Log_4)
