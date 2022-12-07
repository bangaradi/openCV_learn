import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

#read more about each of them HERE -->: https://docs.opencv.org/4.x/d4/d13/tutorial_py_filtering.html

#1. Averaging
average = cv.blur(img, (5,5))
#parameters --> (image to modify, kernel_size)
cv.imshow('Averaging', average)

#2. Gaussian Blur
gauss = cv.GaussianBlur(img, (5,5), 0)
#params --> (image to modify, kernel_size, sigmaX)
    #sigmaX --> standard deviation along X-direction
cv.imshow('Gaussian Blur', gauss)

#3. Median Blur
median = cv.medianBlur(img, 5)
#params --> (image to modify, kernel_size -only one integer needed ..)
cv.imshow('Median', median)

#4. BilateralFiltering
bilateral = cv.bilateralFilter(img, 10, 100, 50)
#params --> (image to modify, diameter, sigmaColor, sigmaSpace)
cv.imshow('Bilateral', bilateral)


cv.waitKey(0)