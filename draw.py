import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

#1. Paint the image a certain color

blank[:] = 255, 0, 0
cv.imshow('Blue', blank)

#     #coloring a certain portion of the window
blank[100:200, 200:300] = 0, 255, 0
cv.imshow('Part Green', blank)

#2. Draw a rectangle
cv.rectangle(blank, (0, 0), (300, 200), (0, 255, 0), thickness = cv.FILLED)
# the parameters are --> (image_to_modify, (start coordinates-> x, y), (end coordinates-> x, y), color of the shape, thickess of the outline)

# we can also do this in the following way -->
cv.rectangle(blank, (0,0), (3*blank.shape[1]//4, blank.shape[0]//2), (0, 255, 0), thickness = -1) #makes a filled rectangle of green color

#3. Draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0, 200, 0), thickness = 2)
# the parameters are -> (image_to_modify, (center_of_the_circle -> x, y), radius_of_the_circle, color of the shape, thickness_of_the_outline_of_the_circle)

#4. Draw a line
cv.line(blank, (0,50), (100, 100), (0, 222, 0), thickness = 5)
# the parameters are --> (image_to_modify, (start coordinates-> x, y), (end coordinates-> x, y), color of the shape, thickess of the outline)

#5. Writing text on the Image
cv.putText(blank, 'Hello', (225, 225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), thickness = 2)
# the parameters are --> (image_to_modify, text_to_write, coordinates_to_start_text, font, scale_of_font, color_of_font, thickness_of_font)

cv.imshow('With Rectangle', blank)
cv.waitKey(0)