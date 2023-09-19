import sys
from PIL import Image
import os
import rawpy
import imageio
from datetime import datetime


def message(file, converted):
    # if conversion finished
    if converted:
        print(datetime.now().time().strftime("%H:%M:%S") + " Converted:  " + file)
    # if conversion failed
    else:
        print(
            datetime.now().time().strftime("%H:%M:%S")
            + " Conversion failed for File:  "
            + file
        )


# convert RAW images function
def convert_raw(file, srcDir, tgtDir, extension=".jpg"):
    try:
        ext = "." + file.split(".")[-1].lower()
        print(datetime.now().time().strftime("%H:%M:%S") + " Converting:  " + file)
        source = os.path.join(srcDir, file)
        with rawpy.imread(source) as raw:
            rgb = raw.postprocess()
        imageio.imsave(os.path.join(tgtDir, file.replace(ext, "") + extension), rgb)
        message(file, True)
    except Exception as e:
        print(e)
        message(file, False)
        pass


# convert function
def convert_file(file, srcDir, tgtDir, extension=".jpg"):
    mappings = {
        ".jpg": "JPEG",
        ".png": "PNG",
    }
    save_format = mappings.get(extension, "JPEG")
    try:
        ext = "." + file.split(".")[-1].lower()
        message(file, False)
        path = os.path.join(srcDir, file)
        im = Image.open(path)
        im.save(os.path.join(tgtDir, file.replace(ext, "") + extension), save_format)
        message(file, True)
    except:
        pass


# rename .ai 2 pdf and problem solved!
def ai_2_pdf(file):
    if file.endswith(".ai"):
        os.rename(file, os.path.join(directory, file + ".pdf"))
        print(
            datetime.now().time().strftime("%H:%M:%S")
            + " Converted ai 2 pdf : "
            + os.path.join(directory, file + ".pdf")
        )


# IT IS POINTLESS TO CONVERT WHAT IS ALREADY CONVERTED!!!!
def image_not_exists(image, tgtDir,tgtExt):
    ext = image.split(".")[-1].lower()
    target = os.path.join(tgtDir, image.replace(ext, tgtExt.replace(".","")))
    if os.path.isfile(target):
        return False
    else:
        return True


# here we check each file to decide what to do
def check_extension(file):
    # get the extension as a String and check if the string is contained in the array extensionsForRawConversion
    ext = "." + file.split(".")[-1].lower()
    # set supported raw conversion extensions!
    extensionsForRawConversion = [
        ".dng",
        ".raw",
        ".cr2",
        ".crw",
        ".erf",
        ".raf",
        ".tif",
        ".kdc",
        ".dcr",
        ".mos",
        ".mef",
        ".nef",
        ".orf",
        ".rw2",
        ".pef",
        ".x3f",
        ".srw",
        ".srf",
        ".sr2",
        ".arw",
        ".mdc",
        ".mrw",
    ]
    # set supported imageio conversion extensions
    extensionsForConversion = [".ppm", ".psd", ".tif", ".webp"]

    if ext in extensionsForRawConversion:
        return "RAW"
    if ext in extensionsForConversion:
        return "NOT RAW"
    # check if an .ai exists and rename it to .pdf	!
    ai_2_pdf(file)
