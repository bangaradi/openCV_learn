import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('Park', img)

b, g, r = cv.split(img)

cv.imshow('Blue', b)
cv.imshow('Red', r)
cv.imshow('Green', g)
#These images are shown as grayscale images, that have intensities of the color as the whiteness in the grayscale image...

#Remerging these splits -->
merged = cv.merge([b,g,r])
cv.imshow('MErged image', merged)

#now we will see a way of actually seeing the splitted colors in their respective color and not in the grayscale format
    #this is done by merging them with the splits of the blank image...
blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

b_blank, g_blank, r_blank = cv.split(blank)

# seeing the red part of the image
    #we are gonna put the blank parts in the other 2 and color part in the given one.
red = cv.merge([b_blank, g_blank, r])
#blue part
blue = cv.merge([b, g_blank, r_blank])
#green part
green = cv.merge([b_blank, g, r_blank])

cv.imshow('Red Image', red)
cv.imshow('Blue Image', blue)
cv.imshow('Green Image', green)

cv.waitKey(0)
