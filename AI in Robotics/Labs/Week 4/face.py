import numpy as np
import cv2

print(f'Here is Numpy Version {np.__version__}')

face_detector = cv2.CascadeClassifier('AI in Robotics/Labs/Week 4/haarcascade_frontalface_default.xml')
mouth_detector = cv2.CascadeClassifier('AI in Robotics/Labs/Week 4/haarcascade_mcs_mouth.xml')

img = cv2.imread('AI in Robotics/Labs/Week 4/ces1.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = cv2.equalizeHist(gray)

gray = cv2.GaussianBlur(gray, (9, 9), 0)

faces = face_detector.detectMultiScale(gray, 1.1, 3)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    
    roi_gray = gray[y + int(h/2):y + h, x:x + w]
    roi_color = img[y + int(h/2):y + h, x:x + w]

    mouths = mouth_detector.detectMultiScale(roi_gray, 1.01, 7)
    
    for (mx, my, mw, mh) in mouths:
        cv2.rectangle(roi_color, (mx, my), (mx + mw, my + mh), (0, 255, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
