# Python Image Converter
[![PyPI version](https://badge.fury.io/py/raw-image-converter.svg)](https://pypi.org/project/raw-image-converter/)
[![All Contributors](https://img.shields.io/github/all-contributors/achimoraites/Python-Image-Converter?color=ee8449&style=flat-square)](#contributors)


The Python Image Converter is a user-friendly CLI tool designed for hassle-free batch conversion of image files.

## Features
- **Bulk Conversion:** Say goodbye to the tedious one-by-one image conversion. Convert hundreds of images at once.
- **Supported File Types:** DNG, CR2, CRW, NEF, PEF, ERF, ORF, PPM, MOS, MRF, MRW, SRW, PSD, TIF, and more.
- **Fast:** Multi-core support.
- **Customizable Output:** Specify your converted images' output directory, resolution, and format

## Install

### Using pip (recommended)
```bash
$ pip3 install raw_image_converter
```

### Running it from the repo 

```bash
 git clone https://github.com/achimoraites/Python-Image-Converter.git [my-app-name]
 cd [my-app-name]

 pip install -r requirements.txt

 python -m raw_image_converter --s <Enter-Path-Of-Directory>
```
## Example usage

### Arguments
- `-s, --src` (required): set the path to the directory you want to convert (source)! 
- `-t, --tgt`: where to store the converted images (target); by default, they are stored in the "converted" folder. 
- `-d, --delete-source-directory`: removes the directory with the original images (source).
- `-r, --resolution`: allows to set the converted image resolutions; you can use numbers or percentages: e.g., 75% -> width and height are 75% of the original size, 1000,1500 -> width to 1000px and the height to 1500px
- `-e, --ext`: specify the output image format for the converted images; by default, it is JPG. Valid options are:
    - `.jpg`
    - `.png`

```
 # simple usage
 raw_image_converter -s <Enter-Path-Of-Directory>

 # set a custom target image format
 raw_image_converter --s <Enter-Path-Of-Directory> --ext '.png'

 # Advanced usage 1
 raw_image_converter -s images -t converted/png -r 25% -e .png -d

 # Set custom resolution 1
 raw_image_converter -s images -t converted/jpg -r 1024,768

 # Set custom resolution 2
 raw_image_converter -s images -t converted/jpg -r 50%,33%
```


And you are done! 

## ScreenShot
<img src='https://raw.githubusercontent.com/achimoraites/Python-Image-Converter/master/sample.png' alt='Python Image Converter'>


## Contributors

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->