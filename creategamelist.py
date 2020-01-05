#!/usr/bin/env python3

import glob
import os
import sys
import subprocess
import arghelper
from pathlib import Path
from datetime import datetime

rompath = arghelper.get_rompath()
gamefile = Path("gameslist.txt")
date = datetime.today().strftime("%d-%m-%Y")

try:
    if gamefile.is_file():
        print("There's already a gameslist-file, do you want to make a backup of it?")
        answer = input("Y/N?\n")
        while(answer != "Y" and answer != "N"):
            print("Only accepting Y for yes and N for no.")
            answer = input("Y/N?\n")
        if(answer == "Y"):
            gamefile.rename(
                Path(gamefile.parent, f"{gamefile.stem}_{date}" + gamefile.suffix))
        elif(answer == "N"):
            gamefile.unlink()
except OSError as e:
    print(e)

try:
    with open(gamefile, "a") as output:
        for file in os.listdir(rompath):
            if file.endswith(".zip"):
                print(os.path.join(file))
                output.write(file+"\n")
    os.system(f"sort {gamefile} -o {gamefile}")
except OSError as e:
    print(e)
