import cv2
import numpy as np

# Kamerayı başlat
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Görüntüyü HSV formatına çevir
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # KIRMIZI renk aralığı
    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])

    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])

    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = mask1 + mask2

    # Gürültü temizleme
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    # Konturları bul
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        c = max(contours, key=cv2.contourArea)

        if cv2.contourArea(c) > 500:
            x, y, w, h = cv2.boundingRect(c)

            # Nesneyi çiz
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Merkez noktası
            cx = x + w // 2
            cy = y + h // 2
            cv2.circle(frame, (cx, cy), 5, (255, 0, 0), -1)

            print("Nesne Konumu:", cx, cy)

    cv2.imshow("Nesne Takibi", frame)
    cv2.imshow("Maske", mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
