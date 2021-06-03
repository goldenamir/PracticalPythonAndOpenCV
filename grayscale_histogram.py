# importing required libraries

from matplotlib import pyplot as plt    
import argparse
import cv2 

ap = argparse.ArgumentParser()
ap.add_argument('-i','--image', required=True, help = 'path to the image file')
args = vars(ap.parse_args())

image = cv2.imread(args.image)

image = cv2.cvtColor, cv2.COLOR_BGR2GRAY)
cv2.imshow('Original', image)

hist = cv2.calcHist([image], [0], None, [256], [0, 256]) # given [0] since grayscale has one channel only, there is no mask so NONE is in, [256] is number of bins
                                                        # [0, 256] is a range of value
plt.figure()
plt.title('Grayscale histogram')
plt.xlabel('Bins')
plt.ylabel('# of Pixels')
plt.plot(hist)
plt.xlim([0, 256])
plt.show()
cv2.waitKey(0)
