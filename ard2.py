import serial
import time
ard = serial.Serial("/dev/cu.usbserial-110", 9600)
time.sleep(2)
while True:
   user = input("input: ")
   if user == "on":
      ard.write(b'1')
   elif user == "off":
      ard.write(b'0')
   elif user == 'end':
      break
      ard.write(b'0')
   else:
      print("not work!")