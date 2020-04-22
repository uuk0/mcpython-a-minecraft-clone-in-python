from . import Command

class replaceitem(Command.Command):
    @staticmethod
    def getHelp():
        return "/replaceitem <entity> <id> <item> [<amount>]"

    @staticmethod
    def isCommand(line):
        return line.split(" ")[0] == "/replaceitem"

    @staticmethod
    def getSyntaxError(line, entity, position, chat):
        #todo: add systax controlling
        return None

    @staticmethod
    def parse(line, entity, position, chat):
        s = line.split(" ")
        e = Command.getSelector(s[1], position, entity)
        invs = e.getInventory()
        id = 0
        for invs in invs[:]:
            for i in invs:
                if id == int(s[2]):
                    i.setItem(s[3], int(s[4]) if len(s) == 3 else 1)
                id += 1

Command.handler.register(replaceitem)