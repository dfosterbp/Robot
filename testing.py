import numpy
import cv2
from naoqi import ALProxy
mo = ALProxy("ALRobotPosture","10.45.76.171",9559)
mo.goToPosture("Stand",1)
tts = ALProxy("ALTextToSpeech","10.45.76.171",9559)
tts.say("Testing Connection")
#Hey Ya'll
