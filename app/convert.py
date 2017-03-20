from PIL import Image
import os
from threading import *

# Keeping the output cleaned 
screenLock = Semaphore(value=1)

# set the extension of files to be converted
fileExtension = '.IIQ'
# where to save our images
directory = "converted"
# create a directory if needed to store our converted images
if not os.path.exists(directory):
    os.makedirs(directory)

# convert function
def convert_file(file,directory):
	im = Image.open(file)
	basewidth = 2048
	wpercent = (basewidth/float(im.size[0]))
	hsize = int((float(im.size[1])*float(wpercent)))
	im = im.resize((basewidth,hsize), Image.ANTIALIAS)
	im.save(directory +'/' + file + ".jpg", "JPEG")
	screenLock.acquire()
	print file + " Converted! \n"
	screenLock.release()

# find files to convert
for file in os.listdir("."):
    if file.endswith(fileExtension):
        #print(os.path.join("Converting :" + directory + '/', file))
        # Added multithreds to complete conversion faster
        t = Thread(target = convert_file, args = (file,directory))
        t.start();
        #convert_file(file)
