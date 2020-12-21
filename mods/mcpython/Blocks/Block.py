from mathhelper import *
from texturGroups import handler as texturhandler
from moduls import *
from destroyGroup import *
import texturGroups


class Block:
    def __init__(self, pos, hitblock=None, register=False):
        self.pos = pos
        self.redstone_level = self.defaultRedstoneLevel()
        if not register:
            self.on_creat()

    def getTex(self):
        print("[ERROR] unknown block-definition-tex: " + str(self))
        raise RuntimeError()

    def update(self, model, window):
        pass

    def getName(self):
        return "unknown:block"

    def isBreakAble(self):
        return True

    def getTexturFile(self):
        return 0

    def defaultRedstoneLevel(self):
        return False

    def getItemName(self):
        return self.getName()

    dropamounts = [1]

    def getDropAmount(self, item):
        return self.dropamounts

    drops = [None]  # if first == None, None is replaced by blockname

    def getDrop(self, item):
        if self.drops[0] == None:
            self.drops[0] = self.getItemName()
        return self.drops

    def hasHitbox(self, item):  #!?
        return True

    destroygroups = []

    def getDestroyGroups(self):
        return self.destroygroups

    def getHardness(self):
        return 1

    def getBrakeSoundFile(self):  #!
        return "./sounds/dig/stone1.ogg"

    def getVisualName(self):
        return self.getName()

    def redstoneStateUpdate(self, model, world):  #!
        pass

    def __call__(self, *args, **kwargs):
        obj = self.__class__(*args, **kwargs)
        obj.setAllNBT(self.getAllItemNBT())

    def getInfoData(self):
        return ""

    def getNBTNames(self):
        return []

    def setNBT(self, name, value):
        pass

    def getNBT(self, name):
        pass

    def generateTEX(self):
        pass

    def getAllNBT(self):
        return []

    def getAllItemNBT(self):
        return {}

    def setAllNBT(self, nbt):
        pass

    def hasInventory(self):
        return False

    def getInventoryID(self):
        return 0

    def show(self, model, window, texture):
        x, y, z = position = self.pos
        vertex_data = cube_vertices(x, y, z, 0.5)
        texture_data = list(texture)
        # create vertex list
        # FIXME Maybe `add_indexed()` should be used instead
        model._shown[position] = model.batch.add(
            24,
            GL_QUADS,
            texturGroups.handler.getGroup(model.world[position].getTexturFile()),
            ("v3f/static", vertex_data),
            ("t2f/static", texture_data),
        )

    def hide(self, model, window):
        position = self.pos
        if position in model._shown:
            model._shown.pop(position).delete()

    def on_creat(self):
        pass

    def on_left_click(self, block, previos, button, modifiers):
        pass

    def on_right_click(self, block, previos, button, modifiers):
        pass

    def isBreakAbleWithItem(self, item):
        return True

    oredictnames = []

    def getOreDictNames(self):
        return self.oredictnames

    inventorys = []

    def getInventorys(self):
        return self.inventorys

    def hasAlpha(self):  #!
        return False

    def hasEnergyStorage(self, side):  #!
        return False

    def getMaxEnergyStorage(self, side):  #!
        return 0

    def getEnergyMode(self, side):  #!
        return 0  # 0: none, 1: only output, 2: only input, 3: balance, 4: input / output if nesesary (fill other maschines before)

    def getEnergyPriority(self, side):  #!
        return 0

    def getStoredEnergy(self, side):  #!
        return 0

    def getId(self):
        return -1

    def getStoreData(self):
        pass

    def setStoreData(self, data):
        pass

    def getPlayerDamage(
        self,
    ):  # the damge when a player is standing near the block (d<0.2)
        return 0

    def getBlastResistence(self):  # get the resistance of the block when exploding
        return 0

    def isFlameAble(self):
        return False

    def isBlockingExplosions(self):
        return False

    def isMoveable(self):
        return True

    def isFullBlock(self):
        return True

    def on_destroy(self):
        pass


class BlockHandler:
    def __init__(self):
        self.blocks = {}
        self.blocksfromid = {}
        self.prefixes = []

    def __call__(self, *args, **kwargs):
        self.register(args[0])
        return args[0]

    def register(self, blockclass):
        name = blockclass((0, 0, 0), register=True).getName()
        self.blocks[name] = blockclass
        self.blocksfromid[blockclass((0, 0, 0), register=True).getId()] = blockclass
        if not name.split(":")[0] in self.prefixes:
            self.prefixes.append(name.split(":")[0])

    def getByName(self, name):
        if type(name) == str:
            if name in self.blocks:
                return self.blocks[name]
            for pre in self.prefixes:
                if pre + ":" + name in self.blocks:
                    return self.blocks[pre + ":" + name]
            return None
        else:
            return name

    def getById(self, id):
        return self.blocksfromid[id]


handler = BlockHandler()


class BlockState:
    def __init__(self, blockid, position):
        self.blockid = blockid
        self.position = position
        self.blockclass = handler.getById(blockid)
