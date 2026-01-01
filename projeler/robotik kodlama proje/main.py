import cv2
import numpy as np
import serial
import time

# Arduino bağlantısı (COM portu değişebilir!)
arduino = serial.Serial('COM3', 9600)
time.sleep(2)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # RENK ARALIKLARI
    colors = {
        "RED": (
            np.array([0, 120, 70]),
            np.array([10, 255, 255])
        ),
        "GREEN": (
            np.array([36, 50, 70]),
            np.array([89, 255, 255])
        ),
        "BLUE": (
            np.array([90, 50, 70]),
            np.array([128, 255, 255])
        )
    }

    for color_name, (lower, upper) in colors.items():
        mask = cv2.inRange(hsv, lower, upper)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            c = max(contours, key=cv2.contourArea)
            if cv2.contourArea(c) > 1000:
                x, y, w, h = cv2.boundingRect(c)
                cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
                cv2.putText(frame, color_name, (x, y-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)

                # Arduino'ya komut gönder
                arduino.write(color_name.encode())
                time.sleep(1)

    cv2.imshow("Renk Algilama", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
