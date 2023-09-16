# BASIC MOMENTS WITH SEVERAL REQUESTS

from djitellopy import tello
from time import sleep
import os

me = tello.Tello()
me.connect()

print("START OF ME.GET_ COMMANDS.")
print("The own udp object")
print(me.get_own_udp_object())
#print(me.udp_response_receiver()) #you would not call this function
#print(me.udp_state_receiver())  #you would not call this function
#print(me.parse_state())    #you would not call this function
print("The current state")
print(me.get_current_state())
print("pitch,roll,yaw,speed x, speed y, speed z")
print(me.get_pitch())
print(me.get_roll())
print(me.get_yaw())
print(me.get_speed_x())
print(me.get_speed_y())
print(me.get_speed_z())
print("acceleration x,y,z, the lowest and highest and actual temperature.")
print(me.get_acceleration_x())
print(me.get_acceleration_y())
print(me.get_acceleration_z())
print(me.get_lowest_temperature())
print(me.get_highest_temperature())
print(me.get_temperature())
print("height,distance,barometer,flight time,battery")
print(me.get_height())
print(me.get_distance_tof())
print(me.get_barometer())
print(me.get_flight_time())
print(me.get_battery())
print("udp video address and video capture")
print(me.get_udp_video_address())
print(" ")
print(" ")
#print(me.get_video_capture())

#print(me.get_frame_read())  #for the camera
#print(me.get_state_field())
#print(me.get_mission_pad_id())  #only for Tello Edu.
#print(me.get_mission_pad_distance_x())
#print(me.get_mission_pad_distance_y())
#print(me.get_mission_pad_distance_z())
#print(me.get_wifi())

print("START OF ME.QUERY_ COMMANDS.")
print("DO NOT USE QUERY WHEN GET_ WORKS")
#print("speed,battery,flight time,height, temperature")
#print(me.query_speed())
#print(me.query_battery())
#print(me.query_flight_time())
#print(me.query_height())
#print(me.query_temperature())
#print("attitude, barometer, distance,wifi,sdk, serial number")
#print(me.query_attitude())
#print(me.query_barometer())
#print(me.query_distance_tof())
#print(me.query_wifi_signal_noise_ratio())
#print(me.query_sdk_version())
#print(me.query_serial_number())


#me.takeoff()
sleep(3)
#me.land()
me.end()
print("The Tello drone presented several values and the drone can fly up and down.")
exit()

