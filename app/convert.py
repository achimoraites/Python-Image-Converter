from PIL import Image
import os
from threading import *
import rawpy
import imageio
from datetime import datetime


# Keeping the output cleaned 
screenLock = Semaphore(value=1)

# set the extension of files to be converted
#fileExtension = '.pdf'
# where to save our images
directory = "converted"
# create a directory if needed to store our converted images
if not os.path.exists(directory):
    os.makedirs(directory)

# convert RAW function
def convert_raw(file,directory):
	#path = 'image.nef'
	screenLock.acquire()
	print datetime.now().time().strftime('%H:%M:%S') + " Raw conversion: " + file
	screenLock.release()
	try:
		path = file
		with rawpy.imread(path) as raw:
			rgb = raw.postprocess()
		imageio.imsave( directory +'\\' +file+'.png', rgb)
		screenLock.acquire()
		print datetime.now().time().strftime('%H:%M:%S') + " Converted:  " + directory +'\\' +file+'.png'
		screenLock.release()
		
	except:
		pass	

# convert function
def convert_file(file,directory):
	try:
		screenLock.acquire()
		print datetime.now().time().strftime('%H:%M:%S') + " Converting : "+file+"\n"
		screenLock.release()
		im = Image.open(file)
		#basewidth = 2048
		#wpercent = (basewidth/float(im.size[0]))
		#hsize = int((float(im.size[1])*float(wpercent)))
		#im = im.resize((basewidth,hsize), Image.ANTIALIAS)
		im.save(directory +'/' + file + ".jpg", "JPEG",dpi=(600,600))
		screenLock.acquire()
		print 'Converted : ' + datetime.now().time().strftime('%H:%M:%S') + ' ' + file + " \n"
		screenLock.release()
	
	except:
		pass
		
def main():
	print '### PYTHON IMAGE CONVERTER ### \n Place this script inside the folder you want to convert \n'
	# counter
	file_counter = 0;	
	print "Started conversion at : " + datetime.now().time().strftime('%H:%M:%S')+ '\n'
	# find files to convert
	
	
	for file in os.listdir('.'):
		
				
			if file.endswith('.psd') | file.endswith('.psd'.upper()):
				#print(os.path.join("Converting :" + directory + '/', file))
				# Added multithreds to complete conversion faster
				t2 = Thread(target = convert_file, args = (file,directory))
				t2.start();
				file_counter += 1
				
				#convert_file(file)
			if file.endswith('.py') | os.path.isdir(file):
				pass
			else:
				#convert_raw(file)
				t = Thread(target = convert_raw, args = (file,directory))
				t.start();
				file_counter += 1
				
	screenLock.acquire()
	print "\n\n Files Converting : " + str(file_counter) + '\n\n'
	screenLock.release()
	
if __name__ == '__main__':
		main()
