import cv2 as cv
import numpy as np

image = cv.imread('dog.jpg')
cv.imshow('image', image)
# cv.waitKey(0)

##BGR to gray
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)
# cv.waitKey(0)

##BGR to HSV(high saturation value)
hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)
# cv.waitKey(0)

##BGR to LAB
lab = cv.cvtColor(image, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)
cv.waitKey(0)
