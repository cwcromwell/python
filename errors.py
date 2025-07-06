import sys
file = open("log", "w")
sys.stderr.write = file.write


print(x) # x is not defined
