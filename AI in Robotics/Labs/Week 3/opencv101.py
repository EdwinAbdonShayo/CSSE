
import cv2
print(f'OpenCV version installed: {cv2.__version__}')

# Loading the image

Img = cv2.imread("AI in Robotics/Labs/Week 3/image.jpg")

# Printing the size of the image on the terminal

print(f"Size of the image: {Img.size}")
print(f"Shape of the image: {Img.shape}")

# Converting the RGB image to grayscale

grayImg = cv2.cvtColor(Img, cv2.COLOR_BGR2GRAY)

# Printing both the original and grayscale image on a window

cv2.imshow('Original', Img)
cv2.imshow('Grayscale', grayImg)

# Closing the generated windows

cv2.waitKey(0)
cv2.destroyAllWindows()

# Creating a threshold and converting the grayscale image into binary

threshold_value = 127

_, binaryImg = cv2.threshold(grayImg, threshold_value, 255, cv2.THRESH_BINARY)

# Printing both the grayscale and the binary image

cv2.imshow('Grayscale', grayImg)

cv2.imshow('Binary Image', binaryImg)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Bluring the grayscale image

blurImg = cv2.GaussianBlur(grayImg, (9,9), 0)

# Printing both the grayscale and the blured image

cv2.imshow('Grayscale', grayImg)
cv2.imshow('Blured Image', blurImg)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Extracting the edges of the grayscale image

low_threshold = 50
high_threshold = 150

edges = cv2.Canny(grayImg, low_threshold, high_threshold)

# Printing both the grayscale and the edges

cv2.imshow('Grayscale', grayImg)
cv2.imshow('Edges', edges)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Resizing the origal image to half the size

height = int(Img.shape[0] / 2)
width = int(Img.shape[1] / 2)

dimensions = (width, height)

resizeImg = cv2.resize(Img, dimensions)

# Printing both the original image and the resized image

cv2.imshow('Original', Img)
cv2.imshow('Resized Original', resizeImg)

cv2.waitKey(0)
cv2.destroyAllWindows()