from . import Command
from Item.Item import handler as itemhandler


class give(Command.Command):
    @staticmethod
    def isCommand(line):
        return line.split(" ")[0] == "/give"

    @staticmethod
    def getSyntaxError(line, entity, position, chat):
        s = line.split(" ")
        if len(s) == 1:
            return [
                "at "
                + s[0]
                + "  : invalid syntax: missing argument <entity> and <item>",
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
                    "at " + line + " : invalid syntax: missing argument <item>",
                    "   " + " " * len(line) + "^",
                ]
        elif len(s) == 3:
            if itemhandler.getClass(s[2]) == None:
                return ["at " + s[2] + " : invalid argument: excpected item-name"]
        elif len(s) == 4:
            if s[3] != "stack":
                try:
                    int(s[3])
                except:
                    return [
                        "at "
                        + s[3]
                        + " : invalid argument type: expected INT or 'stack', gotted "
                        + str(type(s[2])),
                        "    ^",
                    ]
        elif len(s) > 4:
            return [
                "at "
                + line
                + " : invalid syntax: excpceted 3 Arguments, gotted "
                + str(len(s)),
                "   " + " " * len(s[0]) + " " * len(s[1]) + " " * len[s[2]] + "  ^",
            ]

    @staticmethod
    def getHelp():
        return "/give <entity> <item> [<amount>]: give the entity the item with amount"

    @staticmethod
    def parse(line, entity, position, chat):
        s = line.split(" ")
        item = itemhandler.getClass(s[2])
        amount = (
            1
            if len(s) == 3
            else (int(s[3]) if s[3] != "stack" else item.getMaxStackSize())
        )
        entity = Command.getSelector(s[1], position, entity)
        for en in entity:
            for e in en.getInventory():
                for slot in e.slots:
                    if slot.item and slot.item.getName() == s[2]:
                        if slot.amount < slot.item.getMaxStackSize():
                            if slot.amount + amount <= slot.item.getMaxStackSize():
                                slot.amount += amount
                                return
                            else:
                                na = amount - (
                                    slot.item.getMaxStackSize() - slot.amount
                                )
                                slot.amount = slot.item.getMaxStackSize()
                                amount = na
                                return
            for e in en.getInventory():
                for slot in e.slots:
                    if slot.item == None:
                        slot.setItem(s[2], amount=amount)
                        return


Command.handler.register(give)
