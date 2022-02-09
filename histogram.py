import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image = cv.imread('dog.jpg')
cv.imshow('image', image)
# cv.waitKey(0)

blank = np.zeros(image.shape[:2], dtype='uint8')

mask = cv.circle(blank, (image.shape[1]//2,image.shape[0]//2), 100, 255, -1)

gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)
# cv.waitKey(0)

masked = cv.bitwise_and(gray,gray,mask=mask)
cv.imshow('mask',mask)
cv.waitKey(0)

#Grayscale histogram
gray_hist = cv.calcHist([gray], [0], masked, [256], [0,256],)
plt.figure()
plt.title('grayscale histogram with mask')
plt.xlabel('bins')
plt.ylabel('No of Pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

# color histogram
plt.figure()
plt.title('colour histogram with mask')
plt.xlabel('bins')
plt.ylabel('No of Pixels')
color = ('r','g','b')
for i, col in enumerate(color):
    hist = cv.calcHist([image], [i], masked, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])
plt.show()


