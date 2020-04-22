#from Blocks import *
#blockhandler = handler
import Blocks
#from Item import *
#itemhandler = handler
from oredictnames import *
import Inventorys
import json
import os
import globals as G
import Item.Item as Item
import config
import exceptionhandler

class Grid:
    crafting_1x1 = "mcpython:interfaceses:crafting:1x1"
    crafting_2x2 = "mcpython:interfaceses:crafting:2x2"
    crafting_2x1 = "mcpython:interfaceses:crafting:2x1"
    crafting_1x2 = "mcpython:interfaceses:crafting:1x2"
    crafting_3x3 = "mcpython:interfaceses:crafting:3x3"
    crafting_3x2 = "mcpython:interfaceses:crafting:3x2"
    crafting_3x1 = "mcpython:interfaceses:crafting:3x1"
    crafting_2x3 = "mcpython:interfaceses:crafting:2x3"
    crafting_1x3 = "mcpython:interfaceses:crafting:1x3"
    crafting_shapeless = "mcpython:interfaceses:crafting:shapeless"
    crafting_smelting = "mcpython:interfaceses:smelting:1to1"
    crafting_brewing  = "mcpython:interfaceses:magic:brewing"

class Recipi:
    def __init__(self, grid, input, output, inputamount, outputamount, *args, **kwargs):
        self.grid = grid
        self.input = input
        self.inputamount = inputamount
        self.output = output
        self.outputamount = outputamount
        self.args = args
        self.kwargs = kwargs

        craftinghandler.register(self)

class craftinghandler:
    def __init__(self):
        self.recipis = {}
        for e in Grid.__dict__.values():
            self.recipis[e] = []
        self.nrecipi = None
        self.nrecipislots = []

    def register(self, recipi):
        if not recipi.grid in self.recipis.keys():
            print("[ERROR] try to register a recipi in an unknown grid")
        self.recipis[recipi.grid].append(recipi)

    def check_player(self, player):
        self.updateOutput_player(player)

    def removeOutput_player(self, player):
        if not self.nrecipi:
            print("[ERROR] during removing output: no recipi found")
            return
        if self.nrecipi.grid == Grid.crafting_1x1:
            player.inventory.crafting.slots[self.nrecipislots[0]].amount -= self.nrecipi.inputamount[0]
        elif self.nrecipi.grid == Grid.crafting_2x2:
            player.inventory.crafting.slots[self.nrecipislots[0]].amount -= self.nrecipi.inputamount[0]
            player.inventory.crafting.slots[self.nrecipislots[1]].amount -= self.nrecipi.inputamount[1]
            player.inventory.crafting.slots[self.nrecipislots[2]].amount -= self.nrecipi.inputamount[2]
            player.inventory.crafting.slots[self.nrecipislots[3]].amount -= self.nrecipi.inputamount[3]
        elif self.nrecipi.grid == Grid.crafting_1x2 or self.nrecipi.grid == Grid.crafting_2x1:
            Inventorys.handler.inventoryslotsinst[self.nrecipislots[0]].amount -= self.nrecipi.inputamount[0]
            Inventorys.handler.inventoryslotsinst[self.nrecipislots[1]].amount -= self.nrecipi.inputamount[1]
        else:
            for i, e in enumerate(self.nrecipislots):
                e.amount -= self.nrecipi.inputamount[i]

    
    def updateOutput_player(self, player):
        inv = player.inventory.crafting
        for c in self.recipis[Grid.crafting_1x1]:
            for i, s in enumerate(inv.slots[:4]):
                if (s.item and s.item.getName() == c.input[0] and s.amount >= c.inputamount[0]) or (c.input[0] == None and not s.item):
                    flag = True
                    for s1 in inv.slots[:i] + inv.slots[i+1:4]:
                        if s1.item:
                            flag = False
                    if flag:
                        self.nrecipi = c
                        self.nrecipislots = [i]
                        inv.slots[4].setItem(c.output[0])
                        inv.slots[4].amount = c.outputamount[0]
                        return
        for c in self.recipis[Grid.crafting_2x2]:
            flag = True
            for i, s in enumerate(inv.slots[:4]):
                if not (s.item and s.item.getName() == c.input[i] and s.amount >= c.inputamount[i]):
                    if not s.item or not c.input[i] in s.item.getOreDictNames():
                        flag = False
            if flag:
                self.nrecipi = c
                self.nrecipislots = [0, 1, 2, 3]
                inv.slots[4].setItem(c.output[0])
                inv.slots[4].amount = c.outputamount[0]
                return
        for c in self.recipis[Grid.crafting_2x1]:
            for sl in [inv.slots[:2], inv.slots[2:]]:
                flag = True
                for i, s in sl:
                    if not (s.item and s.item.getName() == c.input[i] and s.amount >= c.inputamount[i]):
                        if not s.item or not c.input[i] in s.item.getOreDictNames():
                            flag = False
                if flag:
                    self.nrecipi = c
                    self.nrecipislots = [sl[0].id, sl[1].id]
                    inv.slots[4].setItem(c.output[0])
                    inv.slots[4].amount = c.outputamount[0]
                    return
        for c in self.recipis[Grid.crafting_1x2]:
            sll = [[inv.slots[0], inv.slots[2]], [inv.slots[1], inv.slots[3]]]
            for si in (0, 1):
                sl = sll[si]
                flag = True
                for i, s in enumerate(sl):
                    if not (s.item and s.item.getName() == c.input[i] and s.amount >= c.inputamount[i]):
                        if not s.item or not c.input[i] in s.item.getOreDictNames():
                            flag = False
                if flag:
                    self.nrecipi = c
                    self.nrecipislots = [sl[0].id, sl[1].id]
                    inv.slots[4].setItem(c.output[0])
                    inv.slots[4].amount = c.outputamount[0]
                    return
        items = []
        itemnames = {}
        a = inv.slots[:4]
        for i, e in enumerate(a):
            if e.item:
                items.append(e)
                if not e.item.getName() in itemnames:
                    itemnames[e.item.getName()] = []
                itemnames[e.item.getName()].append(e)
        for c in self.recipis[Grid.crafting_shapeless]:
            rclist = itemnames.copy()
            if len(c.input) <= 4 and len(c.input) == len(items):
                flag = True
                for i, e in enumerate(c.input):
                    if not e in rclist.keys():
                        flag = False
                    elif len(rclist[e]) == 0:
                        flag = False
                    else:
                        rclist[e].pop(0)
                if flag:
                    rcitems = []
                    for e in items:
                        flag = True
                        for rc in rclist.keys():
                            if e in rclist[rc]:
                                flag = False
                        if flag:
                            rcitems.append(e)
                    self.nrecipi = c
                    self.nrecipislots = rcitems
                    inv.slots[4].setItem(c.output[0])
                    inv.slots[4].amount = c.outputamount[0]
                    return

        self.nrecipi = None
        self.nrecipislots = []
        inv.slots[4].setItem(None)

