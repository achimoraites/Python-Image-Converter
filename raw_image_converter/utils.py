from PIL import Image
import os
import rawpy
import imageio
from datetime import datetime


# create a message function
def message(file, converted):
    # if is converted
    if converted:
        print(datetime.now().time().strftime('%H:%M:%S') + " Converted:  " + file)
    else:
        print(datetime.now().time().strftime('%H:%M:%S') + " Converting:  " + file)


# convert RAW images function
def convert_raw(file, directory, tgtDir, extension=".jpg"):

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
def ai_2_pdf(e, directory):
    if e.endswith('.ai'):
        os.rename(e, os.path.join(directory, e + '.pdf'))
        print(
            datetime.now().time().strftime('%H:%M:%S') + " Converted ai 2 pdf : " + os.path.join(directory, e + '.pdf'))


# IT IS POINTLESS TO CONVERT WHAT IS ALREADY CONVERTED!!!!
def image_not_exists(e, directory):
    if os.path.isfile(os.path.join(directory, e + '.jpg')):
        print("File " + e + " is already converted! \n")
        return False
    else:
        return True


# here we check each file to decide what to do		
def check_extension(ext, directory):
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
    ai_2_pdf(ext, directory)