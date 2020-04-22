import globals as G
import pyglet
import texturGroups
from mathhelper import *
from moduls import *
from chat import *
import config
from oredictnames import OreDict
import Item.Item as Item, Blocks.Block as Blocks
import WorldSaver
import WorldHandler
import lootchest
import TickHandler

class StateHandler:
    def __init__(self):
        self.instances = {}
        self.classes = {}
        self.subinst = {}
        self.subclass = {}
        self.activates = None

    def register(self, c):
        obj = c()
        if issubclass(c, State):
            self.instances[obj.getName()] = obj
            self.classes[obj.getName()] = c
        else:
            self.subinst[obj.getName()] = obj
            self.subclass[obj.getName()] = c

    def activate(self, name):
        if not name in self.instances:
            raise ValueError("unsupported state: "+str(name))
        if self.activates:
            dep1 = set(self.activates.getDependencies())
            self.activates.deactivate()
        else:
            dep1 = set([])
        self.activates = self.instances[name]
        dep2 = set(self.activates.getDependencies())
        toadd = dep2 - dep1
        toremove = dep1 - dep2
        for e in list(toadd):
            self.subinst[e].activate()
        for e in list(toremove):
            self.subinst[e].deactivate()
        self.instances[name].activate()


handler = StateHandler()
G.statehandler = handler

class State:
    def __init__(self):
        self.activ = False
        self.events = []

    def getName(self):
        return "minecraft:none"

    def activate(self):
        pass

    def deactivate(self):
        for e in self.events:
            EventHandler.eventhandler.unregister_on_event(e)

    def getDependencies(self):
        return []

G.State = State

class TileState:
    def __init__(self):
        self.activ = False
        self.events = []

    def getName(self):
        return "minecraft:tilestate:none"

    def activate(self):
        pass

    def deactivate(self):
        for e in self.events:
            EventHandler.eventhandler.unregister_on_event(e)

G.TileState = TileState

#from Inventorys import *
invhandler = G.inventoryhandler

import EventHandler

handler = G.statehandler

class TileStateWorldModel(TileState):
    def getName(self):
        return "minecraft:tilestate:world:model"

    def activate(self):
        self.events.append(EventHandler.eventhandler.on_event("on_draw_3D", self.draw3d))

    def draw3d(self, *args):
        G.model.batch.draw()

handler.register(TileStateWorldModel)

class TileStateOptionBackground(TileState):
    def __init__(self):
        TileState.__init__(self)

        self.picture = pyglet.sprite.Sprite(texturGroups.handler.groups["./assets/textures/gui/options_background.png"])

    def getName(self):
        return "minecraft:tilestate:options:background"

    def activate(self):
        self.events.append(EventHandler.eventhandler.on_event("on_draw_2D", self.draw2d))

    def draw2d(self, *args):
        self.picture.draw()

handler.register(TileStateOptionBackground)

class TileStateMouseExternal(TileState):
    def __init__(self):
        TileState.__init__(self)
        self.picture = pyglet.sprite.Sprite(texturGroups.handler.groups["./assets/textures/gui/mousetrigger.png"])

    def getName(self):
        return "minecraft:tilestate:mouseexternal"

    def activate(self):
        self.events.append(EventHandler.eventhandler.on_event("on_draw_2D", self.draw2d))
        self.events.append(EventHandler.eventhandler.on_event("on_mouse_press", self.key_press))

    def draw2d(self, *args):
        if config.CONFIGS["ALTERNATIVMOUSE"]:
            self.picture.draw()

    def key_press(self, eventname, symbol, modifiers, *args):
        if config.CONFIGS["ALTERNATIVMOUSE"]:
            if symbol == key.UP:
                self.picture.y += 10
            elif symbol == key.DOWN:
                self.picture.y -= 10
            elif symbol == key.RIGHT:
                self.picture.x += 10
            elif symbol == key.LEFT:
                self.picture.x -= 10
            elif symbol == key.P:
                EventHandler.eventhandler.call("on_mouse_press", self.picture.x, self.picture.y - 140, mouse.left, None)

handler.register(TileStateMouseExternal)

