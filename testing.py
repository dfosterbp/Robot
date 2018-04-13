from naoqi import ALProxy

motion = ALProxy("ALMotion", "10.45.76.171", 9559)
motion.moveTo(7,0,0)

pose = ALProxy("ALRobotPosture", "10.45.76.171", 9559)
pose.goToPosture("Stand",1)
