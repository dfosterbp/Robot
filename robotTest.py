#from naoqi import ALProxy

#import numpy as np
#import cv2

#img = cv2.imread('binder2.jpg')

#boundaries = [
        #([0,0,0],[36,25,25]),
#        ([35, 20, 20], [55, 40, 35])
        #([53,37,30], [255,255,255])
#]

#for (lower, upper) in boundaries:
#    lower = np.array(lower, dtype = "uint8")
#    upper = np.array(upper, dtype = "uint8")
#mask = cv2.inRange(img, lower, upper)
#output = cv2.bitwise_and(img, img, mask = mask)
#gray_img = cv2.cvtColor(output, cv2.COLOR_RGB2GRAY)
#_, threshold_img = cv2.threshold(gray_img, 60, 255, cv2.THRESH_OTSU)
#_, threshold_img = cv2.threshold(threshold_img, 60, 255, cv2.THRESH_BINARY_INV)
#threshold_img = cv2.cvtColor(threshold_img, cv2.COLOR_GRAY2RGB)


#cv2.imshow("images", threshold_img)
#cv2.waitKey(0)
import numpy as np
import cv2

rawImage = cv2.imread('binder2.jpg')
hsv = cv2.cvtColor(rawImage, cv2.COLOR_BGR2HSV)

hue, saturation, value = cv2.split(hsv)

retval, threshold, = cv2.threshold(saturation, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

medianFiltered = cv2.medianBlur(threshold, 5)

_, contours, hierarchy = cv2.findContours(medianFiltered, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

contour_list = []
for contour in contours:
    area = cv2.contourArea(contour)
    if area > 10000 and area < 20000  :
        contour_list.append(contour)
cv2.drawContours(rawImage, contour_list, -1, (255, 0, 0), 2)


cv2.imshow('IMAGE', rawImage)
cv2.waitKey(0)
