import traceback
import sys
import time
import config
import globals as G
import exceptionhandler

class EventHandler:
    def __init__(self):
        self.events = {}
        self.functions = {}
        self.idtoevent = {}
        self.nextid = 0
        self.callfunctions = []

    def update(self, dt=None):
        functions = []
        if len(self.callfunctions) <= 100:
            functions = self.callfunctions[:]
            self.callfunctions = []
        else:
            functions = self.callfunctions[:100]
            self.callfunctions = self.callfunctions[100:]
        for f in functions:
            try:
                self.functions[f[0]](*f[2])
            except:
                exceptionhandler.addTraceback()

    def register(self, name):
        if not name in self.events:
            self.events[name] = []
        else:
            print("[EVENTHANDLER/WARN] try to add an known event", name)

    def on_event(self, name, funk):
        if not name in self.events:
            print("[EVENTHANDLER/ERROR] try to add an callback for an unknown event", name)
            return
        id = self.nextid
        self.nextid += 1
        self.events[name].append(id)
        self.functions[id] = funk
        self.idtoevent[id] = name
        return id

    def unregister_on_event(self, id):
        if not id in self.idtoevent:
            print("[EVENTHANDLER/ERROR] try to unregister an unknown function", id)
            return
        event = self.idtoevent[id]
        del self.idtoevent[id]
        del self.functions[id]
        self.events[event].remove(id)
        return

    def call(self, name, *args, instant=False):
        if not name in self.events:
            print("[EVENTHANDLER/ERROR] try to call an unknown event")
            return
        if not instant:
            for f in self.events[name]:
                self.callfunctions.append([f, name, [name]+list(args)])
        else:
            for f in self.events[name]:
                try:
                    self.functions[f](*[name]+list(args))
                except:
                    exceptionhandler.addTraceback()

    def event(self, *args):
        self.on_event(args[0].__name__, args[0])
        return args[0]

eventhandler = EventHandler()
eventhandler.register("on_game_inited")
eventhandler.register("on_game_started")
eventhandler.register("on_command_executed")
eventhandler.register("on_unknown_command_executed")
eventhandler.register("on_game_crash")
eventhandler.register("on_draw_3D")
eventhandler.register("on_draw_2D")
eventhandler.register("on_key_press")
eventhandler.register("on_key_release")
eventhandler.register("on_mouse_motion")
eventhandler.register("on_mouse_press")
eventhandler.register("on_demo_info_purchase_now_clicked")
eventhandler.register("on_demo_info_continue_plaing_clicked")
eventhandler.register("on_esc_menü_back_to_game_clicked")
eventhandler.register("on_player_move")
eventhandler.register("on_model_cleaned_start")
eventhandler.register("on_model_cleaned_end")
eventhandler.register("on_chunk_generate")
eventhandler.register("on_resize")

def command_fail(*args):
    print("[CHAT][ERROR] unknown command", args)

eventhandler.on_event("on_unknown_command_executed", command_fail)
