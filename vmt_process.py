import os
import argparse
from tqdm import tqdm

# set argument
parser = argparse.ArgumentParser(description="Process VMT files to remove //\"$nodecal\" comments.")
parser.add_argument("--input", default=os.getcwd(), help="Path to the target folder containing VMT files.")
args = parser.parse_args()
target_folder = args.input

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

if __name__ == "__main__":
    process_vmt_folder(target_folder)
    print("All VMT files processed.")