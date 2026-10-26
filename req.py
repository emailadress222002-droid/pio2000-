import requests
import serial
ard = serial.Serial("/dev/cu.usbserial-10", 9600)
url = "https://ntfy.sh/mohammad_led_control_2026/json"

print("loading")

try:
    response = requests.get(url, stream=True)
    for line in response.iter_lines():
        if line:
            import json
            data = json.loads(line.decode('utf-8'))
            message = data.get("message", "").strip().lower()
            
            if message == "on":
                ard.write(b'1')
            elif message == "off":
                ard.write(b'0')
except Exception as e:
    print("error", e)