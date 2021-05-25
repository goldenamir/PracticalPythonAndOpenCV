# importing required libraries
from __future__ import print_function
import argparse
import cv2


ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True,
                help='Path tot the image')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
cv2.imshow('Original', image)


# remember opencv represents images as NumPy arrays. This

(b,g,r) = image[0,0]
print('Pixel at (0,0) - Red :{}, Green:{}, Blue:{}'.format(r,g,b))

image[0,0] = (0,0,255)
(b,g,r) = image[0,0] # change the color to red on the top left pixel
print('Pixel at (0,0) - Red :{}, Green:{}, Blue:{}'.format(r,g,b))


# slicing capability
corner = image[0:100, 0:100] # Numpy expect for starting y to end y && start x and end x
cv2.imshow('Corner', corner)

image[0:100,0:100] = (0,255,0) # change the specific part of the image as Green

cv2.imshow('update', image)
cv2.waitKey(0)

