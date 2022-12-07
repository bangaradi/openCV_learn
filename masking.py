import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/cats.jpg')
img2 = cv.imread('Resources/Photos/lady.jpg')
img2 = cv.resize(img2, (img.shape[1], img.shape[0]), interpolation = cv.INTER_AREA)
cv.imshow('Cats', img)
cv.imshow('Lady', img2)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank Image', blank)

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
#Essentially this mask can be made into various weird shapes and thus can be used to mask various images... into various shapes

cv.imshow('Mask', mask)

masked_img = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked and Merged', masked_img)

cv.waitKey(0)