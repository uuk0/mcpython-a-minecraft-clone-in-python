from . import Command

class teleport(Command.Command):
    @staticmethod
    def getHelp():
        return ["/teleport <entity> <x> <y> <z>: teleport the entity to given position",
                "/tp <entity> <x> <y> <z>: teleport the entity to given position"]

    @staticmethod
    def isCommand(line):
        return line.split(" ")[0] in ["/teleport", "/tp"]

    @staticmethod
    def getSyntaxError(line, entity, position, chat):
        #todo: add syntax-system
        return None

    @staticmethod
    def parse(line, entity, position, chat):
        s = line.split(" ")
        pos = Command.getPosition(s[2], s[3], s[4], position, entity)
        entity = Command.getSelector(s[1], position, entity)
        for e in entity:
            e.position = pos
            if hasattr(e, "getInst"):
                e.getInst().window.position = pos


Command.handler.register(teleport)