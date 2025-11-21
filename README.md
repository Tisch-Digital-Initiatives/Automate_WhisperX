# Automate_WhisperX

A wrapper for the WhisperX command line tool that can batch process multiple files in a directory. WhisperX generates an srt file for each a/v file in the batch and the script collocates the a/v file with the srt in a new subdirectory. 

This script takes two parameters: the input directory (required) containing the batch of files you want to process and the output directory (optional) if you want the new subdirectories to be created and srt files saved somewhere else. 

To use automate_whisperx.py, run the script in the command line with the arguments -i [input directory] and -o [output directory].

Automate_WhisperX requires [  WhisperX ](https://github.com/m-bain/whisperX) and its dependencies to be downloaded to run. 

