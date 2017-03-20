from PIL import Image
import os
from threading import *
import optparse

# Keeping the output cleaned 
screenLock = Semaphore(value=1)

# set the extension of files to be converted
fileExtension = '.pdf'
# where to save our images
directory = "converted"
# create a directory if needed to store our converted images
if not os.path.exists(directory):
    os.makedirs(directory)

# convert function
def convert_file(file,directory):
	try:
		im = Image.open(file)
		#basewidth = 2048
		#wpercent = (basewidth/float(im.size[0]))
		#hsize = int((float(im.size[1])*float(wpercent)))
		#im = im.resize((basewidth,hsize), Image.ANTIALIAS)
		im.save(directory +'/' + file + ".jpg", "JPEG",dpi=(600,600))
		screenLock.acquire()
		print file + " Converted! \n"
		screenLock.release()
	except:
		pass



def main():
	parser = optparse.OptionParser('### PYTHON IMAGE CONVERTER ### \n'+
	'Place this script inside the folder you want to convert \n' +
	"\n usage%prog "+ \
	"-f <file type>" + '\n\n' + 'Convert all the .dng images example : \n\n convert.py -f .dng')
	parser.add_option('-f', dest='fileType', type='string',\
	help='specify file type of files to convert ex: .dng ')
	(options, args) = parser.parse_args()
	if (options.fileType == None):
		print parser.usage
		exit(0)
	else:
		fileType = options.fileType
		
	
	# find files to convert
	
	
		for file in os.listdir('.'):
			if file.endswith(fileType.lower()) | file.endswith(fileType.upper()):
				#print(os.path.join("Converting :" + directory + '/', file))
				# Added multithreds to complete conversion faster
				t = Thread(target = convert_file, args = (file,directory))
				t.start();
				#convert_file(file)
			
	
if __name__ == '__main__':
		main()
