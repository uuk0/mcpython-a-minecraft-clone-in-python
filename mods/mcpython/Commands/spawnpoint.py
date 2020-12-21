from . import Command


class spawnpoint(Command.Command):
    @staticmethod
    def getHelp():
        return "/spawnpoint <x> <y> <z> [<entity]: set the spawnpoint"

    @staticmethod
    def isCommand(line):
        return line.split(" ")[0] == "/spawnpoint"

    @staticmethod
    def getSyntaxError(line, entity, position, chat):
        # todo: add syntax-system
        return None

    @staticmethod
    def parse(line, entity, position, chat):
        s = line.split(" ")
        pos = Command.getPosition(s[1], s[2], s[3], position, entity)
        if len(s) > 4:
            entity = Command.getSelector(s[4])
        else:
            entity = [entity]
        for en in entity:
            en.getInst().window.spawnpoint = pos


Command.handler.register(spawnpoint)
