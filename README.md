# L4D2-fix-tool

This project is aimed at solving the game crash problem caused by hunter pouncing on the player when there are too many mode is installed. Quick fix for too many indices for index buffer

## Require

```sh
pip install vpk
```

## Usage

Path may be in: 
```
"C:\Program Files (x86)\Steam\steamapps\common\Left 4 Dead 2\left4dead2\addons\workshop"
```

```sh
# unpack vpk binary file into vmt file
python extract_vpk.py --input {vpk_file_path} --output {output_path}

# fix the vmt
python vmt_process.py --input {file_path_from_the_previous_step}

# compack all file into vpk file (need to enter the {file_name}.vpk in the path)
python compact_vpk.py --input {file_path_from_the_previous_step} --output {original_vpk_path}
```

## Issue

TODO: This program currently only highly reduces the chance of crashing, but does not completely fix the issue.
