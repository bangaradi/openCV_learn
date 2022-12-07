import cv2 as cv
import numpy as np

blank = np.zeros((400, 400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

cv.imshow("Rectangle", rectangle)
cv.imshow('Circle', circle)

#1. Bitwise AND
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('Image after bitwise AND', bitwise_and)

#2. Bitwise OR
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Image after bitwise OR', bitwise_or)

#3. Bitwise XOR
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Image after bitwise XOR', bitwise_xor)

#4. Bitwise NOT
bitwise_not_rectangle = cv.bitwise_not(rectangle)
bitwise_not_circle = cv.bitwise_not(circle)
cv.imshow('NOT of rectangle', bitwise_not_rectangle)
cv.imshow('NOT of circle', bitwise_not_circle)

cv.waitKey(0)