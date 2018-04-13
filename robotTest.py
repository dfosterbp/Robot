from naoqi import ALProxy

import numpy as np
import cv2

img = cv2.imread('binder2.jpg')

boundaries = [
        #([0,0,0],[36,25,25]),
        ([35, 20, 20], [55, 40, 35])
        #([53,37,30], [255,255,255])
]

for (lower, upper) in boundaries:
    lower = np.array(lower, dtype = "uint8")
    upper = np.array(upper, dtype = "uint8")
mask = cv2.inRange(img, lower, upper)
output = cv2.bitwise_and(img, img, mask = mask)
gray_img = cv2.cvtColor(output, cv2.COLOR_RGB2GRAY)
_, threshold_img = cv2.threshold(gray_img, 60, 255, cv2.THRESH_OTSU)
_, threshold_img = cv2.threshold(threshold_img, 60, 255, cv2.THRESH_BINARY_INV)
threshold_img = cv2.cvtColor(threshold_img, cv2.COLOR_GRAY2RGB)


cv2.imshow("images", threshold_img)
cv2.waitKey(0)
