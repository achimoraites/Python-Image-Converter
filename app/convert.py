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
def message(file, bool):
    screenLock.acquire()
    # if is converted
    if bool:
        print(datetime.now().time().strftime('%H:%M:%S') + " Converted:  " + file)
    else:
        print(datetime.now().time().strftime('%H:%M:%S') + " Converting:  " + file)
    screenLock.release()


# create a directory if needed to store our converted images!
if not os.path.exists(directory):
    os.makedirs(directory)



# convert RAW images function
def convert_raw(file, directory, tgtDir):
    # path = 'image.nef'

    try:
        message(file, False)
        path = os.path.join(tgtDir, file)
        with rawpy.imread(path) as raw:
            rgb = raw.postprocess()
        imageio.imsave(os.path.join(directory, file + '.jpg'), rgb)
        message(file, True)
    except:
        pass

    try:
        message(file, False)
        path = os.path.join(tgtDir, file)
        with rawpy.imread(path) as raw:
            rgb = raw.postprocess()
        imageio.imsave(os.path.join(directory, file + '.png'), rgb)
        message(file, True)
    except:
        pass


# convert function
def convert_file(file, directory, tgtDir):
    try:
        message(file, False)
        path = os.path.join(tgtDir, file)
        im = Image.open(path)
        # basewidth = 2048
        # wpercent = (basewidth/float(im.size[0]))
        # hsize = int((float(im.size[1])*float(wpercent)))
        # im = im.resize((basewidth,hsize), Image.ANTIALIAS)
        im.save(os.path.join(directory, file + ".jpg"), "JPEG", dpi=(600, 600))
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
def checkExtension(ext):
    # set supported raw conversion extensions!
    extensionsForRawConversion = ['.dng', '.raw', '.cr2', '.crw', '.erf', '.raf', '.tif', '.kdc', '.dcr', '.mos',
                                  '.mef', '.nef', '.orf', '.rw2', '.pef', '.x3f', '.srw', '.srf', '.sr2', '.arw',
                                  '.mdc', '.mrw']
    # set supported imageio conversion extensions
    extensionsForConversion = ['.ppm', '.psd', '.tif']

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

    parser = optparse.OptionParser("usage: " + sys.argv[0] + \
                                   "\n-s <source directory> \n ex: usage%prog -s C:\\Users\\USerName\\Desktop\\Photos_Dir \n After -s Specify the directory you will convert")
    parser.add_option('-s', dest='nname', type='string', \
                      help='specify your source directory!')
    (options, args) = parser.parse_args()
    if (options.nname == None):
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
                if 'RAW' == checkExtension(file):
                    # Added multithreds to complete conversion faster
                    t2 = Thread(target=convert_raw, args=(file, directory, tgtDir))
                    t2.start();

                if 'NOT_RAW' == checkExtension(file):
                    t = Thread(target=convert_file, args=(file, directory, tgtDir))
                    t.start();
                if file.endswith('.tif'):
                    t = Thread(target=convert_file, args=(file, directory, tgtDir))
                    t.start();
        print(" \n Converted Images are stored at - > \n " + os.path.abspath(directory))
    except:
        print(
            "\n The directory at : \n " + tgtDir + "  \n Are you sure is there? \n I am NOT! \n It NOT EXISTS !! Grrrr....\n\n")


if __name__ == '__main__':
    main()
