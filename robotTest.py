#from naoqi import ALProxy

import numpy as np
import argparse
import cv2

#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", help = "path to the image")
#args = vars(ap.parse_args())

img = cv2.imread('stopSign.jpg')

boundaries = [
	([17, 15, 100], [50, 56, 200]),
	([86, 31, 4], [220, 88, 50]),
	([25, 146, 190], [62, 174, 250]),
	([103, 86, 65], [145, 133, 128])
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