class Game(State):
    def __init__(self):
        State.__init__(self)
        # The label that is displayed in the top left of the canvas.
        #[800, 600]
        self.label = pyglet.text.Label('', font_name='Arial', font_size=18,
                                       x=10, y=800 - 10, anchor_x='left', anchor_y='top',
                                       color=(0, 0, 0, 255))

        self.label2 = pyglet.text.Label('', font_name='Arial', font_size=18,
                                        x=10, y=600 - 30, anchor_x='left', anchor_y='top',
                                        color=(0, 0, 0, 255))
        self.reticle = None
        self.resize(None, 0, 0, config.CONFIGS["DEFAULT_WINDOW_SIZE"][0], config.CONFIGS["DEFAULT_WINDOW_SIZE"][1])

    def getName(self):
        return "minecraft:game"

    def activate(self):
        self.events.append(EventHandler.eventhandler.on_event("on_draw_3D", self.draw3d))
        self.events.append(EventHandler.eventhandler.on_event("on_draw_2D", self.draw2d))
        self.events.append(EventHandler.eventhandler.on_event("on_resize", self.resize))
        self.events.append(EventHandler.eventhandler.on_event("on_key_press", self.key_press))
        self.events.append(EventHandler.eventhandler.on_event("on_key_release", self.key_releas))
        self.events.append(EventHandler.eventhandler.on_event("on_mouse_motion", self.mouse_motion))
        self.events.append(EventHandler.eventhandler.on_event("on_mouse_press", self.mouse_press))
        G.window.set_exclusive_mouse(True)

    def getDependencies(self):
        return ["minecraft:tilestate:world:model"]

    def draw3d(self, *args):
        #self.draw_focused_block()
        """ Draw black edges around the block that is currently under the
                crosshairs.

                """
        vector = G.window.get_sight_vector()
        block = G.model.hit_test(G.window.position, vector)[0]
        if block:
            x, y, z = block
            vertex_data = cube_vertices(x, y, z, 0.51)
            glColor3d(0, 0, 0)
            glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
            pyglet.graphics.draw(24, GL_QUADS, ('v3f/static', vertex_data))
            glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

    def draw2d(self, *args):
        """ Draw the label in the top left of the screen.

                """
        x, y, z = G.window.position
        text = ""
        if config.CONFIGS["SHOW_FPS"]:
            text += str(round(pyglet.clock.get_fps())) + " "
        if config.CONFIGS["SHOW_KOORDINATES"]:
            text += str((round(x), round(y), round(z))) + " "
        if config.CONFIGS["SHOW_WORLDSIZE"]:
            text += str(len(G.model._shown)) + "/" + str(len(G.model.world)) + " "
        if (round(x), round(z)) in G.player.dimension.biomedata:
            text += "biom: " + G.player.dimension.biomeinst[
                G.player.dimension.biomedata[(round(x), round(z))]].getName()
        self.label.text = text
        self.label.draw()
        vector = G.window.get_sight_vector()
        block = G.model.hit_test(G.window.position, vector)[0]
        if block and config.CONFIGS["SHOW_BLOCK_LOOKING_AT"]:
            self.label2.text = "You are looking at " + G.model.world[block].getVisualName() + (
                str(block) if config.CONFIGS["SHOW_BLOCK_POS_LOOKING_AT"] else "")
            self.label2.draw()

        glColor3d(0, 0, 0)
        if self.reticle: self.reticle.draw(GL_LINES)
        #G.inventoryhandler.draw()
        import chat
        chat.chat.draw()
        G.player.hartholder.draw()

    def resize(self, eventname, dx, dy, x, y):
        if self.reticle:
            self.reticle.delete()
        x, y = x // 2, y // 2
        n = 10
        self.reticle = pyglet.graphics.vertex_list(4,
            ('v2i', (x - n, y, x + n, y, x, y - n, x, y + n))
        )
        self.label.y -= dy / 2
        self.label2.y -= dy / 2

    def key_press(self, eventname, symbol, modifiers):
        import chat
        chat = chat.chat
        if symbol == config.CONFIGS["init"]["KEYBINDS"]['forward:key']:
            G.window.strafe[0] -= 1
        elif symbol == config.CONFIGS["init"]["KEYBINDS"]['backward:key']:
            G.window.strafe[0] += 1
        elif symbol == config.CONFIGS["init"]["KEYBINDS"]['left:key']:
            G.window.strafe[1] -= 1
        elif symbol == config.CONFIGS["init"]["KEYBINDS"]['right:key']:
            G.window.strafe[1] += 1
        elif symbol == config.CONFIGS["init"]["KEYBINDS"]['jump:key']:
            if G.window.dy == 0:
                G.window.dy = JUMP_SPEED
        elif symbol == config.CONFIGS["init"]["KEYBINDS"]['escape:key']:
            if G.player.mode == 1 and len(G.inventoryhandler.shown) <= 1:
                G.window.set_exclusive_mouse(False)
            elif len(invhandler.shown) <= 1:
                if G.player.inventory.moving_slot and G.player.inventory.moving_start:
                    G.player.inventory.moving_slot.setPos(*G.player.inventory.moving_start)
                    G.player.inventory.moving_slot = None
                G.player.mode = 1
                G.window.set_exclusive_mouse(True)
                for i in range(0, 4):
                    invhandler.hide(i)
                for e in invhandler.shown:
                    if invhandler.inventoryinst[e].getId() == 4:
                        invhandler.hide(e)
                invhandler.show(0)
            G.window.set_menü("minecraft:esc")

        elif symbol == config.CONFIGS["init"]["KEYBINDS"]['togleflying:key'] and G.player.gamemode == 1:
            G.window.flying = not G.window.flying
        elif symbol in G.window.num_keys:
            index = G.window.num_keys.index(symbol)
            G.window.hotbarelement = index
            if G.window.braking_start: G.window.braking_start = time.time()
        elif symbol == config.CONFIGS["init"]["KEYBINDS"]['openchat:key']:
            chat.open()
            G.window.set_menü("minecraft:chat")
        elif symbol == config.CONFIGS["init"]["KEYBINDS"]['openinventory:key']:
            for i in range(0, 4):
                G.inventoryhandler.show(i)
            G.window.set_menü("minecraft:inventory")
        elif symbol == key.LSHIFT and (G.player.mode == 2 or G.player.mode == 3):
            G.player.inventory.on_shift()
        elif symbol == config.CONFIGS["init"]["KEYBINDS"]['movecamera:key'][0] and config.CONFIGS["ALLOW_CAMERA_MOVING_WITH_ARROWS"]:
            G.window.turning_strafe[1] = 1
        elif symbol == config.CONFIGS["init"]["KEYBINDS"]['movecamera:key'][1] and config.CONFIGS["ALLOW_CAMERA_MOVING_WITH_ARROWS"]:
            G.window.turning_strafe[1] = -1
        elif symbol == config.CONFIGS["init"]["KEYBINDS"]['movecamera:key'][3] and config.CONFIGS["ALLOW_CAMERA_MOVING_WITH_ARROWS"]:
            G.window.turning_strafe[0] = 1
        elif symbol == config.CONFIGS["init"]["KEYBINDS"]['movecamera:key'][2] and config.CONFIGS["ALLOW_CAMERA_MOVING_WITH_ARROWS"]:
            G.window.turning_strafe[0] = -1

    def key_releas(self, eventname, symbol, modifiers):
        import chat
        chat = chat.chat
        if G.window.keyEvent == "chat" and chat.opened:
            if G.window.strafe[0] != 0:
                G.window.strafe[0] = 0
            if G.window.strafe[1] != 0:
                G.window.strafe[1] = 0
            return
        if symbol == key.W:
            G.window.strafe[0] += 1
        elif symbol == key.S:
            G.window.strafe[0] -= 1
        elif symbol == key.A:
            G.window.strafe[1] += 1
        elif symbol == key.D:
            G.window.strafe[1] -= 1
        elif symbol == key.UP:
            G.window.turning_strafe[1] = None
        elif symbol == key.DOWN:
            G.window.turning_strafe[1] = None
        elif symbol == key.RIGHT:
            G.window.turning_strafe[0] = None
        elif symbol == key.LEFT:
            G.window.turning_strafe[0] = None

    def mouse_motion(self, eventname, x, y, dx, dy):
        import chat
        chat = chat.chat
        if G.player.inventory.moving_slot:
            if G.player.inventory.moving_slot:
                G.player.inventory.moving_slot.setPos(x + dx, y + dy)
            return
        G.window.mousepos = (x, y)
        if G.window.keyEvent == "chat" and chat.opened:
            return
        if G.window.exclusive:
            m = 0.15 * config.CONFIGS["MOUSESENSITIV"]
            x, y = G.window.rotation
            x, y = x + dx * m, y + dy * m
            y = max(-90, min(90, y))
            G.window.rotation = (x, y)

    def mouse_press(self, eventname, x, y, button, modifiers):
        import chat
        chat = chat.chat
        if chat.opened:
            return
        if G.window.exclusive and G.player.gamemode != 3 and G.player.gamemode != 2:
            vector = G.window.get_sight_vector()
            block, previous = G.model.hit_test(G.window.position, vector)
            if (button == mouse.RIGHT) or \
                    ((button == mouse.LEFT) and (modifiers & key.MOD_CTRL)):
                if block and G.model.world[block].hasInventory() and (not G.player.inventory.hotbar.slots[G.window.hotbarelement].item or (G.player.inventory.hotbar.slots[G.window.hotbarelement].item and not OreDict.ORE_DROP in G.player.inventory.hotbar.slots[G.hotbarelement].item.getOreDictNames() and not (modifiers & key.MOD_SHIFT))):
                    invhandler.show(G.model.world[block].getInventoryID())
                    handler.activate(invhandler.inventoryinst[G.model.world[block].getInventoryID()].eventname)
                    print(G.model.world[block].getInventorys()[0].eventname,
                          invhandler.inventoryinst[G.model.world[block].getInventoryID()])
                    print("showing inventory", G.model.world[block].getInventorys())
                elif G.player.inventory.hotbar.slots[G.window.hotbarelement].item and OreDict.ORE_DROP in G.player.inventory.hotbar.slots[G.window.hotbarelement].item.getOreDictNames() and block and G.model.world[block].getName() == "minecraft:stone":
                    G.model.add_block(block, "minecraft:"+G.player.inventory.hotbar.slots[G.window.hotbarelement].item.getOreMaterial()+"_ore", hitblock=previous)
                elif G.player.inventory.hotbar.slots[G.window.hotbarelement].item:
                    slot = G.player.inventory.hotbar.slots[G.window.hotbarelement]
                    if slot.item and block in G.model.world and slot.item.canInteractWith(G.model.world[block]):
                        slot.item.interactWith(G.model.world[block])
                    elif slot.item.hasBlock() and block in G.model.world and not G.model.world[block].hasInventory() and not slot.item.canInteractWith(G.model.world[block]):
                        if G.model.add_block(previous, slot.item.getBlockName(), hitblock=previous):
                            if G.player.gamemode == 0:
                                item = slot.item
                                if slot.amount == 1:
                                    slot.setItem(None)
                                else:
                                    slot.amount -= 1
                                item.on_block_set(previous)
                    else:
                        slot.item.on_right_click(block, previous, button, modifiers)
            elif button == pyglet.window.mouse.LEFT:
                if block:
                    if ((not G.player.inventory.hotbar.slots[G.window.hotbarelement].item) or G.player.inventory.hotbar.slots[G.window.hotbarelement].item.canDestroyBlock(block, button, modifiers) and G.model.world[block].isBreakAble()) or G.player.gamemode == 1:
                        G.window.braking_start = time.time()
                    else:
                        G.player.inventory.hotbar.slots[G.window.hotbarelement].item.on_left_click(G.window, block, previous, button, modifiers)
            elif button == pyglet.window.mouse.MIDDLE:
                if G.player.gamemode == 1:
                    item = Item.handler.getClass(G.model.world[block].getItemName())()
                    item.blocknbt = G.model.world[block].getAllItemNBT()
                    G.player.addToFreePlace(item)
        elif not G.window.exclusive:
            G.window.set_exclusive_mouse(True)
    
