import cv2, mediapipe as mp, serial
ard = serial.Serial("/dev/cu.usbserial-110", 9600)
cap = cv2.VideoCapture(0)
mp_pose = mp.solutions.pose.Pose()
print(".........")
while True:
   res, frame = cap.read()
   if not res:
        break
   results = mp_pose.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
   if results.pose_landmarks: 
      ard.write(b'1')
   elif not results.pose_landmarks:
      ard.write(b'0')
   cv2.imshow('rec', frame)
   if cv2.waitKey(1) == 27: break