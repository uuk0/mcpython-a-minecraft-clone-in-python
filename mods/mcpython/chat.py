import Item
import Blocks
import entity
from moduls import *

import pyperclip
import structures
import pickle

from pyglet.window import key

from crafting import craftinghandler

import WorldHandler

from Inventorys.Inventory import handler as invhandler

from mathhelper import *

from constans import *

import WorldSaver
import config

import crafting

from EventHandler import eventhandler

import pyglet.window.key
import globals as G
import entity
import math
import random

import states

import Commands.Command

KeyToValue = {key.A:"a", key.B:"b", key.C:"c", key.D:"d", key.E:"e", key.F:"f", key.G:"g", key.H:"h", key.I:"i",
              key.J:"j", key.K:"k", key.L:"l", key.M:"m", key.N:"n", key.O:"o", key.P:"p", key.Q:"q", key.R:"r",
              key.S:"s", key.T:"t", key.U:"u", key.V:"v", key.W:"w", key.X:"x", key.Y:"y", key.Z:"z", key._0:"0",
              key._1:"1", key._2:"2", key._3:"3", key._4:"4", key._5:"5", key._6:"6", key._7:"7", key._8:"8",
              key._9:"9", key.COMMA:",", key.MINUS:"-", key.PLUS:"+", key.SPACE:" ", key.PLUS:"+", key.MINUS:"-",
              46:".", 35:"#", 60:"<", 949187772416:"´", 940597837824:"ß"}

Upper = {"1":"!", "2":"\"", "3":"§", "4":"$", "5":"%", "6":"&", "7":"/",
         "8":"(", "9":")", "0":"=", "+":"*", "-":"_", ",":";", ".":":",
         "#":"'", "<":">", "´":"`", "ß":"?"}

AltGr = {"2":"²", "3":"³", "7":"{", "8":"[", "9":"]", "0":"}", "q":"@", "e":"€", "m":"µ", "+":"~",
         "<":"|"}

def register():
    Commands.Command.register()

class chat:
    def __init__(self):
        self.chat = []
        self.opened = False
        self.window = None
        self.chattext = ""
        self.commandhistory = []
        self.commandhistoryindex = -1

    def println(self, msg):
        self.chat.append(msg)
        if len(self.chat) > 100:
            chat.pop(0)
        print("[CHAT] "+str(msg))

    def warn(self, msg):
        print("[CHAT/WARNING] "+msg)

    def open(self):
        self.opened = True

    def addKey(self, symbol, mod):
        if symbol == key.BACKSPACE:
            self.chattext = self.chattext[:-1]
        elif symbol == key.ENTER:
            self.execute(self.chattext, G.window.position, G.player.model)
            self.chattext = ""
            self.opened = False
            self.commandhistory.append(self.chattext)
            G.window.set_menu("minecraft:game")
        elif mod & key.MOD_CTRL and symbol == key.C:
            pyperclip.copy(self.chattext)
            print("copiing...")
        elif mod & key.MOD_CTRL and symbol == key.V:
            self.chattext += pyperclip.paste()
            print("pasting....")
        elif symbol in KeyToValue.keys():
            value = KeyToValue[symbol]
            if mod & key.MOD_SHIFT:
                if value in Upper.keys():
                    value = Upper[value]
                else:
                    value = value.upper()
            elif mod & key.MOD_CTRL:
                value = AltGr[value]
            self.chattext += value
        else:
            f = open("./exceptions.txt", mode="a")
            f.write("\nunknown key found: "+str(symbol)+":"+str(mod)+"\n")
            f.close()

    def draw(self):
        self.window.chatlabel.text = self.chattext
        self.window.chatlabel.draw()

    def execute(self, msg, pos, entity):
        if not Commands.Command.handler.parse(msg, entity, pos, self):
            self.println(msg)
        return
        splitted = msg.split(" ")
        #fehlt: datapack, function, locate, reload, scoreboard, me, say, tellraw, advancement, bossbar, data, effect, enchant, execute, experience, particel, playsound, recipi, scoreboard, spreadplayers, stopsound, tag, team, title, trigger, xp, clone,

chat = chat()
