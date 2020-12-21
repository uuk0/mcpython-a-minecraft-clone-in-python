from . import Command
import globals as G


class summon(Command.Command):
    @staticmethod
    def getHelp():
        return "/summon <name> <x> <y> <z>"

    @staticmethod
    def isCommand(line):
        return line.split(" ")[0] == "/summon"

    @staticmethod
    def getSyntaxError(line, entity, position, chat):
        pass  # todo: add syntax-system

    @staticmethod
    def parse(line, entity, position, chat):
        sc = line.split(" ")
        name = sc[1]
        x, y, z, = (
            int(sc[2]),
            int(sc[3]),
            int(sc[4]),
        )
        G.window.model.add_entity(name, (x, y, z))


Command.handler.register(summon)
