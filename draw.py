import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype = 'uint8')
cv.imshow('blank', blank)
blank[:] = 0,0,255
cv.imshow('blank',blank)

cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness = 2)
cv.imshow('rectangle', blank)

cv.circle(blank,(250,250), 40, (0,255,0), thickness = cv.FILLED)
cv.imshow('circle',blank)

cv.line(blank, (0,0), (250,250), (255,0,0), thickness = 2)
cv.imshow('line',blank)

cv.putText(blank, "Hello, My name is Pradip", (0,255),cv.FONT_HERSHEY_TRIPLEX, 1.0, (100,100,100), 2)
cv.imshow('text',blank)

cv.waitKey(0)