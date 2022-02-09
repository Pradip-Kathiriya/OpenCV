import cv2 as cv
import numpy as np

image = cv.imread('dog.jpg')

b,g,r = cv.split(image)

cv.imshow('blue', b)
cv.imshow('green', g)
cv.imshow('red', r)
# cv.waitKey(0)

merged = cv.merge([b,g,r])
cv.imshow('merged', merged)
# cv.waitKey(0)

blank = np.zeros(image.shape[:2], dtype='uint8')

##only blue channel
only_blue = cv.merge([b,blank,blank])
cv.imshow('only_blue',only_blue)
# cv.waitKey(0)

##only green channel
only_green = cv.merge([blank,g,blank])
cv.imshow('only_green',only_green)
# cv.waitKey(0)

##only red channel
only_red = cv.merge([blank,blank,r])
cv.imshow('only_red',only_red)
cv.waitKey(0)

