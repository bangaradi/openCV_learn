import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Resources/Photos/park.jpg')

#1. BGR to GrayScale 
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#2. BGR to HSV (hue, saturation, value/brightness)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

#3. BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

#4. BGR to RGB 
#since most of our formats out there are in RGB format, we need to convert our openCV images to RGB, just like we show how plotting in matplotlib changes
#the visible format of the image is of the inverted form
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

#5. HSV to BGR
bgr_from_hsv = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('BGR from HSV', bgr_from_hsv)

#5. GrayScale to HSV
    #this is not possible to carry out, we need to first convert GrayScale to BGR then BGR to HSV
bgr_from_gray = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
hsv_from_bgr = cv.cvtColor(bgr_from_gray, cv.COLOR_BGR2HSV)
cv.imshow('HSV from GRAY', hsv_from_bgr)

#6. GrayScale to BGR
cv.imshow('BGR from GrayScale', bgr_from_gray)


plt.imshow(rgb)
plt.show()

cv.waitKey(0)