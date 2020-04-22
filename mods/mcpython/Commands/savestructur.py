#todo: remove
from . import Command

import structures
import pickle

class savestructur(Command.Command):
    @staticmethod
    def getHelp():
        return "/savestructur <name> <sx> <sy> <sz> <ex> <ey> <ez> [<copyair>] [<rx> <ry> <rz>]"

    @staticmethod
    def getSyntaxError(line, entity, position, chat): # todo: add syntax-system
        pass

    @staticmethod
    def isCommand(line):
        return line.split(" ")[0] == "savestructur"

    @staticmethod
    def parse(line, entity, position, chat):
        sc = line.split(" ")
        name = sc[1]
        sx = int(sc[2]);
        sy = int(sc[3]);
        sz = int(sc[4])
        ex = int(sc[5]);
        ey = int(sc[6]);
        ez = int(sc[7])
        copyair = bool(sc[8]) if len(sc) > 8 else False
        if sx > ex:
            d = sx
            sx = ex
            ex = d
        if sy > ey:
            d = sy
            sy = ey
            ey = d
        if sz > ez:
            d = sz
            sz = ez
            ez = d
        if len(sc) > 9:
            rx, ry, rz = int(sc[9]) - sx, int(sc[10]) - sy, int(sc[11]) - sz
        else:
            rx, ry, rz = 0, 0, 0
        commands = []
        for x in range(sx, ex):
            for y in range(sy, ey):
                for z in range(sz, ez):
                    if not (x, y, z) in G.window.model.world:
                        if copyair:
                            commands.append([1, (x - sx - rx, y - sy - ry, z - sz - rz)])
                    else:
                        commands.append([0, G.window.model.world[(x, y, z)].getName(),
                                         (x - sx - rx, y - sy - ry, z - sz - rz)])
                        for e in G.window.model.world[(x, y, z)].getNBTNames():
                            commands.append([1, (x - sx - rx, y - sy - ry, z - sz - rz), e,
                                             G.window.model.world[(x, y, z)].getNBT(e)])
        f = open("./assets/structures/" + name + ".structur", mode="wb")
        pickle.dump({"version": structures.STRUCTUR_VERSION,
                     "size": (ex - sx, ey - sy, ez - sz),
                     "blocks": commands,
                     "name": name,
                     "build_base": ()}, f)
        f.close()

Command.handler.register(savestructur)