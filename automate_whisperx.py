import subprocess
import shutil
import os
import os.path
from argparse import ArgumentParser


def run_whisperx(filename, indirectory, outdirectory): 
    filepath = os.path.join(indirectory, filename)
    file_subdirectory = os.path.splitext(os.path.join(outdirectory, filename))[0]
    os.mkdir(file_subdirectory)
    subprocess.run(f"whisperx {filepath} --compute_type float32 --model large --output_format srt --language en --output_dir {file_subdirectory}")
    shutil.move(filepath, file_subdirectory)
    #creates subdirectory for each a/v file, runs whisperx command w/ parameters, moves a/v file + srt to matching subdirectory


def process_files(indirectory, outdirectory):
    indirectory_contents = os.listdir(indirectory)
    for child in indirectory_contents:
            run_whisperx(child, indirectory, outdirectory)
#loops through all the A/V files in the input directory


if __name__=="__main__":
    parser = ArgumentParser(prog='autowhisperx', description="This script is a wrapper for the WhisperX command line tool. It batch processes a/v files in an input directory, generates transcripts, and moves all files to an output directory.")
    parser.add_argument("-i", "--indirectory", help="Input directory containing the A/V files.")
    parser.add_argument("-o", "--outdirectory", help="Output directory where A/V files + generated transcripts are moved to.")
    args = parser.parse_args()
    if args.indirectory or args.outdirectory is None: 
        print("please include -i and -o arguments to specify input/output directories!")
        exit()
    elif args.indirectory == args.outdirectory:
        print("Input/Output directories must be different from each other!")
        exit()
    elif not os.path.exists(args.indirectory):
        print("The input directory does not exist!")
        exit()
    elif not os.path.exists(args.outdirectory):
        print("The output directory does not exist!")
        exit()
    process_files(args.indirectory, args.outdirectory)
#Runs script, requires input/output directories as arguments, checks to make sure directories actually exist
    
