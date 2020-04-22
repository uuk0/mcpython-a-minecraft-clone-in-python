from moduls import *
from .entity import *
from mathhelper import *
from .boxmodel import *

import math
import globals as G

BODY_HEIGHT = 2.0 / 3.0
BODY_LENGTH = BODY_HEIGHT * (2.0 / 3.0)
BODY_WIDTH = BODY_LENGTH / 2
HEAD_LENGTH = BODY_LENGTH
HEAD_WIDTH = HEAD_LENGTH
HEAD_HEIGHT = HEAD_LENGTH
ARM_HEIGHT = BODY_HEIGHT
ARM_LENGTH = BODY_WIDTH
ARM_WIDTH = BODY_WIDTH
LEG_HEIGHT = BODY_HEIGHT
LEG_LENGTH = BODY_WIDTH
LEG_WIDTH = BODY_WIDTH

class Player(object):
    def __init__(self, position):
        self.player = None
        self.position = position
        self.rotation = (0, 0, 0)
        image = load_image(G.local+"/assets/textures/mob/player/char.png")
        # head
        self.head = BoxModel(HEAD_LENGTH, HEAD_WIDTH, HEAD_HEIGHT, image, 32, 32, 32)
        self.head.update_texture_data([(32, 96), (64, 96), (0, 64), (64, 64), (32, 64), (96, 64)])
        # body
        self.body = BoxModel(BODY_LENGTH, BODY_WIDTH, BODY_HEIGHT, image, 32, 16, 48)
        self.body.update_texture_data([(80, 48), (112, 48), (64, 0), (112, 0), (80, 0), (128, 0)])
        # left/right arm
        self.left_arm = BoxModel(ARM_LENGTH, ARM_WIDTH, ARM_HEIGHT, image, 16, 16, 48)
        self.left_arm.update_texture_data(
            [(176, 48), (176 + 16, 48), (176, 0), (176 + 32, 0), (176 - 16, 0), (176 + 16, 0)])
        self.right_arm = BoxModel(ARM_LENGTH, ARM_WIDTH, ARM_HEIGHT, image, 16, 16, 48)
        self.right_arm.update_texture_data(
            [(176, 48), (176 + 16, 48), (176, 0), (176 + 32, 0), (176 - 16, 0), (176 + 16, 0)])
        # left/right leg
        self.left_leg = BoxModel(LEG_LENGTH, LEG_WIDTH, LEG_HEIGHT, image, 16, 16, 48)
        self.left_leg.update_texture_data([(16, 48), (16 + 16, 48), (0, 0), (32, 0), (16, 0), (48, 0)])
        self.right_leg = BoxModel(LEG_LENGTH, LEG_WIDTH, LEG_HEIGHT, image, 16, 16, 48)
        self.right_leg.update_texture_data([(16, 48), (16 + 16, 48), (0, 0), (32, 0), (16, 0), (48, 0)])

        self.update_position(position)

    def update_position(self, position, init=False):
        self.position = position
        x, y, z = position
        foot_height = y - 1.25

        self.head.position = (x - HEAD_LENGTH / 2, foot_height + LEG_HEIGHT + BODY_HEIGHT, z - HEAD_WIDTH / 2)
        self.body.position = (x - BODY_LENGTH / 2, foot_height + LEG_HEIGHT, z - BODY_WIDTH / 2)
        self.left_arm.position = (x - BODY_LENGTH / 2 - ARM_LENGTH, foot_height + LEG_HEIGHT, z - BODY_WIDTH / 2)
        self.right_arm.position = (x + BODY_LENGTH / 2, foot_height + LEG_HEIGHT, z - BODY_WIDTH / 2)
        self.left_leg.position = (x - BODY_LENGTH / 2, foot_height, z - BODY_WIDTH / 2)
        self.right_leg.position = (x - BODY_LENGTH / 2 + LEG_LENGTH, foot_height, z - BODY_WIDTH / 2)

    def update_rotation(self, rotation): #here we must do some 3d rotation stuff
        pass


    def draw(self):
        self.head.draw()
        self.body.draw()
        self.left_leg.draw()
        self.right_leg.draw()
        self.left_arm.draw()
        self.right_arm.draw()

    def eventdraw(self, *args):
        self.draw()

    def eventmove(self, eventname, pos, rot):
        self.update_position(pos)
        #self.update_rotation(rot)

class EntityPlayer(Entity): #summonable class
    def on_creat(self):
        self.model = Player(self.position)

    def getName(self):
        return "minecraft:player"

    def getId(self):
        return 1

    def getRanderAble(self):
        return self.model

entityhandler.register(EntityPlayer)

import globals as G
import chat

class PlayerModel(Player): #class that is used by self-system
    def draw(self):
        if self.player.window.camerastate == 1 and self.player.gamemode != 3:
            self.head.draw()
            self.body.draw()
            self.left_leg.draw()
            self.right_leg.draw()
            self.left_arm.draw()
            self.right_arm.draw()#

    def writeToChat(self, msg):
        chat.chat.println(msg)

    def __init__(self, pos):
        Player.__init__(self, pos)
        self.inst = G.player
        self.lastpositions = []
        for e in self.getBoxModels():
            self.lastpositions.append(e.position)

    def getInst(self):
        return G.player

    def kill(self):
        G.window.kill("player fall out of the world")

    def getInventory(self):
        return [G.player.inventory.hotbar, G.player.inventory.rows, G.player.inventory.armor, G.player.inventory.crafting]

    def setPosition(self, position): #!
        for i, e in enumerate(self.getBoxModels()):
            lpos = self.lastpositions[i]
            spos = e.position
            dpos = (lpos[0]-spos[0], lpos[1]-spos[1], lpos[2]-spos[2])
            e.position = (e.position[0] - dpos[0], e.position[1] - dpos[1], e.position[2] - dpos[2])
        self.position = position

    def getBoxModels(self):
        return [self]

    def kill(self):
        G.window.kill("player fall out of world")
