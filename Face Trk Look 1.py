import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, img = cap.read()
    cv2.imshow("Output", img)
    cv2.waitKey(1)

#   Takes picture and displays it
#   Need TaskManager to stop it