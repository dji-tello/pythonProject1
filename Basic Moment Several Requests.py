# BASIC MOMENTS WITH SEVERAL REQUESTS

from djitellopy import tello
from time import sleep

me = tello.Tello()
me.connect()

print(me.get_battery())
print(me.get_flight_time())
print(me.get_height())
print(me.get_barometer())
print(me.get_attitude())
print(me.get_udp_video_address())
print(me.get_distance_tof())
print(me.get_distance_tof())
print(me.get_frame_read())
print(me.get_speed())
print(me.get_temperature())
print(me.get_video_capture())
print(me.get_wifi())

me.takeoff()
me.send_rc_control(0, 0, 0, 0)
sleep(2)
me.send_rc_control(0, 0, 0, 0)
sleep(2)
sleep(2)
me.send_rc_control(0, 0, 0, 0)
sleep(2)
sleep(2)
me.land()
