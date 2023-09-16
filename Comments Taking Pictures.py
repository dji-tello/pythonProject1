# Program "Take a picture" written by Austin Sauls
# Using Python 3.7, Pycharm, Opencv, and djitellopy.

import sys
import os
import cv2
from djitellopy import Tello

#f = open("D:\\Austin.txt", "r")
#print(f.read())
#f = open("D:\\Austin.txt", "r")
#print(f.readline())

#f = open("D:\\Austin.txt", "a")
#f.write("Now the file has more content!")
#f.close()
#f = open("D:\\Sauls.txt", "x")  #the x is to create a file.





print("++++++++++++++version++++++++++++++++++++++")
print(sys.version)
print("++++++++++++++++++path++++++++++++++++++")
print(sys.path)
print("+++++++++++++getwubdiwsversion+++++++++++++++++++++++")
print(sys.getwindowsversion())
print("+++++++++++++modules+++++++++++++++++++++++")
print(sys.modules)
print("+++++++++++++end+++++++++++++++++++++++")


print("Program will set the key to zero.")
key = 0   # Test the key for escape key
print("The picture to show will be called picture.png.")
picture = "picture.png"   # sample selection for picture
print("CV2 will destroy all Windows.")
cv2.destroyAllWindows()
print("The new name for drone is tello.")
tello = Tello()
print("tello will try to perform a connection.")
tello.connect()
print("tello will get the percentage of the battery supply.")
print("The percentage of the battery supply that is available is: " , tello.get_battery())
print("Get the stream on")
tello.streamon()
print("the looping to get multiple pictures.")
#for the looping to get multiple pictures.
for i in range(0,10):
        print("The value of i for the range is:", i)

print("The beginning of the WHILE loop.")
# The beginning of the WHILE loop.
i = 0
while i < 10:

        print("THIS IS THE BEGINNING OF THE COLLECTION OF PICTURES")
        print("CV2 will set a key to wait for 5 seconds and then run again.")
        cv2.waitKey(3000)  # wait for 3 seconds
        print("The 5 seconds wait has finished.")
        print("Tello drome can take picture and put picture image into img.")
        img = tello.get_frame_read().frame
        print("Save the full sized picture in the D:\Pictures folder")

        #isWritten = cv2.imwrite('D:\\Pictures\\image-3.png', img)
        nowfile = "D:\\Pictures\\pictures%s.png" % i
        print(nowfile)
        isWritten = cv2.imwrite(nowfile, img)


        print("The full sized picture was saved.")
        print("The img need to be reduced to smaller size in bytes.")
        img = cv2.resize(img, (360, 240))
        print("CV2 will write the picture.png into the img.")
        cv2.imwrite(picture, img)
        print("CV2 will show the picture img on the console screen.")
        cv2.imshow(picture, img)
        print("CV2 will set a key to wait for 3 seconds so that we can observe the photo.")
        cv2.waitKey(3000)  #wait for 3 seconds
        print("The 3 seconds of photo viewing has completed.")

#f = open("D:\\Austin.txt", "a")
#f.write(picture.png)
#f.close()

        i += 1
print("Start of the DO WHILE loop.")
i = 0
while True:
        print(i)
        i += 1
        if i == 10:
                break
print("End of the DO WHILE loop.")
i=0
while True:
# end of the DO WHILE loop.

        print("The key was initialized to zero, it has the present value of: ", key)
        print("Wait until someone enters a key press.")
        key = cv2.waitKey(20000)  #wait for 20 seconds for someone to do a key press.
        print("Someone has pressed the CV2.waitKey input.")
        print("A person has set the key to be: ", key)
        print("Test the key for ESC (27) or q (113) to destroy pictures.")
        if key == 27 or key == 113:
               print("The key that was pressed was a ESC or q key.")
        if key == 27:
               print("The Escape key was pressed.")
               print("Since the key is ESC, destroy window, end program, do a system exit.")
               print("CV2 will destroy All Windows")
               cv2.destroyAllWindows()
               print("End the program from running.")
               tello.end()
               print("Exit the system.")
               sys.exit("The escape key was pressed.")

        if key == 113:
              print("The q key was pressed.")
              print("Since the key is q, destroy window, end program, do a system exit.")
              print("CV2 will destroy All Windows")
              cv2.destroyAllWindows()
              print("End the program from running.")
              tello.end()
              print("Exit the system.")
              sys.exit("The q key was pressed.")

        elif key != 27 or key != 113:
              print("The key that was pressed was NOT an ESC or q key.")
              print("Then we can fly the tello drone to take off and land.")
                #     tello.takeoff()
                 #   tello.land()
              print("The tello drone has landed so we will destroy window, end program, do a system exit.")
              print("CV2 will destroy All Windows")
              cv2.destroyAllWindows()
              print("CV2 will set a key to wait for 5 seconds and then run again.")
              key = cv2.waitKey(5000)  # wait for 5 seconds
              print("The 10 seconds of photo viewing has completed.")
              print("Wait until someone enters a key press.")
              print("End the program from running with tello.end().")
              tello.end()
              print("The tello.end has completed.")
              print("Exit the system with sys.exit(The NO key was pressed).")
              sys.exit("The NO key was pressed.")

