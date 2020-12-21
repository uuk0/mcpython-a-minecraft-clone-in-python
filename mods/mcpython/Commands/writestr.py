from . import Command


class WriteStr(Command.Command):
    @staticmethod
    def isCommand(line):
        return line.split(" ")[0] in ["/msg", "/tell", "/w"]

    @staticmethod
    def getSyntaxError(line, entity, position, chat):
        s = line.split(" ")
        if len(s) == 1:
            return [
                "at "
                + s[0]
                + "  : invalid syntax: missing argument <players> and <msg>",
                "   " + " " * len(s[0]) + "^",
            ]
        elif len(s) == 2:
            if len(Command.getSelector(s[1], position, entity)) == 0:
                return [
                    "at "
                    + s[1]
                    + " : invalid argument: excpected entity OR entityselector"
                ]
            else:
                return [
                    "at " + line + " : invalid syntax: missing argument <msg>",
                    "   " + " " * len(line) + "^",
                ]
        elif len(s) > 3:
            return [
                "at "
                + line
                + " : invalid syntax: excpceted 3 Arguments, gotted "
                + str(len(s)),
                "   " + " " * len(s[0]) + " " * len(s[1]) + " " * len[s[2]] + "  ^",
            ]
        else:
            for e in Command.getSelector(s[1], position, entity):
                if not (hasattr(e, "writeToChat") and callable(e.writeToChat)):
                    return [
                        "at "
                        + s[1]
                        + " : invalid selector: excpected only players, gotted ",
                        e,
                        "    ^",
                    ]

    @staticmethod
    def parse(line, entity, position, chat):
        s = line.split(" ")
        players = Command.getSelector(s[1], position, entity)
        for player in players:
            player.writeToChat(s[2])

    @staticmethod
    def getHelp():
        return [
            "/msg <players> <msg>: prints the msg by every entity",
            "/tell <players> <msg>: prints the msg by every entity",
            "/w <players> <msg>: prints the msg by every entity",
        ]


Command.handler.register(WriteStr)
