import pyperclip
import io

import Src.Analysis.SearchLine as SearchLine
import Src.Analysis.Enum as Enum
import Src.Skill.SkillObject as SkillObject

# Return skillSequence, totalQuality, totalDurability, totalProgress


def Read(setting):
    # Paste
    _copiedCraftHistory = pyperclip.paste()

    # Convert pasted string to read line buffer
    _readLineBuffer = io.StringIO(_copiedCraftHistory)

    # Search result collection
    skillSequence = []
    totalQuality = 0
    totalDurability = 0
    totalProgress = 0

    # One line at a time, until no more data
    while True:
        # Get line
        line = _readLineBuffer.readline()

        # Stop loop without search if no more data
        if line == "":
            break

        # Has content, do search
        search = SearchLine.Search(setting, line)

        # Find something
        hasResult = search[0]
        resultType = search[1]
        result = search[2]

        # Skip to next line if no match
        if hasResult is False:
            continue

        # Action to result depending on result type
        if resultType == Enum.SearchTypeEnum.GcdSkill:
            skillSequence.append(SkillObject.Skill(result, setting.GcdSkillCastCost))
        if resultType == Enum.SearchTypeEnum.oGcdSkill:
            skillSequence.append(SkillObject.Skill(result, setting.oGcdSkillCastCost))
        if resultType == Enum.SearchTypeEnum.Quality:
            totalQuality += result
        if resultType == Enum.SearchTypeEnum.DurabilityCost:
            totalDurability += result
        if resultType == Enum.SearchTypeEnum.Progress:
            totalProgress += result

    # Done search loop, return result collection
    return skillSequence, totalQuality, totalDurability, totalProgress
