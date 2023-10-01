from datetime import datetime
import os
from raw_image_converter.utils import (
    check_extension,
    convert_file,
    convert_raw,
    image_not_exists,
    delete_directory,
)
import argparse
import concurrent.futures
from colorama import *

# TODO use the extension argument of the command everywhere


def main():
    print("### PYTHON IMAGE CONVERTER ### \n \n")

    parser = argparse.ArgumentParser(description="Convert images to JPG/PNG")
    parser.add_argument(
        "-s",
        "--src",
        dest="src_dir",
        help="specify the source directory!",
        required=True,
    )
    parser.add_argument(
        "-t",
        "--tgt",
        dest="tgt_dir",
        help="specify the target directory!",
        default="converted",
    )
    parser.add_argument(
        "-e",
        "--ext",
        dest="ext",
        default=".jpg",
        choices=[".jpg", ".png"],
        help="the image format to be used for the converted images.",
    )
    parser.add_argument(
        "--delete-source-directory",
        action="store_true",
        dest="delete_source_directory",
        default=False,
        help="Delete the source directory after the convesion",
    )

    args = parser.parse_args()

    srcDir = os.path.abspath(args.src_dir)
    tgtDir = os.path.abspath(args.tgt_dir)

    if not os.path.exists(tgtDir):
        os.makedirs(tgtDir)

    # find files to convert
    try:
        with concurrent.futures.ProcessPoolExecutor() as executor:
            print(
                "Started conversion at : "
                + datetime.now().time().strftime("%H:%M:%S")
                + "\n"
            )
            print("Converting -> " + srcDir + " Directory !\n")
            for file in os.listdir(srcDir):
                if image_not_exists(file, tgtDir, args.ext):
                    if "RAW" == check_extension(file):
                        executor.submit(
                            convert_raw,
                            file,
                            srcDir,
                            tgtDir,
                            args.ext,
                        )

                    if "NOT_RAW" == check_extension(file):
                        executor.submit(
                            convert_file,
                            file,
                            srcDir,
                            tgtDir,
                            args.ext,
                        )
                else:
                    print(
                        f"{Fore.GREEN}File "
                        + file
                        + f" is already converted!{Style.RESET_ALL}"
                        + " \n "
                    )

        print(
            f"{Fore.GREEN}Converted Images are stored at - > "
            + os.path.abspath(tgtDir)
            + f"{Style.RESET_ALL}"
        )

        if args.delete_source_directory:
            delete_directory(srcDir)

    except Exception as e:
        print(f"{Fore.RED}ERROR IN APPLICATION{Style.RESET_ALL}" + e)


if __name__ == "__main__":
    main()
