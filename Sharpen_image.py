import cv2
import numpy as np
def sharpen(image):
    kernel= np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
    new_image= cv2.filter2D(image, -1, kernel)
    cv2.imshow('Sharpened', new_image)
    cv2.waitKey(0)
    return new_image

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

filename, new_image= resize('cats.jpeg', 1280, 960)
image= sharpen(new_image)