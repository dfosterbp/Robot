from naoqi import ALProxy

import numpy as np
import cv2

img = cv2.imread('binderHD.jpg')

boundaries = [
	([60, 20, 20], [100, 60, 60])
]

for (lower, upper) in boundaries:
    lower = np.array(lower, dtype = "uint8")
    upper = np.array(upper, dtype = "uint8")
mask = cv2.inRange(img, lower, upper)
output = cv2.bitwise_and(img, img, mask = mask)

cv2.imshow("images", np.hstack([img, output]))
cv2.waitKey(0)
#hey from gus’s phone