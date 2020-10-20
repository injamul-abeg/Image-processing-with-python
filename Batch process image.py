import cv2
import numpy as np
import sys
import os
import fnmatch

def resize(fname, width, height):
    image =cv2.imread(fname)
    cv2.imshow('Original image', image)
    cv2.waitKey(0)

    org_height, org_width = image.shape[0:2]
    if org_width >= org_height :
        new_image = cv2.resize(image, (width, height))
    else:
        new_image = cv2.resize(image, (height,width))
    return fname, new_image

listOfFiles= os.listdir('.')
pattern= "*.jpg"
n=len(sys.argv)
if n==3:
    width= int(sys.argv[1])
    height= int(sys.argv[2])
else :
    width=1280
    geight=960
if not os.path.exists('new folder'):
    os.makedirs('new folder')

for filename in listOfFiles:
     if fnmatch.fnmatch(filename, pattern):
         filename, new_image= resize(filename, width, height)
         cv2.imwrite("new folder\\",+filename, new_image)

