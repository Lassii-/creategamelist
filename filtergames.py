#!/usr/bin/env python3

import os
import sys
import arghelper
from pathlib import Path

rompath = arghelper.get_rompath()
Path(rompath / "result").mkdir(parents=True, exist_ok=True)
output = rompath / "result"

try:
    if Path("gameslist.txt").is_file:
        with open("gameslist.txt") as gameslist:
            for game in gameslist:
                os.rename(os.path.join(rompath, game.strip()),
                          output / game.strip())
except OSError as e:
    print(e)
