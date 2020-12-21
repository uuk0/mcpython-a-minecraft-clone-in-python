from moduls import *
from EventHandler import eventhandler
from mathhelper import *
import texturGroups


class EntityHandler:
    def __init__(self):
        self.entitys = {}
        self.entitysfromid = {}
        self.prefixes = []
        self.todraw = []
        eventhandler.on_event("on_draw_3D", self.draw)

    def register(self, entityclass):
        name = entityclass((0, 0, 0), test=True).getName()
        self.entitys[name] = entityclass
        self.entitysfromid[entityclass((0, 0, 0), test=True).getId()] = entityclass
        if not name.split(":")[0] in self.prefixes:
            self.prefixes.append(name.split(":")[0])

    def getByName(self, name):
        if type(name) == str:
            if name in self.entitys:
                return self.entitys[name]
            for pre in self.prefixes:
                if pre + ":" + name in self.entitys:
                    return self.entitys[pre + ":" + name]
            return None
        else:
            return name

    def getById(self, id):
        return self.entitysfromid[id]

    def registerInst(self, inst):
        self.todraw.append(inst)

    def draw(self, *args):
        for e in self.todraw:
            drawable = e.getRanderAble()
            if drawable != None and hasattr(drawable, "draw"):
                drawable.draw()


entityhandler = EntityHandler()


class Entity:  # THIS IS THE SUMMONABLE COMPONENT CLASS
    def __init__(self, position, test=False):
        self.position = position
        self.on_creat()
        if not test:
            entityhandler.registerInst(self)
        self.lastpositions = []
        for e in self.getBoxModels():
            self.lastpositions.append(e.position)

    def getRanderAble(self):  #!
        return None

    def setPosition(self, position):  #!
        for i, e in enumerate(self.getBoxModels()):
            lpos = self.lastpositions[i]
            spos = e.position
            dpos = (lpos[0] - spos[0], lpos[1] - spos[1], lpos[2] - spos[2])
            e.position[0] -= dpos[0]
            e.position[1] -= dpos[1]
            e.position[2] -= dpos[2]
        self.position = position

    def setRotation(self):  #!
        pass

    def drawHitBox(self):  #!
        pass

    def hasHitBox(self):  #!
        return False

    def isHitting(self, *args):  #!
        pass

    def on_creat(self):
        pass

    def getId(self):
        return 0

    def getName(self):
        return "minecraft:none"

    def getBoxModels(self):
        return []

    def getInventory(self):
        return []

    def kill(self):
        pass
