import vpk
import argparse
import os

# set argument
parser = argparse.ArgumentParser(description = "Extract files from a VPK archive.")
parser.add_argument("--input", default = "./output/", help = "Path to the folder you want to compact")
parser.add_argument("--output", default = "./output.vpk",help = "Path to the the compacted vpk file you want to save")
args = parser.parse_args()
input_file_path = args.input
output_file_path = args.output

def compact_vpk(input_file_path, output_file_path):
    # collect all file in target folder, and compact into vpk file
    newvpk = vpk.new(input_file_path)
    newvpk.save(output_file_path)
    print("Compact complete")

if __name__ == "__main__":
    compact_vpk(input_file_path, output_file_path)