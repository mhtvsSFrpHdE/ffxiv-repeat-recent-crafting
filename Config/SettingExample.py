# GCD skill
# These skill cost 3 seconds to cast during macro
GcdSkillRegex = "(?<=发动“)(.*)(?=”)"
GcdSkillCastCost = "3"

# oGCD skill
# These skill cost 2 seconds to cast during macro
oGcdSkillRegex = r"(?<=的)([^“”\n]*)(?=  )"
oGcdSkillCastCost = "2"

# Quality
QualityRegex = r"(?<=品质上升了 )(.*)(?=点)"

# Durability cost
DurabilityCostRegex = r"(?<=耐久降低了 )(.*)(?=点)"

# Progress
ProgressRegex = r"(?<=作业进展了 )(.*)(?=点)"

# Macro size
# In Final Fantasy XIV, each macro has a maximum size of 15 lines by default.
MacroSize = 15
