import cv2 as cv

image = cv.imread('dog.jpg')

gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)
cv.waitKey(0)

## simple thresholding
thresh,threshold = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('threshold', threshold)
cv.waitKey(0)

thresh_INV,threshold_INV = cv.threshold(gray, 125, 255, cv.THRESH_BINARY_INV)
cv.imshow('threshold_INV', threshold_INV)
cv.waitKey(0)

adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 9, 3)
cv.imshow('adaptive_thresh', adaptive_thresh)
cv.waitKey(0)