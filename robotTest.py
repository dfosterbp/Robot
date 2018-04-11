from naoqi import ALProxy

import numpy as np
import cv2

img = cv2.imread('binderHD.jpg')

boundaries = [
	([60, 20, 20], [100, 60, 60])
]

#loop over the boundaries
for (lower, upper) in boundaries:
    #red for stopSign.jpg
    lower = np.array(lower, dtype = "uint8")
    upper = np.array(upper, dtype = "uint8")
# find the colors within the specified boundaries and apply
# the mask
mask = cv2.inRange(img, lower, upper)
output = cv2.bitwise_and(img, img, mask = mask)

# show the images
cv2.imshow("images", np.hstack([img, output]))
cv2.waitKey(0)
