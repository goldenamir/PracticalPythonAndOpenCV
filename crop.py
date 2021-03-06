#importing required libraries

import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument('-i','--image', required=True,
                help='Path to the image')

args = vars(ap.parse_args())

image = cv2.imread(args['image'])
cv2.imshow('original', image)

cropped = image[30:120, 240:335] # start y, end y, start x, end x
cv2.imshow('T-Rex face', cropped)
cv2.waitKey(0)

