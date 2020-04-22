from . import Command

class kill(Command.Command):
    @staticmethod
    def getHelp():
        return "/kill [<entity>]: kills every selected entity. when nothing getted, @s is used"

    @staticmethod
    def isCommand(line):
        return line.split(" ")[0] == "/kill"

    @staticmethod
    def getSyntaxError(line, entity, position, chat):
        s = line.split(" ")
        if len(s) == 2:
            return ["at " + s[1] + " : invalid argument: excpected entity OR entityselector"]
        elif len(s) > 2:
            return ["at " + line + " : invalid syntax: excpceted 1 or 2 Arguments, gotted " + str(len(s)),
                    "   " + " " * len(s[0]) + " " * len(s[1]) +" ^"]

    @staticmethod
    def parse(line, entity, position, chat):
        s = line.split(" ")
        if len(s) == 2:
            entity = Command.getSelector(s[1], position, entity)
        else:
            entity = [entity]
        for e in entity:
            e.kill()

Command.handler.register(kill)