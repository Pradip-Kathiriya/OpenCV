import cv2 as cv

img = cv.imread("cat.jpg")
cv.imshow('cat', img)
cv.waitKey(0)

# Reading video

capture = cv.VideoCapture("ball_video1.mp4")
while True:
    isTrue, frame = capture.read()
    cv.imshow('video', frame) 
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()

# Resize the video

def rescaleFrame(frame, scale = 0.5):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dim = (width, height)
    return cv.resize(frame, dim, interpolation=cv.INTER_AREA)
capture = cv.VideoCapture("ball_video1.mp4")
while True:
    isTrue, frame = capture.read()
    resize_frame = rescaleFrame(frame,scale = 0.3)
    cv.imshow('video', frame)
    cv.imshow('resize video', resize_frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()

#Resize live video

def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,height)