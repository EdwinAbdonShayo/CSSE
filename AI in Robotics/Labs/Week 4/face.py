import os
import numpy as np
import cv2

# Specify the image path directly
image_path = r'AI in Robotics\Labs\Week 4\ces2.jpg'

# Absolute or correct relative path to the Haar Cascade XML files
face_cascade_path = r'AI in Robotics\Labs\Week 4\haarcascade_frontalface_default.xml'
mouth_cascade_path = r'AI in Robotics\Labs\Week 4\haarcascade_mcs_mouth.xml'

if os.path.exists(image_path):
    # Load pre-trained classifiers for face, eye, and mouth detection
    face_detector1 = cv2.CascadeClassifier(face_cascade_path)
    mouth_detector = cv2.CascadeClassifier(mouth_cascade_path)

    if face_detector1.empty() or mouth_detector.empty():
        print("Error loading cascade files. Please check the file paths.")
    else:
        img = cv2.imread(image_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect faces in the grayscale image
        faces_result = face_detector1.detectMultiScale(gray, 1.2, 5)

        for (x, y, w, h) in faces_result:
            # Draw rectangle around face
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Define regions of interest for eyes and mouth within the face
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]

            # Detect mouth (since the mouth is usually in the lower third of the face, adjust the region of interest)
            roi_gray_mouth = gray[y + int(h / 2):y + h, x:x + w]
            roi_color_mouth = img[y + int(h / 2):y + h, x:x + w]
            mouths = mouth_detector.detectMultiScale(roi_gray_mouth, 1.9, 7)

            for (mx, my, mw, mh) in mouths:
                cv2.rectangle(roi_color_mouth, (mx, my), (mx + mw, my + mh), (0, 255, 0), 2)
                break

        cv2.imshow('img', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
else:
    print("No image found at the specified path.")
