import cv2
from pyzbar.pyzbar import decode
import time

cam = cv2.VideoCapture(0)
cam.set(3, 640)  
cam.set(4, 480)  

camera = True

while camera:
    success, frame = cam.read()

    if not success:
        break

    for barcode in decode(frame):
        print("Type:", barcode.type)
        print("Data:", barcode.data.decode('utf-8'))
        time.sleep(6)

    cv2.imshow("QR Code Scanner", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
