import cv2 as cv

img = cv.imread('Resources/Photos/cat.jpg')
cv.imshow("cat", img)

#1. converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale Image', gray)

#2. Blurring our image
    #there are many types of blurring algorithms, here we are using the Gaussian Blur...
blur = cv.GaussianBlur(img, (9, 9), cv.BORDER_REPLICATE)
#parameters used --> (image_to_modify, kernel_size, Border_type)
cv.imshow('BLUR', blur)

#3. Edge Cascade
    #meaning to sort of highlight the edges, or make the edges appear distinctively
    #we use the Canny Edge Detection
canny = cv.Canny(img, 150, 175)
# the parameters are --> (image_to_modify, minVal, maxVal)
    #the minVal and maxVal can be understood from the link -> https://docs.opencv.org/4.x/da/d22/tutorial_py_canny.html
cv.imshow("Canny1", canny)

#4. Dilating the image
    #makes the image hazy-aesthetic ;)
dilated = cv.dilate(img, (5,5), iterations = 5)
# parameters --> (image to modify, kernel size, no of iterations) // usually dilation is done in iterations
cv.imshow("Dilated", dilated)

dilated_ec = cv.dilate(canny, (5,5), iterations = 5)
cv.imshow('Dilated Edge Cascading', dilated_ec)

#5. Eroding the image
    #reverse of dilating
eroded = cv.erode(dilated_ec, (5,5), iterations = 5)
# parameters --> (image to modify, kernel size, no of iterations) // erosion is also done iterations
# erosion is sort of the reverse of dilations, and in most of the cases, after exact same parameters, the original image is acquired from the dilated image
cv.imshow('Eroded Image', eroded)

#6. Resizing the image
resized = cv.resize(img, (100, 500), interpolation = cv.INTER_AREA)
# parameters are --> (image to modify, new-dimensions, interpolation type)
    #interpolation type can be decided based on enlargement or shrinking of the image
        # if we want to enlarge, we generally use INTER_AREA
        # if we want to shrink , we use INTER_LINEAR or INTER_CUBIC.. out of these INTER_CUBIC is the slowest, but the image is of higher quality than that of INTER_AREA or INTER_LINEAR
cv.imshow('Resized Image', resized)

#7. Cropping the images
cropped = img[250:450, 250:450]
cv.imshow('Cropped Image', cropped)

cv.waitKey(0)