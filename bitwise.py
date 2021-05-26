import numpy as np
import cv2

rectangle = np.zeros((300,300), dtype = 'uint8')
cv2.rectangle(rectangle, (25,25),(275, 275), 255, -1)
cv2.imshow('rectangle', rectangle)

circle = np.zeros((300, 300), dtype = 'uint8')
cv2.circle(circle, (150, 150), 150, 255, -1)
cv2.imshow('circle', circle)

# with bitwise we can combine these two iamges

bitwiseAnd = cv2.bitwise_and(rectangle, circle) # a bitwise AND is true if and only if both pixels are greater than zero
cv2.imshow('AND', bitwiseAnd)
cv2.waitKey(0)

bitwiseOr = cv2.bitwise_or(rectangle, circle) # a bitwise OR is true if either of the two pixels are greater than zero
cv2.imshow('OR', bitwiseOr)
cv2.waitKey(0)

bitwiseXor = cv2.bitwise_xor(rectangle, circle) # a bitwise XOR is true if and only if either of the two pixels are greater than zero, but not both
cv2.imshow('XOR', bitwiseXor)
cv2.waitKey(0)

bitwiseNot = cv2.bitwise_not(circle)
cv2.imshow('NOT', bitwiseNot)
cv2.waitKey(0)

