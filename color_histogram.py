# importing require libraries

from __future__ import print_function
from maplib import pyplot as plt
import numpy as np
import argparse
import cv2


ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True,
                help='path to the image')

args = vars(ap.parse())


image = cv2.imread(args.image)
cv2.imshow('original', image)


# splitting the channels
# SPLIT TO THREE CHANNEL, noramlly read it to red, green and blue
chans = cv2.split(image)
colors = ['b', 'g', 'r']
plt.figure()
plt.title('Flattened color histogram')
plt.xlabel('Bins')
plt.ylabel('# of bins')

for (chan, color) in zip(chans, color):
    hist = cv2.calcHist([chan, color], [0], None, [256], [0, 256])
    plt.plot(hist, color=color)
    plt.xlim([0, 256])


fig = plt.figure()


################################################################
# 2D histogram
ax = fig.add_subplot(131)
hist = cv2.calcHist([chans[1], chans[0]], [0, 1],
                    None, [32, 32], [0, 256, 0, 256])  # instead of 255 range we have used 32 since is popular
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Color Histogram for G and B")
plt.colorbar(p)
ax = fig.add_subplot(132)
hist = cv2.calcHist([chans[1], chans[2]], [0, 1],
                    None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Color Histogram for G and R")
plt.colorbar(p)

ax = fig.add_subplot(133)
hist = cv2.calcHist([chans[0], chans[2]], [0, 1],
                    None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Color Histogram for B and R")
plt.colorbar(p)

print("2D histogram shape: {}, with {} values".format(
    hist.shape, hist.flatten().shape[0]))


################################################################
# 3D histogram
hist = cv2.calcHist([image], [0,1,2],None, [8,8,8],[0,256,0,256,0,256])
print('3d hisogram shape.{}, with {} values',.format(hist.shape, hist.flatten().shape[0]))
plt.show()
