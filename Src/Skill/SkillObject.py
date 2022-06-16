from string import Template

class Skill:
    def __init__(self, skillName, castCostInSec):
        self.SkillName = skillName
        self.CastCost = castCostInSec

    def ToMacroString(self):
        macroTemplate = Template("/ac $skillName<wait.$castCost>\n")

        return macroTemplate.substitute(skillName=self.SkillName, castCost=self.CastCost)
