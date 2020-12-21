# todo: remove
from . import Command
import structures
import globals as G


class paststructur(Command.Command):
    @staticmethod
    def getHelp():
        return "/paststructur <name> <x> <y> <z>"

    @staticmethod
    def isCommand(line):
        return line.split(" ")[0] == "/paststructur"

    @staticmethod
    def getSyntaxError(line, entity, position, chat):  # todo: add systax-system
        pass

    @staticmethod
    def parse(line, entity, position, chat):
        sc = line.split(" ")
        name = sc[1]
        x, y, z = int(sc[2]), int(sc[3]), int(sc[4])
        structures.handler.structures[name].past(G.window.model, x, y, z)


Command.handler.register(paststructur)
