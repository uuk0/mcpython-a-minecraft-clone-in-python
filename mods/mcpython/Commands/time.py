from . import Command
import globals as G

class time(Command.Command):
    @staticmethod
    def getHelp():
        return "/time <'set'|'add'|'remove'> <time|'day'|'night'>"

    @staticmethod
    def isCommand(line):
        return line.split(" ")[0] == "/time"

    @staticmethod
    def getSyntaxError(line, entity, position, chat): #todo: add syntax-system
        pass

    @staticmethod
    def parse(line, entity, position, chat):
        sc = line.split(" ")
        if sc[1] == "set":
            if sc[2] == "day":
                sc[2] = 100
            elif sc[2] == "night":
                sc[2] = 1000
            G.window.gametime = int(sc[2])
        elif sc[1] == "add":
            G.window.gametime += int(sc[2])
        elif sc[1] == "remove":
            G.window.gametime -= int(sc[2])

Command.handler.register(time)