import os
import sys
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

Path(rompath / "result").mkdir(parents=True, exist_ok=True)
output = rompath / "result"
try:
    if Path("gameslist.txt").is_file:
        with open("gameslist.txt") as gameslist:
            for game in gameslist:
                os.rename(os.path.join(rompath, game.strip()),
                          output / game.strip())
except IOError:
    print("Can't find gameslist.txt!")
