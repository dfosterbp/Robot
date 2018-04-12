from naoqi import ALProxy

import numpy as np
import cv2

img = cv2.imread('binderHD.jpg')

boundaries = [
        #([0,0,0],[60,20,20]),
	([60, 20, 20], [100, 60, 60])
        #([100,60,60], [255,255,255])
]

for (lower, upper) in boundaries:
    lower = np.array(lower, dtype = "uint8")
    upper = np.array(upper, dtype = "uint8")
mask = cv2.inRange(img, lower, upper)
output = cv2.bitwise_and(img, img, mask = mask)
gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
_, threshold_img = cv2.threshold(gray_img, 60, 255, cv2.THRESH_BINARY)
threshold_img = cv2.cvtColor(threshold_img, cv2.COLOR_GRAY2RGB)

cv2.imshow("images", threshold_img)
cv2.waitKey(0)
