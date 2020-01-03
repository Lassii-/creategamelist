#!/usr/bin/env python3

import glob
import os
import sys
import subprocess
from pathlib import Path

if len(sys.argv) > 2:
    print("Too many arguments.")
    sys.exit()

if len(sys.argv) < 2:
    rompath = Path.cwd()
else:
    if not Path(sys.argv[1]).exists:
        print("The path you specified doesn't exist.")
        sys.exit()
    rompath = sys.argv[1]

try:
    with open("gameslist.txt", "a") as output:
        for file in os.listdir(rompath):
            if file.endswith(".zip"):
                print(os.path.join(file))
                output.write(file+"\n")
    os.system("sort gameslist.txt -o gameslist.txt")
except Exception:
    print("Unexpected error:", sys.exc_info()[0])
