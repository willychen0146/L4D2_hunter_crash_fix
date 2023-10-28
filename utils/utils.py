import vpk
import os
import argparse
from tqdm import tqdm

# extract vpk file into writable vmt file
def extract_vpk(input_file_path, output_file_path):
    # get target vpk file
    pak = vpk.open(input_file_path)

    for filepath in pak:
        # get every file in vpk
        pakfile = pak.get_file(filepath)
        print(filepath)

        # create output file path
        output_filepath = os.path.join(output_file_path, filepath)
        os.makedirs(os.path.dirname(output_filepath), exist_ok=True)

        # save file to the output path
        pakfile.save(output_filepath)
        print(f"Extracted: {filepath}")

    print("Extraction complete")

# process vmt file to fix the crash
def process_vmt_file(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    modified_lines = []
    for line in lines:
        if line.strip().startswith('//"$nodecal"'):
            modified_lines.append(line.replace('//', '', 1)) 
        else:
            modified_lines.append(line)

    with open(file_path, 'w') as f:
        f.writelines(modified_lines)

def process_vmt_folder(folder_path):
    for root, _, files in os.walk(folder_path):
        for file in tqdm(files, desc="Processing VMT files"):
            if file.lower().endswith('.vmt'):
                file_path = os.path.join(root, file)
                process_vmt_file(file_path)

# compact all element in the folder back into vpk file
def compact_vpk(input_file_path, output_file_path):
    # collect all file in target folder, and compact into vpk file
    newvpk = vpk.new(input_file_path)
    newvpk.save(output_file_path)
    print("Compact complete")
