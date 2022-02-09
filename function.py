import cv2 as cv
import numpy as np

image = cv.imread("cat.jpg")
cv.imshow('color', image)

gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow('grey', gray)
# cv.waitKey(0)

blur = cv.GaussianBlur(image, (19,19), cv.BORDER_DEFAULT)
cv.imshow('blur',blur)
# cv.waitKey(0)

canny = cv.Canny(gray, 125, 175)
cv.imshow('canny',canny)
# cv.waitKey(0)

dilate = cv.dilate(canny, (3,3), iterations=1)
cv.imshow('dilate',dilate)
# cv.waitKey(0)

eroded = cv.erode(dilate, (3,3), iterations=1)
cv.imshow('erode',eroded)
# cv.waitKey(0)

resize = cv.resize(image,(500,500))
cv.imshow('resize',resize)
# cv.waitKey(0)

cropped = image[50:200 , 100:500]
cv.imshow('cropped', cropped)
cv.waitKey(0)





