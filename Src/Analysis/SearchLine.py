import Src.Analysis.RegexObject as RegexObject
import Src.Analysis.Enum as Enum

# Return "True, Type, Content" or "False, None, None"


def Search(setting, line):
    # Find Gcd skill
    search = RegexObject.Regex(setting.GcdSkillRegex, line).GetResult()
    if search[0] is True:
        return True, Enum.SearchTypeEnum.GcdSkill, search[1].group()

    # Find oGcd skill
    search = RegexObject.Regex(setting.oGcdSkillRegex, line).GetResult()
    if search[0] is True:
        return True, Enum.SearchTypeEnum.oGcdSkill, search[1].group()

    # Find Durability cost
    search = RegexObject.Regex(setting.DurabilityCostRegex, line).GetResult()
    if search[0] is True:
        return True, Enum.SearchTypeEnum.DurabilityCost, int(search[1].group())

    # Find Quality
    search = RegexObject.Regex(setting.QualityRegex, line).GetResult()
    if search[0] is True:
        return True, Enum.SearchTypeEnum.Quality, int(search[1].group())

    # Find Progress
    search = RegexObject.Regex(setting.ProgressRegex, line).GetResult()
    if search[0] is True:
        return True, Enum.SearchTypeEnum.Progress, int(search[1].group())

    return False, None, None
