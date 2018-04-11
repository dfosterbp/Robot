#from naoqi import ALProxy

import numpy as np
import argparse
import cv2

#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", help = "path to the image")
#args = vars(ap.parse_args())

ip_addr = "172.17.21.168"

robotVoice = ALProxy("ALTextToSpeech", ip_addr, 9559)
#robotVoice.say("Hello, World!")
robotPose = ALProxy("ALRobotPosture", ip_addr, 9559)
#robotPose.goToPosture("Stand", 1)
robotNav = ALProxy("ALNavigation", ip_addr, 9559)
robotVideoDevice = ALProxy("ALVideoDevice", ip_addr, 9559)
robotSonar = ALProxy("ALSonar", ip_addr, 9559)
robotSonar.subscribe("NAO_Program")

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
<<<<<<< HEAD

#cv2.imshow('image',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#tts = ALProxy("ALTextToSpeech", ip_addr, 9559)
#pose = ALProxy("ALRobotPosture", ip_addr, 9559)
#motion = ALProxy("ALMotion", ip_addr, 9559)
#pose.goToPosture("Stand",1)
#motion.moveTo(0.5, 0, 0)
=======
>>>>>>> 39dc8d0a7720a6c5148545295385913d7b04980b
