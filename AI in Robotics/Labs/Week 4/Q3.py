import cv2

# Initialize face and eye detectors
face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
cap = cv2.VideoCapture(0)

while cap.isOpened():
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    faces = face_detector.detectMultiScale(gray, 1.1, 7)  # Detect faces

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 3)  # Draw face rectangle
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_detector.detectMultiScale(roi_gray)  # Detect eyes

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 5)  # Draw eye rectangle

    cv2.imshow("window", frame)  # Show frame

    if cv2.waitKey(1) & 0xFF == ord(' '):  # Quit on 'space' key
        break

    if cv2.getWindowProperty("window", cv2.WND_PROP_VISIBLE) < 1:  # Close if window closed
        break

cap.release()
cv2.destroyAllWindows()
