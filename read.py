import cv2
import numpy as np

img = cv2.imread('Resources/Photos/cat.jpg')

cv2.imshow('cat', img)

#cv2.waitKey(0)
#-------------------------------------------

#Reading Videos

#capture = cv2.VideoCapture(0) // here the argument '0' actually means to read from the webcam, can also be '1' that means read from the first camera and so on.. 

capture = cv2.VideoCapture('Resources/Videos/dog.mp4')

# the videos are always read frame-by-frame ...
while True: 
    isTrue, frame = capture.read()
    cv2.imshow('Video', frame)
    if cv2.waitKey(20) & 0xFF == ord('d'): #means if letter 'd' is pressed on the keyboard...
        break

capture.release()
cv2.destroyAllWindows()