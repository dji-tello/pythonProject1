# Program "Take a picture" written by Austin Sauls
# Using Python 3.7, Pycharm, Opencv, and djitellopy.

import cv2
from djitellopy import Tello
from time import sleep
import sys

key = 0   # Test the key for escape key
picture = "picture.png"   # sample selection for picture

print(10)
cv2.destroyAllWindows()
print(11)
tello = Tello()
print(12)
tello.connect()
print(13)
print(tello.get_battery())
print(14)
tello.streamon()
print(15)
# Tello drome can take picture and
# put picture image into img.
img = tello.get_frame_read().frame
print(16)
#  img need to be reduced to bytes
img = cv2.resize(img, (360, 240))
#
print(17)
#  writes picture in OpencvPython file
#  and gives it a name of picture.png
cv2.imwrite(picture, img)
#  rests so that write has time to work
print(18)
#  shows the picture on screen
cv2.imshow(picture, img)
print(19)
#  pause so imshow has time to work

#  pauses for 5 seconds and wait for key press
key = cv2.waitKey(5000)  #wait for 5 seconds
print(20)
#  test the key for ESC or q to destroy pictures
if key == 27 or key == 113:
#  if key is ESC or q, destroy window and exit
        print(21)
        cv2.destroyAllWindows()
        tello.end()
        print(22)
if key == 27:
        sys.exit("The escape key was pressed.")
        print(23)
if key == 113:
        sys.exit("The q key was pressed.")
        print(24)
elif key != 27 or key != 113:
        print(25)
        cv2.destroyAllWindows()
        print(26)
  #      tello.takeoff()
        print(27)
  #      tello.land()
        print(28)
        tello.end()
        print(29)
        sys.exit("The drone toke off and landed.")
        print(30)