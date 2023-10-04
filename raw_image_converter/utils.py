from PIL import Image
import os
import numpy as np
import rawpy
import imageio
from datetime import datetime
import shutil

def split_file_extension(file):
    return os.path.splitext(file)

def message(file, converted):
    current_time = datetime.now().time().strftime("%H:%M:%S")
    # if conversion finished
    if converted:
        print(f"{current_time} Converted: {file}")
    # if conversion failed
    else:
        print(f"{current_time} Conversion failed for File: {file}")


# convert RAW images function
def convert_raw(file, srcDir, tgtDir, extension=".jpg", resolution=("100%", "100%")):
    try:
        filename, _ = split_file_extension(file)
        print(datetime.now().time().strftime("%H:%M:%S") + " Converting:  " + file)
        source = os.path.join(srcDir, file)
        with rawpy.imread(source) as raw:
            rgb = raw.postprocess()
        if resolution:
            pil_image = Image.fromarray(rgb)

            # Resize the image
            width = calculate_image_dimension(pil_image.width, resolution[0])
            height = calculate_image_dimension(pil_image.height, resolution[1])
            pil_image = pil_image.resize((width, height))

            rgb = np.array(pil_image)
        imageio.imsave(os.path.join(tgtDir, filename + extension), rgb)
        message(file, True)
    except Exception as e:
        print(e)
        message(file, False)
        pass


def calculate_image_dimension(dimension, resolution):
    if "%" in resolution:
        factor = float(resolution.strip("%").strip()) / 100.0
        result = int(dimension * factor)
    else:
        result = int(resolution)
    return result


# convert function
def convert_file(file, srcDir, tgtDir, extension=".jpg", resolution=("100%", "100%")):
    mappings = {
        ".jpg": "JPEG",
        ".png": "PNG",
    }
    save_format = mappings.get(extension, "JPEG")
    try:
        filename, _ = split_file_extension(file)
        message(file, False)
        path = os.path.join(srcDir, file)
        im = Image.open(path)
        if resolution:
            width = calculate_image_dimension(im.width, resolution[0])
            height = calculate_image_dimension(im.height, resolution[1])
            im = im.resize((width, height))
        im.save(os.path.join(tgtDir, filename + extension), save_format)
        message(file, True)
    except:
        pass


# rename .ai 2 pdf and problem solved!
def ai_2_pdf(file):
    if file.endswith(".ai"):
        os.rename(file, os.path.join(file + ".pdf"))
        print(
            datetime.now().time().strftime("%H:%M:%S")
            + " Converted ai 2 pdf : "
            + os.path.join(file + ".pdf")
        )


# IT IS POINTLESS TO CONVERT WHAT IS ALREADY CONVERTED!!!!
def image_not_exists(image, tgtDir, tgtExt):
    filename, _ = split_file_extension(image)
    target = os.path.join(tgtDir, filename + tgtExt)
    if os.path.isfile(target):
        return False
    else:
        return True


# here we check each file to decide what to do
def check_file_type(file):
    # get the extension as a String and check if the string is contained in the array extensionsForRawConversion
    _, ext = split_file_extension(file)
    # set supported raw conversion extensions!
    raw = [
        ".dng",
        ".raw",
        ".cr2",
        ".crw",
        ".erf",
        ".raf",
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
    not_raw = [".ppm", ".psd", ".tiff", ".webp"]

    if ext in raw:
        return "RAW"
    if ext in not_raw:
        return "NOT RAW"
    # check if an .ai exists and rename it to .pdf	!
    ai_2_pdf(file)


def delete_directory(dir):
    try:
        shutil.rmtree(dir)
        print(f"Removed source directory {dir}")
    except OSError as o:
        print(f"Error, {o.strerror}: {dir}")
