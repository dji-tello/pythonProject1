# Program "Take a picture" written by Austin Sauls
# Using Python 3.9, Pycharm, Opencv, and djitellopy.

import sys
import cv2
from djitellopy import Tello

import time

start = time.time()
print("hello")





print("Program will set the key to zero.")
key = 0   # Test the key for escape key
print("The picture to show will be called picture.png.")
picture = "picture.png"   # sample selection for picture
print("CV2 will destroy all Windows.")
cv2.destroyAllWindows()
print("The new name for drone is tello.")
tello = Tello()
print("The tello will try to perform a connection.")
tello.connect()
print("Available battery is: " , tello.get_battery())
print("Get the stream on")
tello.streamon()
print("The looping to get multiple pictures.")
for i in range(0,10):
        print("The value of i for looping in the range is:", i)
print("The beginning of the WHILE loop.")
i = 0
while i < 10:
        print("THE COLLECTION OF PICTURES")
        print("Tello can take picture and put them on disk.")
        img = tello.get_frame_read().frame
        nowfile = "D:\\Pictures\\BBB%s.png" % i
        print(nowfile)
        isWritten = cv2.imwrite(nowfile, img)
        img = cv2.resize(img, (360, 240))
        cv2.imwrite(picture, img)
        cv2.imshow(picture, img)
        cv2.waitKey(5000)
        i += 1
print("Start of the DO WHILE loop.")
i = 0
while True:
        print("Testing the value of i for breaking:" , i)
        i += 1
        if i == 10:
                break
print("End of the DO WHILE loop.")

end = time.time()
print(end - start)


print("Reset the value of the i back to zero.")
i=0
while True:
        print("Wait until someone enters a key press.")
        key = cv2.waitKey(20000)  #wait for 20 seconds
        print("A person has set the key to be: ", key)
        if key == 27 or key == 113:
            if key == 27:
               cv2.destroyAllWindows()
               tello.end()
               sys.exit("The escape key was pressed.")
            if key == 113:
              cv2.destroyAllWindows()
              tello.end()
              sys.exit("The q key was pressed.")

        elif key != 27 or key != 113:
                #     tello.takeoff()
                 #   tello.land()
              cv2.destroyAllWindows()
              tello.end()
              sys.exit("The NO key was pressed.")

