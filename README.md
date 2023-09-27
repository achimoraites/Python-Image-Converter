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

```
 # simple usage
 raw_image_converter --s <Enter-Path-Of-Directory>

 # set a custom target image format
 raw_image_converter --s <Enter-Path-Of-Directory> --ext '.png'
```
- The --s argument is where you set the path to the directory you want to convert! 
- The --ext argument is where you specify the image format that will be used for the converted images; by default the `.jpg` is used. valid options are:
    - `.jpg`
    - `.png`

The application will create a folder 'converted' where all your converted images are located!

And you are done! 

## ScreenShot
<img src='https://raw.githubusercontent.com/achimoraites/Python-Image-Converter/master/sample.png' alt='Python Image Converter'>

