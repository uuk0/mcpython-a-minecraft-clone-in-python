from . import Command

class gamemode(Command.Command):
    @staticmethod
    def isCommand(line):
        return line.split(" ")[0] == "/gamemode"

    @staticmethod
    def getSyntaxError(line, entity, position, chat):
        s = line.split(" ")
        if len(s) == 1:
            return ["at "+line+" : missing argument <gamemode>",
                    "   "+" "*len(line)+"^"]
        if s[1] not in ["survival", "creative", "hardcore", "spectator",
                        "0", "1", "2", "3"]:
            return ["at "+s[1]+" : unknown gamemode"
                    "    ^"]
        if len(s) > 3:
            return ["at " + line + " : invalid syntax: excpceted 3 Arguments, gotted " + str(len(s)),
                    "   " + " " * len(s[0]) + " " * len(s[1]) + " " * len[s[2]] + "  ^"]
        if len(s) == 3 and Command.getSelector(s[2], position, entity) == []:
            return ["at " + s[2] + " : invalid argument: excpected entity OR entityselector"]
        for e in (Command.getSelector(s[2], position, entity) if len(s) == 3 else [entity]):
            if not (hasattr(e, "writeToChat") and callable(e.writeToChat)):
                return ["at " + s[2] + " : invalid selector: excpected only players, gotted "+str(e),
                        "    ^"]


    @staticmethod
    def parse(line, entity, position, chat):
        s = line.split(" ")
        gamemode = s[1]
        if gamemode in ["survival", "creative", "hardcore", "spectator"]:
            gamemode = ["0", "1", "2", "3"][["survival", "creative", "hardcore", "spectator"].index(gamemode)]
        if len(s) == 3:
            entity = Command.getSelector(s[2], position, entity)
        else:
            entity = [entity]
        for e in entity:
            e.getInst().gamemode = gamemode

    @staticmethod
    def getHelp():
        return "/gamemode <gamemode> [<players>]: set the gamemode of you / players"


Command.handler.register(gamemode)