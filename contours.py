import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Cat', img)

blank = np.zeros(img.shape, dtype = 'uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny', canny)

#thresholding can be used as an alternative in place of canny when finding out contours, because canny can sometimes give too many details, which are not needed
#to get over the details we therefore sometiems blur the image before putting it in the canny function to lower the amount of details
#SO, finally we only have the choice of choosing between 'Canny with Blur' and 'Thresholding'
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
#parameters used are --> (grayscale_image, lower_bound_pixel_intensity, upper_bound_pixel_intensity, thresholding_type)
    # the pixel is set zero is it below or above the lower/upper bound otherwise 1.

cv.imshow('Thresh', thresh)

# calling the contour function
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# parameters used are --> (image_to_find contours_on, contour_retrievel_mode, contour_approximation_mode)

cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow('Blank with Contours', blank)

print(f'{len(contours)} contours found!')



cv.waitKey(0)