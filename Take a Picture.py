import cv2
from djitellopy import Tello
from time import sleep
import numpy as np

tello = Tello()
tello.connect()
print(tello.get_battery())

# tello.streamon()

trying = 0
while (trying < 1):
    trying = trying + 1
    floor = "picture" + str(trying)
    floor = floor +  ".png"
    floor = '"' + floor + '"'
    print(floor)
    print("finished modification")
    sleep(5)

    tello.streamon()
    print(0)

    frame_read = tello.get_frame_read()
# the picture is called picture.png
    print(1)
    sleep(2)
# tello.takeoff()

    cv2.imwrite("picture.png", frame_read.frame)
#  writes picture in OpencvPython file
#  C:\Users\dasau\PycharmProjects\pythonProject1\OpencvPython
    print(2)
    sleep(2)

    cv2.imshow("picture.png", frame_read.frame)
    print(3)
    sleep(2)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         tello.land()

tello.takeoff()
tello.land()

# tello.land()

numpy.ndarray