# Python Image Converter
[![PyPI version](https://badge.fury.io/py/raw-image-converter.svg)](https://pypi.org/project/raw-image-converter/)


## This is a simple Image converter written in Python
The app is using PIL ,rawpy and imageio . 
Files are converted to .jpg format 

## Convert for FREE multiple image files
I saw all kinds of software out there but when you have hundrends of raw images is tedious to convert 
one by one! Other Options were to get program suits like photoshop or even pay! 
# Notes
The .ai files are renamed as .pdf and moved to the converted directory !!! 


# What files can be used ?
### DNG , CR2 , CRW, NEF , PEF, ERF , ORF , PPM , MOS , MRF , MRW , SRW and more!!!
Personally i convert a lot of .psd , .TIF and .dng files !!! 
## Speed
This script is multithreaded and checks if you have already converted an image!

## Install

### Using pip (recommended)
```bash
$ pip3 install raw_image_converter
```

### Running it from the repo
In that case using an virtual environment is recommended

```bash
 git clone https://github.com/achimoraites/Python-Image-Converter.git [my-app-name]
 cd [my-app-name]

 pip install -r requirements.txt

 python -m raw_image_converter --s <Enter-Path-Of-Directory>
```
## Example usage

### Arguments
- `-s, --src` (required): set the path to the directory you want to convert (source)! 
- `-t, --tgt`: where to store the converted images (target), by default they are stored in the "converted" folder. 
- `-d, --delete-source-directory`: removes the directory with the original images (source) 
- `-r, --resolution`: Allows to set the converted image resolutions, you can use numbers or percentages: eg 75% -> width and height are 75% of the original size, 1000,1500 sets the width to 1000px and the height to 1500px
- `-e, --ext`: specify the converted image format that will be used for the converted images; by default the `.jpg` is used. valid options are:
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