handler.register(Game)

class ChatState(State):
    def getName(self):
        return "minecraft:chat"
    
    def getDependencies(self):
        return ["minecraft:tilestate:world:model"]
    
    def activate(self):
        self.events.append(EventHandler.eventhandler.on_event("on_draw_2D", self.draw_2d))
        self.events.append(EventHandler.eventhandler.on_event("on_key_press", self.key_press))
        G.window.set_exclusive_mouse(False)
        
    def draw_2d(self, *args):
        import chat
        chat.chat.draw()
        
    def key_press(self, eventname, symbol, modifiers):
        import chat
        chat = chat.chat
        if symbol == key.ESCAPE:
            chat.opened = False
            chat.text = ""
            G.window.set_menü("minecraft:game")
        else:
            chat.addKey(symbol, modifiers)
        
handler.register(ChatState)

class DemoInfo(State):
    def __init__(self):
        State.__init__(self)
        self.demoinfosprite = pyglet.sprite.Sprite(texturGroups.handler.groups["./assets/textures/gui/demomsg.png"])
        self.demoinfosprite.x = 100
        self.demoinfosprite.y = 100
        EventHandler.eventhandler.on_event("on_resize", self.resize)
    
    def getName(self):
        return "minecraft:demo_info"

    def getDependencies(self):
        return ["minecraft:tilestate:world:model"]
    
    def activate(self):
        self.events.append(EventHandler.eventhandler.on_event("on_draw_2D", self.draw_2d))
        self.events.append(EventHandler.eventhandler.on_event("on_mouse_press", self.mouse_press))
        self.events.append(
            EventHandler.eventhandler.on_event("on_demo_info_purchase_now_clicked", self.on_demo_info_purchase_now_clicked))
        self.events.append(
            EventHandler.eventhandler.on_event("on_demo_info_continue_plaing_clicked", self.on_demo_info_continue_plaing_clicked))
        self.events.append(EventHandler.eventhandler.on_event("on_key_press", self.key_press))
        G.window.set_exclusive_mouse(False)
        
    def draw_2d(self, *args):
        self.demoinfosprite.draw()
        
    def resize(self, _, dx, dy, x, y):
        self.demoinfosprite.x -= dx / 2
        self.demoinfosprite.y -= dy / 2
        
    def mouse_press(self, eventname, x, y, button, modifiers):
        if x > 114 and x < 341 and y > 133 and y < 170:
            EventHandler.eventhandler.call("on_demo_info_purchase_now_clicked")
        elif x > 350 and x < 574 and y > 132 and y < 170:
            EventHandler.eventhandler.call("on_demo_info_continue_plaing_clicked")
        elif (modifiers & key.MOD_SHIFT):
            print(x, y)
            
    def on_demo_info_purchase_now_clicked(self):
        print("not implemented feature")
        G.window.set_menü("minecraft:game")
        
    def on_demo_info_continue_plaing_clicked(self, eventname):
        G.window.set_menü("minecraft:game")
        
    def key_press(self, eventname, symbol, mods):
        if symbol == key.ESCAPE:
            G.window.set_menü("minecraft:game")
    
