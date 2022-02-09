import cv2 as cv
import numpy as np

image = cv.imread('dog.jpg')

gray=cv.cvtColor(image, cv.COLOR_BGR2GRAY)

## Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('laplcian', lap)
# cv.waitKey(0)

##sobel
sobelx = cv.Sobel(gray,cv.CV_64F,1,0)
sobely = cv.Sobel(gray,cv.CV_64F, 0, 1)
combined_sob = cv.bitwise_or(sobelx, sobely)
cv.imshow('combined_sob', combined_sob)
# cv.waitKey(0)

##canny
canny = cv.Canny(gray,125, 175)
cv.imshow('canny', canny)
cv.waitKey(0)
