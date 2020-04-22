from . import Command
import globals as G

class seed(Command.Command):
    @staticmethod
    def isCommand(line):
        return line == "/seed"

    @staticmethod
    def parse(line, entity, position, chat):
        print("parsing")
        chat.println("seed: "+str(G.seed))

    @staticmethod
    def getHelp():
        return "/seed: returns the seed of the world"

Command.handler.register(seed)