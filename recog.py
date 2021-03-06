import cv2
import numpy as np
import sys

facePath = "haarcascade_frontalface_default.xml"
smilePath = "haarcascade_smile.xml"
faceCascade = cv2.CascadeClassifier(facePath)
smileCascade = cv2.CascadeClassifier(smilePath)

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

sF = 1.05

while True:

    ret, frame = cap.read()
    img = frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray, scaleFactor=sF, minNeighbors=8, minSize=(55, 55), flags=cv2.FONT_HERSHEY_SIMPLEX)
    # Rectangle for face

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        smile = smileCascade.detectMultiScale(roi_gray, scaleFactor= 1.7, minNeighbors=22,minSize=(25, 25),flags=cv2.FONT_HERSHEY_SIMPLEX)

        # Rectangle for smile
        for (x, y, w, h) in smile:

            cv2.putText(frame, "Found Smile", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            cv2.rectangle(roi_color, (x, y), (x+w, y+h), (255, 0, 0), 1)

    cv2.imshow('Smile Detector', frame)
    c = cv2.waitKey(7) % 0x100
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()
