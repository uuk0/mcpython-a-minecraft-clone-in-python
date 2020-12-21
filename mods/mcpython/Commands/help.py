from . import Command
import EventHandler

COMMANDLIST = []


class help(Command.Command):
    @staticmethod
    def getcommands(*args):
        print("[COMMAND/INFO] loading commands for help-pages...")
        global COMMANDLIST
        COMMANDLIST = []
        speclist = {}
        for c in Command.handler.commands:
            speclist[c.__name__] = c
        i = list(speclist.keys())
        i.sort()
        for e in i:
            if type(speclist[e].getHelp()) == str:
                COMMANDLIST.append(speclist[e].getHelp())
            else:
                COMMANDLIST += speclist[e].getHelp()
        COMMANDLIST.sort()

    @staticmethod
    def isCommand(line):
        return line.split(" ")[0] == "/help"

    @staticmethod
    def getSyntaxError(line, entity, position, chat):
        s = line.split(" ")
        if len(s) > 2:
            return [
                "at "
                + s
                + " : invalid syntax: excpected 1 or 2 arguments, getted "
                + str(len(s)),
                "    " + " " * len(s[0]) + " " * len(s[1]) + " ^",
            ]
        if len(s) == 2 and s[1] != "all":
            try:
                index = int(s[1])
            except:
                return ["at " + s[1] + " : invalid index", "    ^"]

    @staticmethod
    def getHelp():
        return "/help [<index|'all'>]: returns this help page"

    @staticmethod
    def parse(line, entity, position, chat):
        s = line.split(" ")
        if len(s) == 2 and s[1] != "all":
            index = int(s[1])
        elif len(s) != 2:
            index = 1
        if len(s) > 1 and s[1] == "all":
            chat.println("-------------------------------")
            chat.println("help page")
            chat.println("-------------------------------")
            for c in COMMANDLIST:
                chat.println(c)
            return
        data = COMMANDLIST[(index - 1) * 8 : (index - 1) * 8 + 8]
        chat.println("-------------------------------")
        chat.println("help page " + str(index))
        chat.println("-------------------------------")
        for c in data:
            chat.println(c)


Command.handler.register(help)

EventHandler.eventhandler.on_event("on_game_started", help.getcommands)
