import cv2
import numpy as np

def getImagepath():
    #implement soon
    return 0

def biggestContour(contours):
    bigCont = np.array([])
    max_area = 0

    for i in contours:
        area = cv2.contourArea(i)
        if area>50 and area>max_area:
            approx = cv2.approxPolyDP(i, 0.02*cv2.arcLength(i, True), True)
            if len(approx)==4:
                bigCont=approx
                max_area = area

    return bigCont, max_area


            
