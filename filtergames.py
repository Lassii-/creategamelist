#!/usr/bin/env python3

import os
import arghelper
from pathlib import Path

rompath: Path = arghelper.get_rompath()
gamefile: Path = arghelper.get_gameslist()

def main():
    try:
        with open(gamefile) as gameslist:
            Path(rompath / "result").mkdir(parents=True, exist_ok=True)
            output = rompath / "result"
            for game in gameslist:
                os.rename(os.path.join(rompath, game.strip()),
                        output / game.strip())
    except (OSError, FileNotFoundError) as e:
        print(e)
        print(f"If you got an error saying {gamefile}.txt doesn't exist, you probably forgot to run creategamelist.py first.")

if __name__ == '__main__':
    main()
