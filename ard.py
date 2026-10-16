import time
import os
import re
import sounddevice as sd
import soundfile as sf
import speech_recognition as sr
import serial

ard = serial.Serial('/dev/cu.usbserial-110', 9600)
time.sleep(2)

f = 44100
duration = 2

print("speak---")

while True:
    try:
        rd = sd.rec(int(f * duration), samplerate=f, channels=1)
        sd.wait()
        sf.write('t.wav', rd, f)
        
        r = sr.Recognizer()
        with sr.AudioFile('t.wav') as s:
            a = r.record(s)
            tx = r.recognize_google(a, language='en-UK')
            if tx in "on":
               print("!!!!")
               ard.write(b'1')
            elif tx == "not":
               break
               ard.write(b'0')
            elif tx == "off":
               ard.write(b'0')
            else:
                ard.write(b'0')
    except:
        pass
