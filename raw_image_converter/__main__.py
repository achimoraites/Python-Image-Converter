from datetime import datetime
import os
import sys
from raw_image_converter.utils import check_extension, convert_file, convert_raw, image_not_exists
import argparse
import concurrent.futures


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


    print(
        "Started conversion at : " + datetime.now().time().strftime("%H:%M:%S") + "\n"
    )
    print("Converting \n -> " + tgtDir + " Directory !\n")
    # find files to convert
    try:
        with concurrent.futures.ProcessPoolExecutor() as executor:
            for file in os.listdir(tgtDir):
                # CHECK IF WE HAVE CONVERTED THIS IMAGE! IF YES SKIP THE CONVERSIONS!
                if image_not_exists(file, directory):
                    if "RAW" == check_extension(file, directory):
                        executor.submit(
                            convert_raw,
                            file,
                            directory,
                            tgtDir,
                            options.target_image_extension,
                        )

                    if "NOT_RAW" == check_extension(file, directory):
                        executor.submit(
                            convert_file,
                            file,
                            directory,
                            tgtDir,
                            options.target_image_extension,
                        )

        print(" \n Converted Images are stored at - > \n " + os.path.abspath(directory))
    except:
        print(
            "\n The directory at : \n "
            + tgtDir
            + "\n Are you sure is there? \n I am NOT! \n It NOT EXISTS !! "
            "Grrrr....\n\n"
        )


if __name__ == "__main__":
    main()
