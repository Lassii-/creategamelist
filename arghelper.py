import sys
import os
from pathlib import Path

systems = ['MAME', 'NES', 'SNES', 'GB', 'GBC', 'N64', 'PCE', 'MD']

# Sets the path to ROM-files based on the user given CLI argument. If that's not given, uses the current working directory
def get_rompath() -> Path:
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
    rompath = Path(rompath)
    if(os.path.exists(rompath)):
        return rompath
    else:
        print("The path given doesn't exist!")
        sys.exit()


# Sets the name of the list file based on user selection
def get_gameslist() -> Path:
    answer = input(f"Which platform? {systems} ").upper()
    while(answer not in systems):
        print(f"You didn't pick a correct platform! Choose from {systems}")
        answer = input("Which platform? ").upper()
    gamefile = Path(f"{answer}gameslist.txt")
    return gamefile