handler.register(DemoInfo)    

class ESC_State(State):
    def __init__(self):
        State.__init__(self)
        self.esc_menü_back_to_gamesprite = pyglet.sprite.Sprite(
            texturGroups.handler.groups["./assets/textures/gui/optionbackground_A.png"])
        self.esc_menü_back_to_gamesprite.x = 200
        self.esc_menü_back_to_gamesprite.y = 400
        self.esc_menü_quitsprite = pyglet.sprite.Sprite(
            texturGroups.handler.groups["./assets/textures/gui/optionbackground_F.png"])
        self.esc_menü_quitsprite.x = 200
        self.esc_menü_quitsprite.y = 200
        EventHandler.eventhandler.on_event("on_resize", self.resize)
        
    def resize(self, _, dx, dy, x, y):
        self.esc_menü_back_to_gamesprite.x -= dx / 2
        self.esc_menü_back_to_gamesprite.y -= dy / 2
        self.esc_menü_quitsprite.x -= dx / 2
        self.esc_menü_quitsprite.y -= dy / 2
        
    def getName(self):
        return "minecraft:esc"

    def getDependencies(self):
        return ["minecraft:tilestate:world:model"]

    def activate(self):
        self.events.append(EventHandler.eventhandler.on_event("on_draw_2D", self.draw_2d))
        self.events.append(EventHandler.eventhandler.on_event("on_key_press", self.key_press))
        self.events.append(EventHandler.eventhandler.on_event("on_mouse_press", self.mouse_press))
        G.window.set_exclusive_mouse(False)
        
    def draw_2d(self, *args):
        self.esc_menü_quitsprite.draw()
        self.esc_menü_back_to_gamesprite.draw()
        
    def key_press(self, eventname, symbol, mods):
        if symbol == key.ESCAPE:
            G.window.set_menü("minecraft:game")
            
    def mouse_press(self, eventname, x, y, button, modifiers):
        if x > 200 and x < 595 and y > 401 and y < 437:
            G.window.set_menü("minecraft:game")
        elif x > 200 and x < 596 and y > 202 and y < 236:
            print("[INFO] saving world...")
            WorldSaver.saveWorld(G.model, G.window.worldname)
            print("[INFO] saved!")
            WorldSaver.cleanUpModel(G.model)
            G.window.set_menü("minecraft:start_menü")
        elif (modifiers & key.MOD_SHIFT):
            print(x, y)

