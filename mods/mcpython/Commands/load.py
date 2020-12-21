# todo: delet
from . import Command
import WorldSaver
import globals as G


class load(Command.Command):
    @staticmethod
    def getHelp():
        return "/load <worldname>: load the world"

    @staticmethod
    def isCommand(line):
        return line.split(" ")[0] == "/load"

    @staticmethod
    def getSyntaxError(line, entity, position, chat):
        pass

    # todo: add syntax-system

    @staticmethod
    def parse(line, entity, position, chat):
        s = line.split(" ")
        G.window.worldname = None
        name = s[1]
        WorldSaver.loadWorld(G.window.model, name)
        G.window.worldname = name


Command.handler.register(load)
