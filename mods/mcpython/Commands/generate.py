# todo: remove
from . import Command
from mathhelper import *
import globals as G


class generate(Command.Command):
    @staticmethod
    def getHelp():
        return "/generate: generate the chunk in which you are in"

    @staticmethod
    def isCommand(line):
        return line == "/generate"

    @staticmethod
    def parse(line, entity, position, chat):
        sector = sectorize(G.window.position)
        G.window.world.generateChunk(sector[0] * 16, sector[2] * 16)


Command.handler.register(generate)
