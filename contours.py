import cv2 as cv
import numpy as np

image = cv.imread('cat.jpg')
cv.imshow('image', image)
# cv.waitKey(0)

gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
cv.imshow('gray', gray)
# cv.waitKey(0)

canny = cv.Canny(gray, 125, 175)
cv.imshow('canny', canny)
# cv.waitKey(0)

ret, threshold = cv.threshold (gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('threshold', threshold)
# cv.waitKey(0)

im2, contours, heirarchies = cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
print(f"{len(contours)} counter(s) found")
# cv.waitKey(0)

blank = np.zeros((1200,1200,3), dtype='uint8')
cv.imshow('blank',blank)
# cv.waitKey(0)

draw = cv.drawContours(blank, contours, -1, (0,0,255),2)
cv.imshow('draw',draw)
cv.waitKey(0)

