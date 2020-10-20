import cv2

def blur(image):
    kernels=[3,5,9,13]
    for index , k in enumerate(kernels):
        image_bl= cv2.blur(image, ksize=(k,k))
        cv2.imshow(str(k), image_bl)
        cv2.waitKey(0)
    return
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


blur(new_image)
