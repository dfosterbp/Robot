from naoqi import ALProxy

import numpy as np
import cv2

img = cv2.imread('binderHD.jpg')

boundaries = [
        #([0,0,0],[36,25,25]),
        ([35, 20, 20], [255, 40, 35])
        #([53,37,30], [255,255,255])
]

for (lower, upper) in boundaries:
    lower = np.array(lower, dtype = "uint8")
    upper = np.array(upper, dtype = "uint8")
mask = cv2.inRange(img, lower, upper)
output = cv2.bitwise_and(img, img, mask = mask)
gray_img = cv2.cvtColor(output, cv2.COLOR_RGB2GRAY)
_, threshold_img = cv2.threshold(gray_img, 60, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY_INV)
threshold_img = cv2.cvtColor(threshold_img, cv2.COLOR_GRAY2RGB)

params = cv2.SimpleBlobDetector_Params()

params.minThreshold = 0;
params.maxThreshold = 255;

params.filterByArea = True
params.minArea = 6000
params.maxArea = 100000

params.filterByCircularity = True
params.minCircularity = 0.1

params.filterByConvexity = False
params.filterByInertia = False


detector = cv2.SimpleBlobDetector.create(params)

keypoints = detector.detect(threshold_img)
im_with_keypoints = cv2.drawKeypoints(threshold_img, keypoints, np.array([]), (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow("Keypoints", im_with_keypoints)

cv2.waitKey(0)
