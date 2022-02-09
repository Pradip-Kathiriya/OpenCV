import cv2 as cv
import numpy as np

image = cv.imread('dog.jpg')
cv.imshow('image', image)
# cv.waitKey(0)

#average blur
blur = cv.blur(image, (3,3))
cv.imshow('blur', blur)
# cv.waitKey(0)

#gaussian blur
gaussian = cv.GaussianBlur(image, (7,7),0)
cv.imshow('gaussian', gaussian)
# cv.waitKey(0)

#median blur
median = cv.medianBlur(image,5)
cv.imshow('median', median)
# cv.waitKey(0)

#bilateral blur
bilateral = cv.bilateralFilter(image, 5, 15, 15)
cv.imshow('bilateral', bilateral)
cv.waitKey(0)