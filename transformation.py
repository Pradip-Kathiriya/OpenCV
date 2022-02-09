import cv2 as cv
import numpy as np

def translate (image, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (image.shape[1], image.shape[0])
    return cv.warpAffine(image, transMat, dimensions)

def rotation(image, angle, rotpoint = None):
    dimensions = (image.shape[1], image.shape[0])
    if rotpoint == None:
        rotpoint = (image.shape[1]//2, image.shape[0]//2)
    rotMat = cv.getRotationMatrix2D(rotpoint,angle, 1.0)
    return cv.warpAffine(image,rotMat,dimensions)

image = cv.imread('cat.jpg')
cv.imshow('image', image)

translate = translate(image, 20, 20)
cv.imshow('translate', translate)
cv.waitKey(0)

rotation = rotation(image, 45)
cv.imshow('rotation', rotation)
cv.waitKey(0)

resized = cv.resize(image, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('resized', resized)
cv.waitKey(0)

flip = cv.flip(image,-1)
cv.imshow('flip', flip)
cv.waitKey(0)



