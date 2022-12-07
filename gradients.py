import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


#Laplacian , a way to detect edges on the image
lap = cv.Laplacian(gray, cv.CV_64F)
#params --> (image, data depth)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)


#Sobel - gradient magnitude representation
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
#params --> (image, data depth, x_direction, y_direction)

cv.imshow('Sobel x', sobelx)
cv.imshow('Sobel y', sobely)

combined_sobel = cv.bitwise_or(sobelx, sobely)
cv.imshow('Combined Sobel', combined_sobel)

#Canny
canny = cv.Canny(gray, 150, 175)
#canny is an advanced kind of edge detection algo that uses sobel and laplacian at it's various stages.
cv.imshow('Canny', canny)



cv.waitKey(0)