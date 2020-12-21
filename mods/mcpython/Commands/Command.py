import config
import math
import globals as G
import random


class CommandHandler:
    def __init__(self):
        self.commands = []

    def register(self, klass):
        self.commands.append(klass)

    def parse(self, line, entity, position, chat):
        possible = []
        for c in self.commands:
            if c.isCommand(line):
                possible.append(c)
        print(possible)
        if len(possible) == 0:
            return False
        exceptions = []
        for e in possible:
            ex = e.getSyntaxError(line, entity, position, chat)
            if ex:
                exceptions.append(ex)
                possible.remove(e)
        if len(possible) == 0:
            print("[COMMAND/ERROR] can't find command parseable. exceptions:")
            for e in exceptions:
                for ex in e:
                    print(ex)
            return True
        elif len(possible) > 1:
            print("[COMMAND/ERROR] can't find ONE command. possible:", possible)
            return True
        else:
            possible[0].parse(line, entity, position, chat)
            return True


handler = CommandHandler()

"""Not added:
/debug, """


class Command:
    @staticmethod
    def isCommand(line):
        return False

    @staticmethod
    def getSyntaxError(line, entity, position, chat):
        return None

    @staticmethod
    def parse(line, entity, position, chat):
        pass

    @staticmethod
    def getHelp():
        return ""


PlayerRegister = {}


def register():
    PlayerRegister = {config.CONFIGS["PLAYER_NAME"]: G.player.model}


def getSelector(text, pos, entity):
    if text in PlayerRegister:
        return PlayerRegister[text]
    elif text == "@s":
        return [entity]
    elif text == "@p":
        n = [None, None]
        for e in PlayerRegister.values():
            dx = e.position[0] - pos[0]
            dy = e.position[1] - pos[1]
            dz = e.position[2] - pos[2]
            if dx < 0:
                dx = -dx
            if dy < 0:
                dy = -dy
            if dz < 0:
                dz = -dz
            d = math.sqrt(dx * dx + dy * dy + dz * dz)
            if n[0] == None or d < n[0]:
                n = [d, e]
        if n == [None, None]:
            return []
        return n[1]
    elif text == "@a":
        return PlayerRegister.values()
    elif text == "@r":
        return random.choice(PlayerRegister.values())
    else:
        return []


def getPosition(x, y, z, pos, entity):
    if x == "~":
        x = pos[0]
    elif getSelector(x, pos, entity) != []:
        x = getSelector(x, pos, entity)[0].position[0]
    if y == "~":
        y = pos[0]
    elif getSelector(y, pos, entity) != []:
        y = getSelector(x, pos, entity)[0].position[1]
    if z == "~":
        z = pos[0]
    elif getSelector(z, pos, entity) != []:
        z = getSelector(x, pos, entity)[0].position[2]
    return int(x), int(y), int(z)
