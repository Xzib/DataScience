'''
This program look for .jpg image files in the root dir
and resize them to 800x800 pixels and add them to the 
numpy array named 'img_array', makes a new directory 'resized_images'
in the root and add all the resized images to that directory

'''

import numpy as np
from matplotlib import pyplot as plt
import os 
from PIL import Image

#Root directory
root = '.'

'''
change this path to your directory
'''
folder_path = 'D:\\zohaib\\piaic\\data_science\\ai_anees_ahmed\\image_into_array\\resize_image\\'
#image array
img_array = np.zeros([20,800,800,3])
# tuple for resizing the images 'wxh'
size = 800, 800
count = 0  
new_dir = 'resize_image'  
if not(new_dir in os.listdir(root)):
    os.mkdir(f'.\\{new_dir}') 
#Looking for .jpg files in the root and all sub directories
print("Looking for .jpg files. please wait...")
for subdirs, dirs, files in os.walk(root): 
    #print("inside folder..")
    #print(os.listdir())  
    for file in files:
        #print("files..")
        #print(os.listdir())
        filepath = subdirs + os.sep + file
        #print(filepath)
        if filepath.endswith('.jpg') and count != 20:
            #print("inside if...")
            #image = plt.imread(filepath)         
            im = Image.open(filepath).resize(size)
            im.save(folder_path+str(count)+'.jpg','JPEG')
            #im_resize = im.resize(size)
            #making a new folder for resized files and saving the resized files  
            img_array[count]=im
            #print(img_array[count].shape)
            count += 1
print(type(img_array))
print(img_array.shape)
print(img_array[:6,:200,:200,:3]) 
