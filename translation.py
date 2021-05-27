# importing required libraries

import numpy as np
import argparse
import imutils # this library is fantastic for translation, rotation and resizing
import cv2

ap = argparse.ArgumentParser()
ap.add_argument('-i','--image', required=True, 
                help = 'Path to the image')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
cv2.imshow('Original', image)

M = np.float32([[1,0,25],[0,1,50]])  # transition matrix M defined as a floating point array, the first row of the matrix is [1,0,tx] where tx 
                                     # is the number of pixels we will shift the image left or right.
                                     # negatie values of tx will shift the image to the left and positive values will shift the image to the right

                                    # [0,1,ty] where ty is the number of pixels we will shift the image up and down
                                    # negative value of ty will shift the image up and postive values will shift the image down
                                    
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow('shifted down and right', shifted)

M = np.float32([[1,0,-50],[0,1,-90]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow('shifted up and left', shifted)
