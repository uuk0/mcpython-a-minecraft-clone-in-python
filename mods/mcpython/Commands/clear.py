from . import Command

class clear(Command.Command):
    @staticmethod
    def isCommand(line):
        return line.split(" ")[0] == "/clear"

    @staticmethod
    def getSyntaxError(line, entity, position, chat):
        s = line.split(" ")
        if len(s) > 2:
            return ["at "+s+" : invalid syntax: excpected 1 or 2 arguments, getted "+str(len(s)),
                    "    "+" "*len(s[0])+" "*len(s[1])+" ^"]
        if len(s) == 2 and Command.getSelector(s[1]) == []:
            return ["at "+s[1]+" : invalid entity: no entity found",
                    "    ^"]
        return None

    @staticmethod
    def parse(line, entity, position, chat):
        s = line.split(" ")
        if len(s) == 2:
            entity = Command.getSelector(s[1], position, entity)
        else:
            entity = [entity]
        for en in entity:
            for i in en.getInventory():
                for s in i.slots:
                    s.setItem(None)

    @staticmethod
    def getHelp():
        return "/clear [<entity>]: clears the inventory of the entity"

Command.handler.register(clear)