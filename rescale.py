#udpout:127.0.0.1:14540
from pymavlink import mavutil

#udpcast()
address = 'udpin:localhost:14550' #simulasyon
# address= '/dev/ttyACM0' #pixhawk usb
# address= '/dev/ttyTHS1' #pixhawk telem2 baudrate= 115200
vehicle= mavutil.mavlink_connection(address,baudrate=57600,autoreconnect= True)
vehicle.wait_heartbeat()
print("baglanti basarili")

# while True:
#     message= vehicle.recv_match(blocking= True)
#     print(message)