handler.register(ESC_State)

class StartMenü(State):
    def __init__(self):
        State.__init__(self)
        self.game_start_worldselect = pyglet.sprite.Sprite(
            texturGroups.handler.groups["./assets/textures/gui/startgui_singelplayer.png"])
        self.game_start_worldselect.x = 200
        self.game_start_worldselect.y = 400
        self.game_start_quit_sprite = pyglet.sprite.Sprite(
            texturGroups.handler.groups["./assets/textures/gui/startgui_quitgame.png"])
        self.game_start_quit_sprite.x = 400
        self.game_start_quit_sprite.y = 275
        EventHandler.eventhandler.on_event("on_resize", self.resize)

    def resize(self, _, dx, dy, x, y):
        self.game_start_quit_sprite.x -= dx / 2
        self.game_start_quit_sprite.y -= dy / 2
        self.game_start_worldselect.x -= dx / 2
        self.game_start_worldselect.y -= dy / 2
    
    def getName(self):
        return "minecraft:start_menü"
    
    def getDependencies(self):
        return ["minecraft:tilestate:options:background", "minecraft:tilestate:mouseexternal"]
    
    def activate(self):
        self.events.append(EventHandler.eventhandler.on_event("on_draw_2D", self.draw_2d))
        self.events.append(EventHandler.eventhandler.on_event("on_mouse_press", self.mouse_press))
        G.window.set_exclusive_mouse(False)
        
    def draw_2d(self, *args):
        self.game_start_worldselect.draw()
        self.game_start_quit_sprite.draw()
    
    def mouse_press(self, eventname, x, y, button, modifiers):
        if x > self.game_start_worldselect.x \
                and x < self.game_start_worldselect.x + self.game_start_worldselect.image.width \
                and y > self.game_start_worldselect.y \
                and y < self.game_start_worldselect.y + self.game_start_worldselect.image.height:
            G.window.set_menü("minecraft:world_select")
        elif x > self.game_start_quit_sprite.x \
                and x < self.game_start_quit_sprite.x + self.game_start_quit_sprite.image.width \
                and y > self.game_start_quit_sprite.y \
                and y < self.game_start_quit_sprite.y + self.game_start_quit_sprite.image.height:
            G.window.close()
        elif (modifiers & key.MOD_SHIFT):
            print(x, y)
            
