import subprocess
import shutil
import os
import os.path
import mimetypes
from argparse import ArgumentParser


def run_whisperx(filename, indirectory, outdirectory): 
    filepath = os.path.join(indirectory, filename)
    if outdirectory != "": 
        file_subdirectory = os.path.splitext(os.path.join(outdirectory, filename))[0]
        os.mkdir(file_subdirectory)
    else: 
        file_subdirectory = os.path.splitext(os.path.join(indirectory, filename))[0]
        os.mkdir(file_subdirectory)
    #allows for optional output directory, will create subdirectories in either in/out directory
    if str(os.name)=="posix":
        #checks posix or unix operating system -- require different command line syntax
        subprocess.run([f"whisperx {filepath} --compute_type float32 --output_format srt --language en --output_dir {file_subdirectory}"], capture_output=True, shell=True)
    else: 
        subprocess.run(f"whisperx {filepath} --compute_type float32 --output_format srt --language en --output_dir {file_subdirectory}")
    shutil.move(filepath, file_subdirectory)
    #creates subdirectory for each a/v file, runs whisperx command w/ parameters, moves a/v file + srt to matching subdirectory


def process_files(indirectory, outdirectory):
    indirectory_contents = os.listdir(indirectory)
    for child in indirectory_contents:
        mimetypes.init()
        mimetype = (mimetypes.guess_type(child))[0]
        if mimetype != None: 
            mimetype = mimetype.split('/')[0]
        if mimetype in ['audio', 'video']:
            run_whisperx(child, indirectory, outdirectory)
#iterates through each file in directory, determines mimetype, only runs whisperx on audio and video files 

if __name__=="__main__":
    parser = ArgumentParser(prog='autowhisperx', description="This script is a wrapper for the WhisperX command line tool. It batch processes a/v files in an input directory, generates transcripts, and moves all files to an output directory.")
    parser.add_argument("-i", "--indirectory", help="Input directory containing the A/V files.")
    parser.add_argument("-o", "--outdirectory", help="(Optional) Output directory where A/V files + generated transcripts are moved to.", default = "")
    args = parser.parse_args()
    if args.indirectory and args.outdirectory is not None: 
        if args.indirectory == args.outdirectory:
            print("Input/Output directories must be different from each other!")
            exit()
        elif not os.path.exists(args.indirectory):
            print("The input directory does not exist!")
            exit()
        process_files(args.indirectory, args.outdirectory)
    else: 
        print("please run this program with -i and -o arguments")
#Runs script, requires input/output directories as arguments, checks to make sure directories actually exist

