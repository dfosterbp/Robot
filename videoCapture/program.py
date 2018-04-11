# vim: set fileencoding=utf-8 :
import sys
import numpy as np
import argparse
import cv2
from naoqi import ALProxy

if(len(sys.argv) <= 2):
    print "parameter error"
    print "python " + sys.argv[0] + " <ipaddr> <port>"

#ip_addr = sys.argv[1]
#port_num = int(sys.argv[2])

# get NAOqi module proxy
videoDevice = ALProxy('ALVideoDevice', "10.45.76.171", 9559) #Don't touch this, it's what sets up the camera

# subscribe top camera
AL_kTopCamera = 0       # This uses the top camera on the NAO, use 1 if you want to use the bottom camera

AL_kQVGA = 1            # 320x240: use this to change the resolution allowed for the camera window, look at aldebaran documentation on what values to change to

AL_kBGRColorSpace = 13  # This is like a filter, change value to numbers 1-13

captureDevice = videoDevice.subscribeCamera(
    "Gus07", AL_kTopCamera, AL_kQVGA, AL_kBGRColorSpace, 10) # This tells the computer what should be displayed to us

# create image
width = 320
height = 240
image = np.zeros((height, width, 3), np.uint8)

while True:

    # get image
    result = videoDevice.getImageRemote(captureDevice);

    # These are catch situations, if you get "cannot capture", reset the NAO
    if result == None:
        print 'cannot capture.'
    elif result[6] == None:
        print 'no image data string.'
    else:

        # translate value to mat
        values = map(ord, list(result[6]))
        i = 0
        for y in range(0, height):
            for x in range(0, width):
                image.itemset((y, x, 0), values[i + 0])
                image.itemset((y, x, 1), values[i + 1])
                image.itemset((y, x, 2), values[i + 2])
                i += 3

        # show image
        img = cv2.imread('binderHD.jpg')

        boundaries = [
            ([60, 20, 20], [100, 60, 60])
        ]

        for (lower, upper) in boundaries:
            lower = np.array(lower, dtype = "uint8")
            upper = np.array(upper, dtype = "uint8")
        #mask = cv2.inRange(img, lower, upper)
        #output = cv2.bitwise_and(img, img, mask = mask)

        cv2.imshow("images", np.hstack([image, image]))
        #cv2.waitKey(0)


    # exit by pressing [ESC]
    if cv2.waitKey(33) == 27:
        captureDevice = videoDevice.unsubscribe(videoDevice)
        break

