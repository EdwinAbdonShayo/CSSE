
import cv2
print(cv2.__version__)

Img = cv2.imread("AI in Robotics/Labs/Week 3/image.jpg")

cv2.imshow('Original', Img)

print(f"Size of the image: {Img.size}")
print(f"Shape of the image: {Img.shape}")

grayImg = cv2.cvtColor(Img, cv2.COLOR_BGR2GRAY)

blurImg = cv2.GaussianBlur(Img, (9,9), 0)

cv2.imshow('Grayscale', grayImg)

threshold_value = 127

_, binaryImg = cv2.threshold(grayImg, threshold_value, 255, cv2.THRESH_BINARY)

cv2.imshow('Binary Image', binaryImg)
cv2.imshow('Blured Image', blurImg)

cv2.waitKey(0)
