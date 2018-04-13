<<<<<<< HEAD
import numpy as np
import cv2


# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()
 
# Change thresholds
params.minThreshold = 10;
params.maxThreshold = 200;
 
# Filter by Area.
params.filterByArea = True
params.minArea = 4000
 
# Filter by Circularity
params.filterByCircularity = True
params.minCircularity = 0.1
 
# Filter by Convexity
params.filterByConvexity = False
params.minConvexity = 0.87
 
# Filter by Inertia
params.filterByInertia = False
params.minInertiaRatio = 0.01

im = cv2.imread('binder2.jpg', cv2.IMREAD_GRAYSCALE)
detector = cv2.SimpleBlobDetector.create(params)

keypoints = detector.detect(im)
im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)
=======
from naoqi import ALProxy

motion = ALProxy("ALMotion", "10.45.76.171", 9559)
motion.moveTo(7,0,0)

pose = ALProxy("ALRobotPosture", "10.45.76.171", 9559)
pose.goToPosture("Stand",1)
>>>>>>> 6004fd64dcdd56f9a0b9f9edd9e6e1d2c0347054
