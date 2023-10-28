import vpk
import argparse
import os

# set argument
parser = argparse.ArgumentParser(description = "Extract files from a VPK archive.")
parser.add_argument("--input", default = "./test.vpk", help = "Path to the input VPK file")
parser.add_argument("--output", default = "./output/",help = "Directory where extracted files will be saved")
args = parser.parse_args()
input_file_path = args.input
output_file_path = args.output

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

if __name__ == "__main__":
    extract_vpk(input_file_path, output_file_path)