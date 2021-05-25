# importing required libraries

import numpy as np
import cv2 

def translate(image, x, y): 
    M = np.float32([[1,0,x],[0,1,y]])
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

    return shifted


'''

how we can use this function?

shiftted = imutils.translate(image, 0, 100)
cv2.imshow('shifted down', shifted)
cv2.waitKey(0)

'''

def rotate(image, angle, center = None, scale=1.0):
    (h, w) = image.shape[:2]

    if center is None:
        center = (w//2, h//2)

    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M,(w, h))

    return rotated

'''

how we can use this function?

rotated = imutils.rotate(image,180)
cv2.imshow('Rotated by 180 degrees', rotated)
cv2.waitKey(0)

'''

def resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image

    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)

    else:
        r = width / float(w)
        dim = (width, int(w * r))

    resized = cv2.resize(image,dim, interpolation = inter)

    return resized

    