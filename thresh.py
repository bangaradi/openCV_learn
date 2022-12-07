import cv2 as cv

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#Simple Thresholding
threshold, thresh = cv.threshold(gray, 225, 255, cv.THRESH_BINARY)
#params --> (image, threshold pixel value, maxVal, thresholding type)
    #maxVal refers to the value it will be set to when the pixel value is above the threshold
        #for thresholding types refer --> https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html

cv.imshow('Simple Thresholded', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
# sort of the negative image of cv.THRESH_BINARY

#Adaptive Thresholding
    #Simple Thresholding works with a global constant value, but that may not be right because of the lighting conditions in the image,
    #here, adaptive thershold comes to help as it sets the threshold for different blocks of the image.
adaptive_thresh_mean = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
#params --> (image, maxVal, way_of_determining_the_threshold_of_the_block, type_of_simple_thresholding, block_size, Constant to be subtracted from the mean)
 #to know more --> https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html

adaptive_thresh_gaussian = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 3)

cv.imshow('Mean Adaptive Thresholding', adaptive_thresh_mean)
cv.imshow('Gaussian Adaptive Thresholding', adaptive_thresh_gaussian)

cv.waitKey(0)