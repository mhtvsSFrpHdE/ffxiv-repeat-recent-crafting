from pathlib import Path  # nopep8
import os  # nopep8
import sys  # nopep8

# Append source code folder
srcPath = Path(os.path.dirname(__file__)).joinpath("Src")  # nopep8
sys.path.append(srcPath.joinpath("Config"))  # nopep8

del srcPath  # nopep8

import Config.Setting as Setting
import Src.Clipboard.ReadLoop as ReadLoop
import Src.Message.Result as Result

# Get
skillSequence, totalQuality, totalDurability, totalProgress = ReadLoop.Read(Setting)

# Set
Result.PrintResult(Setting, skillSequence, totalQuality, totalDurability, totalProgress)
