import cv2
image = cv2.imread('example.jpg', 0)
_, thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
cv2.imwrite('output.png', thresh)