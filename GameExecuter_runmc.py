import pickle
import subprocess
import sys
import os
import time
from subprocess import *

#THESE COMPILER CAN PACK AND UNPACK PYTHON FILES AND RESOURCE FILES

def getDir(file):
    s = file.split("/")[:-1]
    st = s[0]
    for e in s[1:]:
        st += "/" + e
    return st

def unpack(file, outdir):
    f = open(file, mode="rb")
    data = pickle.load(f)
    f.close()
    for e in data["files"].keys():
        print("unpacking file", e)
        d = getDir(outdir+"/"+e)
        if not os.path.isdir(d):
            os.makedirs(d)
        f = open(outdir+"/"+e, mode="wb")
        f.write(data["files"][e][0])
        f.close()

def execute(file, dir):
    f = open(file, mode="rb")
    d = pickle.load(f)
    f.close()
    id = d["id"]
    name = d["name"]

    flag = False
    if os.path.isfile(dir+"/unpack.version"):
        f = open(dir+"/unpack.version", mode="rb")
        data = pickle.load(f)
        f.close()
        if data["name"] != name or data["id"] != id:
            flag = True
    else:
        flag = True
    if flag:
        unpack(file, dir)
        data = {"name":name, "id":id}
        f = open(dir+"/unpack.version", mode="wb")
        pickle.dump(data, f)
        f.close()
    sys.path.append(dir)
    os.system("start cmd /c py "+dir+"/__main__.py "+dir)
    sys.path.remove(dir)

def startMcpython():
    execute("./version.cpy", "./tmp")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        startMcpython()
    else:
        execute(sys.argv[1], "./tmp")
