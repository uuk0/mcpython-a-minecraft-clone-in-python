import threading
from time import *
import globals as G


class TickHandler:
    def __init__(self):
        self.ticks = [[]] * 100
        self.nextupdate = time() + 1

    def _run(self, dt):
        if (
            G.player
            and G.window
            and (G.window.keyEvent == "esc_menü" or G.window.keyEvent == "start_menü")
        ):
            return
        self.nextupdate += 1
        data = self.ticks.pop(0)
        self.ticks.append([])
        for f in data:
            try:
                f[0](*f[1], **f[2])
            except:
                print(f)
                raise

    def run(self, funk, tick, args=[], kwargs={}):
        self.ticks[tick].append([funk, args, kwargs])


handler = TickHandler()
