import glob
import os
import sys
import subprocess

if len(sys.argv) > 2:
    print("Too many arguments.")
    sys.exit()

if len(sys.argv) < 2:
    rompath = os.getcwd()
    print(rompath)
else:
    if not os.path.isdir(sys.argv[1]):
        print("The path you specified doesn't exist.")
        sys.exit()
    rompath = sys.argv[1]
    print(rompath)

with open("gameslist.txt", "a") as output:
    for file in os.listdir(rompath):
        if file.endswith(".zip"):
            print(os.path.join(file))
            output.write(file+"\n")

os.system("sort gameslist.txt -o gameslist.txt")
