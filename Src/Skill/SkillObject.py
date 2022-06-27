from string import Template

class Skill:
    def __init__(self, setting, skillName, castCostInSec):
        self.Setting = setting
        self.SkillName = skillName
        self.CastCost = castCostInSec

    def ToMacroString(self):
        # Paste "\n" string directly will not work
        macroTemplate = Template("/ac $skillName<wait.$castCost>" + self.Setting.NewLineInResult)

        return macroTemplate.substitute(skillName=self.SkillName, castCost=self.CastCost)
