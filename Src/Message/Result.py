from string import Template
from termcolor import colored
import pyperclip

import Config.Message as Message


def PrintResult(setting, skillSequence, totalQuality, totalDurability, totalProgress):
    macroLineBuffer = ""
    totalSkillTime = 0
    macrolineNumber = len(skillSequence)

    # Has valid skill in sequence
    if macrolineNumber > 0:
        # Convert skill sequence to macro
        for skillIndex, skill in enumerate(skillSequence):
            macroLineBuffer += skill.ToMacroString()
            totalSkillTime += int(skill.CastCost)

            # Every 15 line, add an empty line as warning
            if (skillIndex + 1) % setting.MacroSize == 0:
                # Paste "\n" string directly will not work
                macroLineBuffer += setting.NewLineInResult

        # Copy macro to clipboard
        pyperclip.copy(macroLineBuffer)

        # Print macro
        print(macroLineBuffer + "\n")

        # Print information about this macro
        print(Message.MacroCopied)

        # Warning if line number exceeded size limit
        if macrolineNumber > setting.MacroSize:
            print(colored(Message.ExceededMaximumMacroSize, 'red'))

        # Quality and progress
        print(Template(Message.Provide).substitute(quality=totalQuality, progress=totalProgress))

        # Durability cost and time cost
        print(Template(Message.Cost).substitute(durability=totalDurability, time=totalSkillTime))

    # No valid skill in sequence
    else:
        print(Message.InputNotValid)
