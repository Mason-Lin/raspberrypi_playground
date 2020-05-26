import cv2
cap = cv2.VideoCapture(0)

ret, frame = cap.read()
cv2.imwrite('ori.jpg', frame)
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray.jpg', gray)


cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)
fourcc = cv2.VideoWriter_fourcc('F', 'M', 'P', '4')

out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 320))

for i in range(30):
    if not (cap.isOpened()):
        break

    ret, frame = cap.read()
    if ret == True:
        out.write(frame)
    else:
        break

cap.release()
out.release()
cv2.destroyAllwindows()

