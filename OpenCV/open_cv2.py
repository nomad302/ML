import cv2

img = cv2.imread('dog.png')

gray = cv2.imread('dog.png',cv2.IMREAD_GRAYSCALE)

cv2.imshow('Dog image',img)

cv2.imshow('Gray Dog image',gray)

# it will wait infinitely to close window
cv2.waitKey(0)

cv2.distroyAllWindows()
