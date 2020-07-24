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
