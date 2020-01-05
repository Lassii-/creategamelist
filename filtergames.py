#!/usr/bin/env python3

import os
import sys
import arghelper
from pathlib import Path

gamefile = Path("gameslist.txt")
rompath = arghelper.get_rompath()

try:
    with open(gamefile) as gameslist:
        Path(rompath / "result").mkdir(parents=True, exist_ok=True)
        output = rompath / "result"
        for game in gameslist:
            os.rename(os.path.join(rompath, game.strip()),
                      output / game.strip())
except (OSError, FileNotFoundError) as e:
    print("If you got an error saying gameslist.txt doesn't exist, you probably forgot to run creategamelist.py first.")
    print(e)
