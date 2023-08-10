from datetime import datetime
import os
import sys
from utils import check_extension, convert_file, convert_raw, image_not_exists
import optparse
import concurrent.futures


def main():
    # where to save our images
    directory = "converted"
    # create a directory if needed to store our converted images!
    if not os.path.exists(directory):
        os.makedirs(directory)

    print("### PYTHON IMAGE CONVERTER ### \n \n")

    parser = optparse.OptionParser(
        "usage: " + sys.argv[0] + "\n-s <source directory> \n ex: usage%prog --s "
        "C:\\Users\\USerName\\Desktop\\Photos_Dir \n After --s Specify the directory you "
        "will convert"
    )
    parser.add_option(
        "--s", dest="nname", type="string", help="specify your source directory!"
    )
    parser.add_option(
        "--ext",
        dest="target_image_extension",
        type="choice",
        default=".jpg",
        choices=[".jpg", ".png"],
        help="the image format to be used for the converted images.",
    )
    (options, args) = parser.parse_args()
    if options.nname is None:
        print(parser.usage)
        exit(0)
    else:
        tgtDir = os.path.abspath(options.nname)

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
