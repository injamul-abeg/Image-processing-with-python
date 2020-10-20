import cv2
def resize(fname, width, height):
    image =cv2.imread(fname)
    cv2.imshow('Original image', image)
    cv2.waitKey(0)

    org_height, org_width = image.shape[0:2]
    print("Width",org_width )
    print("Height", org_height)
    if org_width >= org_height :
        new_image = cv2.resize(image, (width, height))
    else:
        new_image = cv2.resize(image, (height,width))
    return fname, new_image

filename, new_image= resize('cats.jpeg', 1280, 960)
cv2.imshow('resized image', new_image)
cv2.waitKey(0)
new_height, new_width = new_image.shape[0:2]
print("New Width",new_width )
print("New Height", new_height)