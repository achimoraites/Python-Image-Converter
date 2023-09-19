import sys
from PIL import Image
import os
import rawpy
import imageio
from datetime import datetime
import argparse
import concurrent.futures
from .utils import (message,convert_file,convert_raw,ai_2_pdf,
                   image_not_exists,check_extension)
from colorama import *
#TODO use the extension argument of the command everywhere

# All images are converted to jpg

# where to save our images
directory = "converted"

# create a directory if needed to store our converted images!
if not os.path.exists(directory):
    os.makedirs(directory)


def main():
    print('### PYTHON IMAGE CONVERTER ### \n \n')

    parser = argparse.ArgumentParser(description="Convert images to JPG")
    parser.add_argument('-s', "--src", dest = "src_dir",help='specify the source directory!', required=True) # this argument is required to start the conversion
    parser.add_argument("-t","--tgt", dest = "tgt_dir", help="specify the target directory!") # if there is no target directory given, the script will store the converted images in the source folder
    parser.add_argument('-e',"--ext", dest = "ext", default=".jpg", choices=['.jpg', '.png'],
                      help='the image format to be used for the converted images.')
    parser.add_argument("-f","--folder", dest = "seperate_folder", default=False, help="should the converted images be placed in a seperate folder")
    args = parser.parse_args()
    
    if args.tgt_dir == None:
        if args.seperate_folder:
            if not os.path.exists(args.src_dir + "/" + directory):
                os.makedirs(args.src_dir + "/" + directory)
            srcDir = args.src_dir
            tgtDir = args.src_dir + directory
        else:
            srcDir = args.src_dir
            tgtDir = args.src_dir
            
    else:
        if args.seperate_folder: # if the converted files should be stored in a seperate folder, create the folder and add the images to the folder
            if not os.path.exists(args.tgt_dir + "/" + directory):
                os.makedirs(args.tgt_dir + "/" + directory)
            srcDir = os.path.abspath(args.src_dir)
            tgtDir = os.path.abspath(args.tgt_dir + directory)
        else: # if the converted files sould be kept in the source folder, 
            srcDir = os.path.abspath(args.src_dir)
            tgtDir = os.path.abspath(args.tgt_dir)

    # find files to convert
        
    for file in os.listdir(srcDir):
       
            # CHECK IF WE HAVE CONVERTED THIS IMAGE! IF YES SKIP THE CONVERSIONS!
            #TODO also use the extension from the command as a parameter to the image_not_exists function
            if image_not_exists(file, tgtDir):
                if 'RAW' == check_extension(file):
                    # Added multithreading to complete conversion faster
                    t2 = Thread(target=convert_raw, args=(file, srcDir, tgtDir, args.ext))
                    t2.start()

                if 'NOT_RAW' == check_extension(file):
                    t = Thread(target=convert_file, args=(file, srcDir, tgtDir, args.ext))
                    t.start()
        
       
            #print(
           # "\n The directory at : \n " + srcDir + "\n Are you sure is there? \n I am NOT! \n It NOT EXISTS !! "
                                                  # "Grrrr....\n\n")
    print(" \n Converted Images are stored at - > " + os.path.abspath(tgtDir))   

if __name__ == "__main__":
    main()