craftinghandler = craftinghandler()

def loadRecipi(file):
    filename = file
    unknown_items = []
    try:
        with open(file, "r") as file:
            data = json.load(file)
        t = data["type"]
        if t == "crafting_shapeless":
            _items = data['ingredients']
            items = []
            itemamount = []
            for e in _items:
                try:
                    items.append(e["item"] if "item" in e else (e["tag"]))
                    if "tag" in e and config.CONFIGS["PRINT_CRAFTINGRECIPIS_DEBUG"]:
                        print("[CRAFTING/LOADER] found oredict-notation", e["tag"])
                    itemamount.append(e["count"] if "count" in e else 1)
                    item = e["item"] if "item" in e else None
                    if item and not item in Item.handler.nametoitem.keys() and not item in unknown_items:
                        unknown_items.append(item)
                except:
                    if config.CONFIGS["PRINT_CRAFTINGRECIPIS_DEBUG"]:
                        print("error_reson", "\n", e, "\n", data, "\n", file)
                        raise
                    else:
                        exceptionhandler.addTraceback(False)
            _result = data['result']
            result = []
            resultamount = []
            for e in [_result]:
                result.append(e["item"])
                resultamount.append(e["count"] if "count" in e else 1)
            Recipi(Grid.crafting_shapeless, items, result, itemamount, resultamount)

        elif t == "crafting_shaped":
            pattern = data["pattern"]
            recipinames = []
            recipiamount = []
            keys = data["key"]
            _result = data["result"]
            #print(pattern, keys, file)
            for key in keys:
                item = keys[key]["item"] if "item" in keys[key] else keys[key]["tag"]
                amount = keys[key]["count"] if "count" in keys[key] else 1
                for i1 in range(len(pattern)):
                    for i2 in range(len(pattern[0])):
                        if pattern[i1][i2] == key:
                            recipinames.append([item])
                            if not item in Item.handler.nametoitem.keys() and not item in unknown_items:
                                unknown_items.append(item)
                            recipiamount.append([amount])
            result = []
            resultamount = []
            for e in [_result]:
                result.append(e["item"])
                resultamount.append(e["count"] if "count" in e else 1)
            if len(pattern) == 1:
                if len(pattern[0]) == 1:
                    Recipi(Grid.crafting_1x1, recipinames, result, recipiamount, resultamount)
                elif len(pattern[0]) == 2:
                    Recipi(Grid.crafting_2x1, recipinames, result, recipiamount, resultamount)
                elif len(pattern[0]) == 3:
                    Recipi(Grid.crafting_3x1, recipinames, result, recipiamount, resultamount)
            elif len(pattern) == 2:
                if len(pattern[0]) == 1:
                    Recipi(Grid.crafting_1x2, recipinames, result, recipiamount, resultamount)
                elif len(pattern[0]) == 2:
                    Recipi(Grid.crafting_2x2, recipinames, result, recipiamount, resultamount)
                elif len(pattern[0]) == 3:
                    Recipi(Grid.crafting_3x2, recipinames, result, recipiamount, resultamount)
            elif len(pattern) == 3:
                if len(pattern[0]) == 1:
                    Recipi(Grid.crafting_1x3, recipinames, result, recipiamount, resultamount)
                elif len(pattern[0]) == 2:
                    Recipi(Grid.crafting_2x3, recipinames, result, recipiamount, resultamount)
                elif len(pattern[0]) == 3:
                    Recipi(Grid.crafting_3x3, recipinames, result, recipiamount, resultamount)

        elif config.CONFIGS["PRINT_CRAFTINGRECIPIS_DEBUG"]:
            print("unknow recipi type:", t)
    except:
        if config.CONFIGS["PRINT_CRAFTINGRECIPIS_DEBUG"]:
            print("can't load recipi", filename)
        exceptionhandler.addTraceback(False)
    if len(unknown_items) > 0 and config.CONFIGS["PRINT_CRAFTINGRECIPIS_DEBUG"]:
        print("can't find the following items in registry that are used in these recipi:")
        print(unknown_items)


for f in os.listdir(G.local+"/assets/recipes"):
    loadRecipi(G.local+"/assets/recipes/"+f)


