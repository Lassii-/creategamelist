#!/usr/bin/env python3

import glob
import os
import sys
import subprocess
import arghelper
from pathlib import Path
from datetime import datetime

rompath = arghelper.get_rompath()

date = datetime.today().strftime("%d-%m-%Y")
answer = input("Which platform? (MAME/NES/SNES/GB/GBC/GBA/N64/PCE/MD ")
while(answer != "MAME" and answer != "NES" and answer != "SNES" and answer != "GB" and answer != "GBC" and answer != "GBA" and answer != "N64" and answer != "PCE" and answer != "MD"):
    print("You didn't pick a correct platform! Choose from MAME/NES/SNES/GB/GBC/N64/PCE/MD")
    answer = input("Which platform? ")

if(answer == "MAME"):
    gamefile = Path("MAMEgameslist.txt")
elif(answer == "NES"):
    gamefile = Path("NESgameslist.txt")
elif(answer == "SNES"):
    gamefile = Path("SNESgameslist.txt")
elif(answer == "GB"):
    gamefile = Path("GBgameslist.txt")
elif(answer == "GBC"):
    gamefile = Path("GBCgameslist.txt")
elif(answer == "GBA"):
    gamefile = Path("GBAgameslist.txt")
elif(answer == "N64"):
    gamefile = Path("N64gameslist.txt")
elif(answer == "PCE"):
    gamefile = Path("PCEgameslist.txt")
elif(answer == "MD"):
    gamefile = Path("MDgameslist.txt")


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
