#
# Tello Python3 Control Demo
#
# http://www.ryzerobotics.com/
#
# 1/1/2018

# ----------imports-------------------------------
# import python modules that will serve
# various purposes for the rest of code
import threading
import socket
import sys
import time
# -----------------------------------------------

# -------address and bind------------------------
# create a UDP port for PC
host = '0.0.0.0'
port = 9000
locaddr = (host,port)


# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tello_address = ('192.168.10.1', 8889)

# define end points of the operation
sock.bind(locaddr)
# -----------------------------------------------

# ---------The function "receive"----------------

def recv():
    count = 0
    while True:
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print ('\nExit . . .\n')
            break
# -----------------------------------------------

# ----------Input Commands to Tello--------------

print ('\r\n\r\nTello Python3 Demo.\r\n')
print ('Tello: command takeoff land flip forward back left right \r\n       up down cw ccw speed speed?\r\n')
print ('end -- quit demo.\r\n')

#recvThread create
recvThread = threading.Thread(target=recv)
recvThread.start()

while True:

    try:
        msg = input("");

        if not msg:
            break

        if 'end' in msg:
            print ('...')
            sock.close()
            break

        # Send data to tello
        msg = msg.encode(encoding="utf-8")
        sent = sock.sendto(msg, tello_address)
    except KeyboardInterrupt:
        print ('\n . . .\n')
        sock.close()
        break




