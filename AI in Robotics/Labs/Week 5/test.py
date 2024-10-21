
import cv2

# Load the pre-trained Haar Cascade for bottle detection (you need to provide this .xml file)
bottle_cascade = cv2.CascadeClassifier('AI in Robotics\Labs\Week 5\Samples\classifier\cascade.xml')

# Load the image where you want to detect the bottle
image_path = 'AI in Robotics\Labs\Week 5\ottle_image.jpg'
img = cv2.imread(image_path)

# Convert the image to grayscale for better performance of the cascade
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect bottles in the image
bottles = bottle_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Check if any bottles are detected and print the result to the terminal
if len(bottles) > 0:
    print(f"Bottle(s) detected: {len(bottles)} bottle(s) found.")
else:
    print("No bottles detected.")

# Draw rectangles around the detected bottles
for (x, y, w, h) in bottles:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Display the output image
cv2.imshow('Detected Bottles', img)

# Wait for a key press and close the image window
cv2.waitKey(0)
cv2.destroyAllWindows()
