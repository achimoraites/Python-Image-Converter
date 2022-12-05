import sys
from PIL import Image
import os
from threading import *
import rawpy
import imageio
from datetime import datetime
import optparse

# All images are converted to jpg

# Keeping the output cleaned 
screenLock = Semaphore(value=1)

# where to save our images
directory = "converted"


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
def convert_raw(file, directory, tgtDir, extension=".jpg"):
    # path = 'image.nef'

    try:
        message(file, False)
        path = os.path.join(tgtDir, file)
        with rawpy.imread(path) as raw:
            rgb = raw.postprocess()
        imageio.imsave(os.path.join(directory, file + extension), rgb)
        message(file, True)
    except:
        pass


# convert function
def convert_file(file, directory, tgtDir, extension=".jpg"):
    mappings = {
        '.jpg': 'JPEG',
        '.png': 'PNG',
    }
    save_format = mappings.get(extension, 'JPEG')
    try:
        message(file, False)
        path = os.path.join(tgtDir, file)
        im = Image.open(path)
        im.save(os.path.join(directory, file + extension), save_format, dpi=(600, 600))
        message(file, True)

    except:
        pass


# rename .ai 2 pdf and problem solved! 
def ai_2_pdf(e):
    if e.endswith('.ai'):
        os.rename(e, os.path.join(directory, e + '.pdf'))
        print(
            datetime.now().time().strftime('%H:%M:%S') + " Converted ai 2 pdf : " + os.path.join(directory, e + '.pdf'))


# IT IS POINTLESS TO CONVERT WHAT IS ALREADY CONVERTED!!!!
def image_not_exists(e):
    if os.path.isfile(os.path.join(directory, e + '.jpg')):
        screenLock.acquire()
        print("File " + e + " is already converted! \n")
        screenLock.release()
        return False
    else:
        return True


# here we check each file to decide what to do		
def check_extension(ext):
    # set supported raw conversion extensions!
    extensionsForRawConversion = ['.dng', '.raw', '.cr2', '.crw', '.erf', '.raf', '.tif', '.kdc', '.dcr', '.mos',
                                  '.mef', '.nef', '.orf', '.rw2', '.pef', '.x3f', '.srw', '.srf', '.sr2', '.arw',
                                  '.mdc', '.mrw']
    # set supported imageio conversion extensions
    extensionsForConversion = ['.ppm', '.psd', '.tif', '.webp']

    for i in extensionsForRawConversion:
        if ext.lower().endswith(i):
            return 'RAW'

    for e in extensionsForConversion:
        if ext.lower().endswith(e):
            return 'NOT_RAW'
    # check if an .ai exists and rename it to .pdf	!
    ai_2_pdf(ext)


def main():
    print('### PYTHON IMAGE CONVERTER ### \n \n')

    parser = optparse.OptionParser("usage: " + sys.argv[0] +
                                   "\n-s <source directory> \n ex: usage%prog --s "
                                   "C:\\Users\\USerName\\Desktop\\Photos_Dir \n After --s Specify the directory you "
                                   "will convert")
    parser.add_option('--s', dest='nname', type='string', help='specify your source directory!')
    parser.add_option('--ext', dest='target_image_extension', type='choice',
                      default=".jpg", choices=['.jpg', '.png'],
                      help='the image format to be used for the converted images.')
    (options, args) = parser.parse_args()
    if options.nname is None:
        print(parser.usage)
        exit(0)
    else:
        tgtDir = os.path.abspath(options.nname)

    print("Started conversion at : " + datetime.now().time().strftime('%H:%M:%S') + '\n')
    print("Converting \n -> " + tgtDir + " Directory !\n")
    # find files to convert
    try:

        for file in os.listdir(tgtDir):
            # CHECK IF WE HAVE CONVERTED THIS IMAGE! IF YES SKIP THE CONVERSIONS!
            if image_not_exists(file):
                if 'RAW' == check_extension(file):
                    # Added multithreading to complete conversion faster
                    t2 = Thread(target=convert_raw, args=(file, directory, tgtDir, options.target_image_extension))
                    t2.start()

                if 'NOT_RAW' == check_extension(file):
                    t = Thread(target=convert_file, args=(file, directory, tgtDir, options.target_image_extension))
                    t.start()

        print(" \n Converted Images are stored at - > \n " + os.path.abspath(directory))
    except:
        print(
            "\n The directory at : \n " + tgtDir + "\n Are you sure is there? \n I am NOT! \n It NOT EXISTS !! "
                                                   "Grrrr....\n\n")


if __name__ == '__main__':
    main()
