import sys
file = open("log", "w")
sys.stderr.write = file.write