import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

# blank = np.zeros(img.shape[:2], dtype = 'uint8')

# circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)

# #HISTOGRAMs
#     #can be computed for grayScale and RGB images

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("GrayScale", gray)

# mask = cv.bitwise_and(gray, gray, mask=circle)
# cv.imshow('Masked Image', mask)

# #GrayScale Histogram
# gray_hist = cv.calcHist([gray], [0], None, [256], [0, 256])
#params -> (list of images, all the channels as list, mask, histSize, ranges)

#calculating histogram with the mask
# gray_hist_mask = cv.calcHist([gray], [0], circle, [256], [0, 256])


# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('bins')
# plt.ylabel('no. of pixels')
# plt.plot(gray_hist, label='unmasked')
# plt.plot(gray_hist_mask, label = 'masked')
# plt.xlim([0, 256])
# plt.legend()
# plt.show()

plt.figure()
plt.title('Color Histogram')
plt.xlabel('bins')
plt.ylabel('no. of pixels')

colors = ('b', 'g', 'r')

for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color = col)
    plt.xlim([0, 256])


plt.show()


cv.waitKey(0)