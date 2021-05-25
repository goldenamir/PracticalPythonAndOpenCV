# importing required libraries

import numpy as np
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument('-i','--image', required=True,
                help='Path to the image')

args = vars(ap.parse_args())

image = cv2.imread(args['image'])
cv2.imshow('original', image)

# resizing based on width
r = 150.0 / image.shape[1]
dim = (150, int(image.shape[0] * r)) # width to be 150 pixel 

resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
cv2.imshow('resized (width)', resized)

# resizing based on height
r = 50.0 . image.shape[0]
dim = (int(image.shape[1] * r), 50)

resized = cv2.resized(image, dim, interpolation = cv2.INTER_AREA)
cv2.imshow('resized (height)', resized)
cv2.waitKey(0)

