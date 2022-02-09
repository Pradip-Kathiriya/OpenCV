import cv2 as cv
import numpy as np

image = cv.imread('group.webp')
cv.imshow('image', image)
# cv.waitKey(0)

gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
cv.imshow('gray', gray)
# cv.waitKey(0)

haar_cascade = cv.CascadeClassifier('haar_face.xml')
face_rect = haar_cascade.detectMultiScale(image, scaleFactor = 1.1, minNeighbors = 2)

for(x,y,w,h) in face_rect:
    cv.rectangle (image, (x,y), (x+w,y+h), (0,0,255), thickness=2)
    
cv.imshow('face with rectangle', image)
# cv.waitKey(0)


capture = cv.VideoCapture("video_for_face.mp4")
while True:
    isTrue, frame = capture.read()
    face_rect = haar_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors = 1)
    for (x,y,w,h) in face_rect:
        cv.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), thickness=2)
    cv.imshow('video for face detection', frame)
    if cv.waitKey(0) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()
