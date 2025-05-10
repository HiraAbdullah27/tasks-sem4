import cv2
image = cv2.imread('example.jpg', 0)
sift = cv2.SIFT_create()
keypoints, descriptors = sift.detectAndCompute(image, None)
output = cv2.drawKeypoints(image, keypoints, None)
cv2.imwrite('output.png', output)