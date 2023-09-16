import cv2
import numpy as np

img = cv2.imread('test.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# gray = cv2.cvtColor(img, cv2.6)
