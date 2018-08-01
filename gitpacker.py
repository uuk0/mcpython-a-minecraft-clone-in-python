import os, pickle, zipfile, sys, time, traceback


#THESE COMPILER CAN PACK AND UNPACK PYTHON FILES AND RESOURCE FILES

#a list of ALL moduls that mustn't be copied (for littler space)
BUILD_IN = ["__future__", "sys", "math", "traceback", "time", "os", "random", "pickle", "gtk", "ctypes",
            "shutil", "collections", "threading", "platform", "contextlib", "re", "subprocess", "warnings",
            "itertools", "objc", "urllib", "urllib.request", "urllib.error", "urllib.parse", "errno",
            "multiprocessing", "select", "MacOS", "signal", "io", "getopt", "inspect", "array", "operator",
            "zlib", "cpngfilters", "msvcrt", "unicodedata", "builtins", "mmap", "ctypes", "ctypes.util",
            "future.utils", "future", "atexit", "_weakref", "imp", "binascii", "os.path", "_struct", "_functools",
            "functools", "struct", "optparse", "codecs", "Image", "PIL", "heapq", "copy", "marshal", "textwrap",
            "parser", "importlib", "dummy_threading", "html"]
FILE_ENDINGS = ["", ".py", ".pyc", ".png"]

MAX_SIZE = 10 * 1024 * 1024 #THES SIZE IS OPTIMIZED FOR MCPYTHON. real size: 25 * 1024 * 1024

def _getDir(file): #splitted by /
    file = file.split("/")[:-1]
    f = file[0]
    for e in file[1:]:
        f += "/" + e
    return f

def _getFullFile(file): #input splitted by "."
    while "." in file:
        file = file[:file.index(".")] + "/" + file[file.index(".")+1:]
    fd = None
    for d in sys.path:
        for e in FILE_ENDINGS:
            if os.path.exists(d+"/"+file+e):
                fd = d+"/"+file+e
    if fd:
        return fd
    else:
        pass

def _getLocalFile(file, debug=False): #output splitted by "/"
    rd = None
    for d in sys.path:
        if file.startswith(d):
            rd = d
    if debug:
        print(file, rd, sys.path)
    if rd:
        return file.replace(rd, "")[1:]
    else:
        raise IOError("can't localize file: file is not in sys.path", file)

def getNecFiles(file, local=None, files=None):
    if local:
        sys.path += local
    if files != None:
        _files = files[:]
    else:
        _files = []
    files = [file]
    analyse = [file]
    analysed = _files
    files += _files
    while len(analyse) > 0:
        try:
            file = analyse.pop(0)
            if file.endswith(".py") and not file in analysed and not _getFullFile(file) in analysed:
                print("analysing file: "+file)
                f = open(file, mode="r")
                data = f.read()
                f.close()
                for i, l in enumerate(data.split("\n")):
                    try:
                        if "import " in l: #import-statement
                            while l.startswith(" ") or l.startswith("   "):
                                l = l[1:]
                            if l.startswith("import "):
                                if not l.split(" ")[1] in BUILD_IN:
                                    f = _getFullFile(l.split(" ")[1])
                                    files.append(f)
                                    analyse.append(f)
                            elif l.startswith("from"):
                                f = l.split(" ")[1]
                                if not f.startswith("."):
                                    if not (f in BUILD_IN or f.split(".")[0] in BUILD_IN):
                                        try:
                                            fd = _getFullFile(f)
                                        except:
                                            try:
                                                fd = _getFullFile(l.split(" ")[1] + "." + l.split(" ")[3])
                                            except:
                                                print(l, i)
                                                raise
                                        files.append(fd)
                                        analyse.append(fd)
                                else:
                                    analyse.append(file+"/"+f[1:])
                            elif l.startswith("print") or l.startswith("#") or l.startswith("exec") or "__import__" in l:
                                pass
                    except:
                        print(l, i)
                        traceback.print_exc()
            elif os.path.isdir(file):
                for e in os.listdir(file):
                    analyse.append(file+"/"+e)
            analysed.append(file)
        except:
            print(file)
            traceback.print_exc()
    if local:
        sys.path += local
    return files

def pack(file, out, res=[], not_res=[], not_res_end=[], version=0, name="", local=None, syspath=None):
    if type(file) == str: file = [file]
    files = []
    for f in file:
        files += getNecFiles(f)
    print("adding extra resources...")
    while len(res) > 0:
        e = res.pop(0)
        if e in not_res:
            pass
        else:
            flag = False
            for er in not_res_end:
                if e.endswith(er):
                    flag = True
            if flag:
                pass
            elif os.path.isfile(e):
                print(e)
                if e.endswith(".py"):
                    files = getNecFiles(e, local=local, files=files)
                else:
                    files.append(e)
            elif os.path.isdir(e):
                print(e)
                for f in os.listdir(e):
                    res.append(e+"/"+f)
    files = list(set(files))
    time.sleep(2)
    print("files found:", len(files))
    time.sleep(2)
    file_id = 0
    zip = None
    if syspath:
        sys.path = syspath
    while len(files) > 0:
        file = files.pop(0)
        if file:
            lf = _getLocalFile(file)
            print(lf)
            if not os.path.isfile(out+"/file_"+str(file_id)+".spart"):
                zip = zipfile.ZipFile(out+"/file_"+str(file_id)+".spart", mode="w")
            else:
                zip = zipfile.ZipFile(out+"/file_"+str(file_id)+".spart", mode="a")
            zip.write(file, arcname=lf)
            zip.close()
            if os.path.getsize(out+"/file_"+str(file_id)+".spart") >= MAX_SIZE:
                file_id += 1
            
def pack_mcpython():
    for e in os.listdir("."):
        if os.path.isfile(e) and e.endswith(".spart"):
            os.remove(e)
    pack(["./__main__.py"],
                ".", res=["./assets", "./config.txt", "./initscript.txt",
               "./exceptions.txt",
              "./version.info", "./mods/creatmcmodinfo.py",
              "./mods/mcpython_moduls",
              "./mods/mcpython", "./saves/dir.txt",
                                               "./mods/mcpython/mcpython.py", "./mods/mcpython_moduls/modulinit.py"],
         not_res=["./assets/unused", "./assets/textures/todo"],
         not_res_end=[".pyc", ".xml"],
         version=int(input("select an version-id: ")),
         name="mcpython",
         local=["./mods/mcpython", "./mods/mcpython_moduls"], syspath=sys.path[:])

def unpack():
    for e in os.listdir("."):
        if os.path.isfile(e) and e.endswith(".spart"):
            with zipfile.ZipFile(e) as f:
               f.extractall(".")
        print(e)

if len(sys.argv) > 1:
    if sys.argv[1] == "unpack":
        unpack()
    elif sys.argv[1] == "pack":
        pack_mcpython()
