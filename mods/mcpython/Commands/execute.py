from . import Command
import globals as G

class execute(Command.Command):
    @staticmethod
    def isCommand(line):
        return line.split(" ")[0] == "/execute"

    @staticmethod
    def getSyntaxError(line, entity, position, chat): #todo: add syntax controling
        return None

    @staticmethod
    def parse(line, entity, position, chat):
        s = line.split(" ")
        i = 1
        while i <= len(s):
            if s[i] == "as":
                entity = Command.getSelector(s[i+1], position, entity)
                i += 2
            elif s[i] == "at":
                position = Command.getPosition(s[i+1], s[i+2], s[i+3], position, entity)
                i += 2
            elif s[i] == "if":
                if s[i+1] == "block":
                    pos = Command.getPosition(s[i+2], s[i+3], s[i+4], position, entity)
                    blockname = s[i+5]
                    if not pos in G.model.world or not G.model.world[pos].getName() == blockname:
                        return
                    s += 6
                elif s[i+1] == "entity":
                    e = Command.getSelector(s[i+2], pos, entity)
                    if e == []:
                        return
            elif s[i] == "unless":
                pass
            elif s[i] == "run":
                commands = s[i+1:]
                command = ""
                for e in commands:
                    commands += (" " if command != "" else "") + e
                Command.handler.parse(command, entity, position, G.window.chat)

    @staticmethod
    def getHelp():
        return ["/execute {[as <entity>], [at <entity>], [if/unless [block <position> <block>, blocks <position1> <position2> <position>, entity <entity> #missing:score]], [in <dimenson-id], [run <undercommand>], }"]

Command.handler.register(execute)