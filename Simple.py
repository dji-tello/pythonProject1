from djitellopy import tello
me = tello.Tello()
me.connect()
me.takeoff()
me.land()