import sys
from pathlib import Path


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
    return gamefile
