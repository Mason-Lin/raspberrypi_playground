import os
os.environ['LD_PRELOAD'] = "/usr/lib/arm-linux-gnueabihf/libatomic.so.1.2.0"

import cv2
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)
fourcc = cv2.VideoWriter_fourcc(*'XVID')

out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 320))

for i in range(150):
    if not (cap.isOpened()):
        break

    ret, frame = cap.read()
    if ret == True:
        out.write(frame)
    else:
        break

cap.release()
