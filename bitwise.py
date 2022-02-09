import cv2 as cv
import numpy as np

blank = np.zeros([500,500], dtype = 'uint8')
cv.imshow('blank', blank)
# cv.waitKey(0)

circle = cv.circle(blank.copy(), (250,250), 250, 255, thickness = -1)
cv.imshow('circle', circle)
# cv.waitKey(0)

rectangle = cv.rectangle(blank.copy(), (10,10), (490,490), 255, thickness = -1)
cv.imshow('rectangle', rectangle)
# cv.waitKey(0)

## Bitwise_and
bitwise_and  = cv.bitwise_and(circle, rectangle)
cv.imshow('bitwise_and', bitwise_and)
# cv.waitKey(0)

##bitwise_or
bitwise_or = cv.bitwise_or(circle, rectangle)
cv.imshow('bitwise_or', bitwise_or)
# cv.waitKey(0)

##bitwise_xor
bitwise_xor = cv.bitwise_xor(circle, rectangle)
cv.imshow('bitwise_xor', bitwise_xor)
# cv.waitKey(0)

##bitwise_not
bitwise_not = cv.bitwise_not(circle)
cv.imshow('bitwise_not', bitwise_not)
cv.waitKey(0) 
