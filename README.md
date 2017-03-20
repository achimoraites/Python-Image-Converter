# Python-Image-Converter

### Not supported formats :
CRW , PEF , ORF , CR2 , MRW .
## This is a simple Image converter written in Python
The app is using PIL , you simply put the convert.py in the folder you want to convert set the options 
and the app will convert all the selected files to jpeg . I wrote this app to convert multiple image files
as fast as possible.
### Before you can use it Install Image

</br> pip install Image 

### Example usage

</br> open the command line and go to the folder containing images you want to convert:
C:\Users\Toula\Desktop\Photos_for_conversion> </br>
copy the convert.py in the folder </br>
Edit the file to customise your conversion: </br>
# set the extension of files to be converted 
fileExtension = '.IIQ' </br>
The extension sould be set to the filetype of images to be converted </br>
in line 19 you will find : </br>
basewidth = 2048 </br>
Change it to set the image size ,
if you want a thumbnail you can set it to 200 and the proportions are automatically calculated!</br>
save your changes !!!


### Now lets convert!
Run the convert.py :  </br>
C:\Users\Toula\Desktop\Photos_for_conversion>python convert.py </br>
The application will create a folder converted where all your converted images are located!
</br>
And you are done! 


