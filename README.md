# ffxiv-repeat-recent-crafting

Generate crafting macro from recent crafting log.

- Read crafting log from clipboard
- Parse and generate crafting macro, copy to clipboard
- Report how much quality, progress is provided
- Report how much durability, time is costed
- Warn if this macro exceeds 15 line limit

## How to use

1. Duplicate `Config\SettingExample.py` as `Config\Setting.py`  
   and change variable depending on your environment.
1. The program use regex for match skill name or statistics.  
   therefor same code base can support different game language.  
   However, a little bit understanding of regex is needed to create your own match rule.  
   Website like https://regexr.com can speed up this progress.
