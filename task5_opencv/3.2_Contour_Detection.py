import cv2
image = cv2.imread('example.jpg', 0)
_, thresh = cv2.threshold(image, 127, 255, 0)
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
output = cv2.drawContours(cv2.cvtColor(image, cv2.COLOR_GRAY2BGR), contours, -1, (0, 255, 0), 3)
cv2.imwrite('output.png', output)