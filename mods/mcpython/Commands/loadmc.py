#todo: delet
from . import Command
import mcworldconverter

class loadmc(Command.Command):
    @staticmethod
    def getHelp():
        return "/loadmc <worldfolder>: loads an minecraft world and saves it to local dir"

    @staticmethod
    def isCommand(line):
        return line.split(" ")[0] == "/loadmc"

    @staticmethod
    def getSyntaxError(line, entity, position, chat): #todo: add syntax-system
        pass

    @staticmethod
    def parse(line, entity, position, chat):
        mcworldconverter.convert(line.split(" ")[1])

Command.handler.register(loadmc)