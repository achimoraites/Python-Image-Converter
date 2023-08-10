from datetime import datetime
import argparse

#TODO use the extension argument of the command everywhere

# All images are converted to jpg

# Keeping the output cleaned 
screenLock = Semaphore(value=1)

# where to save our images
directory = "converted"

#region move to utils.py
# create a message function
def message(file, converted):
    screenLock.acquire()
    # if is converted
    if converted:
        print(datetime.now().time().strftime('%H:%M:%S') + " Converted:  " + file)
    else:
        print(datetime.now().time().strftime('%H:%M:%S') + " Converting:  " + file)
    screenLock.release()


# create a directory if needed to store our converted images!
if not os.path.exists(directory):
    os.makedirs(directory)


# convert RAW images function
def convert_raw(file, srcDir, tgtDir, extension=".jpg"):
    # path = 'image.nef'
    try:
        ext = "."+file.split(".")[-1].lower()
        message(file, False)
        source = os.path.join(srcDir, file)
        with rawpy.imread(source) as raw:
            rgb = raw.postprocess()
        imageio.imsave(os.path.join(tgtDir, file.replace(ext,"") + extension), rgb)
        message(file, True)
    except:
        pass


# convert function
def convert_file(file, srcDir, tgtDir, extension=".jpg"):

    mappings = {
        '.jpg': 'JPEG',
        '.png': 'PNG',
    }
    save_format = mappings.get(extension, 'JPEG')
    try:
        ext = "."+file.split(".")[-1].lower()
        message(file, False)
        path = os.path.join(srcDir, file)
        im = Image.open(path)
        im.save(os.path.join(tgtDir, file.replace(ext,"") + extension), save_format)
        message(file, True)
    except:
        pass


# rename .ai 2 pdf and problem solved! 
def ai_2_pdf(file):
    if file.endswith('.ai'):
        os.rename(file, os.path.join(directory, file + '.pdf'))
        print(
            datetime.now().time().strftime('%H:%M:%S') + " Converted ai 2 pdf : " + os.path.join(directory, file + '.pdf'))


# IT IS POINTLESS TO CONVERT WHAT IS ALREADY CONVERTED!!!!
def image_not_exists(image,tgtDir):
    ext = image.split(".")[-1].lower()
    target = os.path.join(tgtDir, image.replace(ext, 'jpg'))
    if os.path.isfile(target):
        screenLock.acquire()
        print("File " + image + " is already converted! \n")
        screenLock.release()
        return False
    else:
        return True


# here we check each file to decide what to do		
def check_extension(file):
    # get the extension as a String and check if the string is contained in the array extensionsForRawConversion
    ext = "."+file.split(".")[-1].lower()
    # set supported raw conversion extensions!
    extensionsForRawConversion = ['.dng', '.raw', '.cr2', '.crw', '.erf', '.raf', '.tif', '.kdc', '.dcr', '.mos',
                                  '.mef', '.nef', '.orf', '.rw2', '.pef', '.x3f', '.srw', '.srf', '.sr2', '.arw',
                                  '.mdc', '.mrw']
    # set supported imageio conversion extensions
    extensionsForConversion = ['.ppm', '.psd', '.tif', '.webp']

    if ext in extensionsForRawConversion:
        return "RAW"
    if ext in extensionsForConversion:
        return "NOT RAW"
    # check if an .ai exists and rename it to .pdf	!
    ai_2_pdf(file)
  #endregion
  
import os
import sys
from utils import check_extension, convert_file, convert_raw, image_not_exists
import optparse
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
            for file in os.listdir(src):
                # CHECK IF WE HAVE CONVERTED THIS IMAGE! IF YES SKIP THE CONVERSIONS!
                if image_not_exists(file, tgtDir):
                    if "RAW" == check_extension(file):
                        executor.submit(
                            convert_raw,
                            file,
                            srcDir,
                            tgtDir,
                            options.target_image_extension,
                        )

                    if "NOT_RAW" == check_extension(file):
                        executor.submit(
                            convert_file,
                            file,
                            srcDir,
                            tgtDir,
                            options.target_image_extension,
                        )

        print(" \n Converted Images are stored at - > \n " + os.path.abspath(tgtDir))
    except:
        print(
            "\n The directory at : \n "
            + tgtDir
            + "\n Are you sure is there? \n I am NOT! \n It NOT EXISTS !! "
            "Grrrr....\n\n"
        )



if __name__ == "__main__":
    main()
