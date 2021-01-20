import sys
from pathlib import Path

systems = ['MAME', 'NES', 'SNES', 'GB', 'GBC', 'N64', 'PCE', 'MD']

def get_rompath():
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
    return rompath


def get_gameslist():
    answer = input(f"Which platform? {systems} ")

    while(answer not in systems):
        print(f"You didn't pick a correct platform! Choose from {systems}")
        answer = input("Which platform? ")
    gamefile = Path(f"{answer}gameslist.txt")
    print(gamefile)
    return gamefile
