print("MCPYTHON ModLoader")
import sys, os, globals as G
dir = sys.argv[1] if len(sys.argv) > 1 else "./"
G.local = dir

sys.argv.append(os.path.dirname(os.path.realpath(__file__)))
import ModLoader
ModLoader.load(dir)
