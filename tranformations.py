import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/park.jpg')

cv.imshow('Park', img)


#1. Translating the image
def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])

    return cv.warpAffine(img, transMat, dimensions)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

translated = translate(img, -100, 100)

cv.imshow('Translated', translated)

#2. Rotation on an image
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 0.5)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 30)

cv.imshow("Rotated Image", rotated)

#3. Resizing the image
resized = cv.resize(img, (10000, 10000), interpolation=cv.INTER_CUBIC)

cv.imshow("Resized Image", resized)

#4. Flipping an image
flip = cv.flip(img, -1)
#0 --> flip image vertically
#1 --> flip image horizontally
#-1--> flip image both horizontally and vertically

cv.imshow('Flipped', flip)

#5. Cropping the image
cropped = img[200:300, 300:400]

cv.imshow("Cropped", cropped)

cv.waitKey(0)