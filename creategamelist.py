#!/usr/bin/env python3

import os

import arghelper
from pathlib import Path
from datetime import datetime

rompath: Path = arghelper.get_rompath()
gamefile: Path = arghelper.get_gameslist()
date = datetime.today().strftime("%d-%m-%Y")

def main():
    try:
        if gamefile.is_file():
            print(f"There's already a {gamefile}-file, do you want to make a backup of it?")
            answer = input("Y/N?\n").upper()
            while(answer != "Y" and answer != "N"):
                print("Only accepting Y for yes and N for no.")
                answer = input("Y/N?\n")
            if(answer == "Y"):
                # Rename the old file with current date appended to the filename
                gamefile.rename(
                    Path(gamefile.parent, f"{gamefile.stem}_{date}" + gamefile.suffix))
            elif(answer == "N"):
                # Remove the old file
                gamefile.unlink()
    except OSError as e:
        print(e)

    try:
        with open(gamefile, "a") as output:
            for file in sorted(os.listdir(rompath)):
                if file.endswith(".zip"):
                    print(os.path.join(file))
                    output.write(file+"\n")
    except OSError as e:
        print(e)

if __name__ == '__main__':     # Runs main() if file wasn't imported.
    main()