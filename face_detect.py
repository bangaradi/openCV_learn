import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/group 2.jpg')
cv.imshow('Lady', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#storing our pre-trained classifier in our variable.
haar_cascade = cv.CascadeClassifier('haar_faces.xml')

#gives the coordinates of the rectangles in which we have found the faces.
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6)
#params --> (image, scaleFactor, no of neighbors a rectangle need to have to be called a face.)

print(f'Number of faces found = {len(faces_rect)}')

for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness = 1)

cv.imshow('Detected Faces', img)

cv.waitKey(0)