handler.register(StartMenü)

class Loading(State):
    def getDependencies(self):
        return ["minecraft:tilestate:options:background"]
    
    def getName(self):
        return "minecraft:loading"
    
handler.register(Loading)

class Inventory(State):
    def getName(self):
        return "minecraft:inventory"
    
    def getDependencies(self):
        return ["minecraft:tilestate:world:model", "minecraft:tilestate:mouseexternal"]
    
    def activate(self):
        for i in range(4): G.inventoryhandler.show(i)
        G.window.set_exclusive_mouse(False)
        
    def key_press(self, eventname, symbol, mods):
        if symbol == key.ESCAPE or symbol == key.E:
            G.window.set_menü("minecraft:game")

    def deactivate(self):
        for i in range(4): G.inventoryhandler.hide(i)
                
handler.register(Inventory)

class WorldSelect(State):
    def __init__(self):
        State.__init__(self)
        self.world_select_creat_new_sprite = pyglet.sprite.Sprite(
            texturGroups.handler.groups["./assets/textures/gui/worldselect_creat_new.png"])
        self.world_select_creat_new_sprite.x = 400
        self.world_select_creat_new_sprite.y = 80
        self.world_select_canceled_sprite = pyglet.sprite.Sprite(
            texturGroups.handler.groups["./assets/textures/gui/worldselect_cancel.png"])
        self.world_select_canceled_sprite.x = 400
        self.world_select_canceled_sprite.y = 40
        EventHandler.eventhandler.on_event("on_resize", self.resize)
        self.lastselect = time.time() - 10

    def resize(self, _, dx, dy, x, y):
        self.world_select_canceled_sprite.x -= dx / 2
        self.world_select_canceled_sprite.y -= dy / 2
        self.world_select_creat_new_sprite.x -= dx / 2
        self.world_select_creat_new_sprite.y -= dy / 2

    def getDependencies(self):
        return ["minecraft:tilestate:options:background", "minecraft:tilestate:mouseexternal"]
    
    def getName(self):
        return "minecraft:world_select"
    
    def activate(self):
        self.events.append(EventHandler.eventhandler.on_event("on_draw_2D", self.draw_2d))
        self.events.append(EventHandler.eventhandler.on_event("on_mouse_press", self.mouse_press))
        G.window.set_exclusive_mouse(False)

    def draw_2d(self, *args):
        self.world_select_creat_new_sprite.draw()
        self.world_select_canceled_sprite.draw()

    def mouse_press(self, eventname, x, y, button, modifiers):
        if x > self.world_select_creat_new_sprite.x \
                and x <  self.world_select_creat_new_sprite.x + self.world_select_creat_new_sprite.image.width \
                and y > self.world_select_creat_new_sprite.y \
                and y < self.world_select_creat_new_sprite.y + self.world_select_creat_new_sprite.image.height:
            G.window.set_menü("minecraft:loading")
            #TickHandler.handler.run(self.generate, 2)
            self.generate()
        elif x > self.world_select_canceled_sprite.x \
                and x < self.world_select_canceled_sprite.image.width \
                and y > self.world_select_canceled_sprite.y \
                and y < self.world_select_canceled_sprite.y + self.world_select_canceled_sprite.image.height:
            self.set_menü("start_menü")
        elif (modifiers & key.MOD_SHIFT):
            print(x, y)

    def generate(self):
        if time.time() - self.lastselect < 10:
            G.window.set_menü("minecraft:game")
            raise ValueError()
            return
        WorldSaver.cleanUpModel(G.model)
        G.window.set_exclusive_mouse(False)
        self.seed = random.randint(-1000, 1000)
        G.seed = self.seed
        G.random.setSeed(self.seed)
        G.player.gamemode = int(input("gamemode: "))
        G.window.worldname = str(input("woldname: "))
        enableBaseChest = str(input("Base chest? (1/0): "))
        G.window.world = WorldHandler.World(G.model, G.window.seed, "1", [])
        for x in range(-2, 3):
            for z in range(-2, 3):
                print("generating", x, z)
                G.window.world.generateChunk(x, z)
        WorldSaver.saveWorld(G.model, G.window.worldname)
        G.model.change_sectors(None, sectorize(G.window.position))
        y = 200
        x, z = G.window.world.spawnpoint
        while (x, y, z) in G.model.world:
            y += 1
        G.window.world.spawnpoint = (x, y, z)
        G.window.startpos = (x, y, z)
        G.window.position = (x, y, z)
        if enableBaseChest == "1":
            print("generating base chest")
            chest = lootchest.StartChest()
            chest.past((x, y - 1, z))
        if config.CONFIGS["init"]["GAMETYPE"] != "gametype:full":
            G.window.set_menü("minecraft:demo_info")
        else:
            G.window.set_menü("minecraft:game")

        self.demostarttime = time.time()
        self.lastselect = time.time()

handler.register(WorldSelect)