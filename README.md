# obsidian-todo
Pure text todo list solution.

- Reset checkbox status when a new day come
- Open different obsidian document everyday in a week

## How to use

1. Duplicate `Config\ObsidianFilePathExample.py` as `Config\ObsidianFilePath.py`  
and change variable depending on your environment.
1. Duplicate `Config\SettingExample.py` as `Config\Setting.py`  
and change variable depending on your environment.
1. Run `pythonw main.py` under `main.py` folder,  
Obsidian will open and show today's note.  
If use python`w`, console will not show.

## Important

`ObsidianFilePath.py\everydayTemplate` file will copy and override to `ObsidianFilePath.py\everyday`,  
if you don't want this, create two dummy file to avoid error.
