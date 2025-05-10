import cv2
import numpy as np
image = np.zeros((512, 512, 3), np.uint8)
cv2.line(image, (0, 0), (511, 511), (255, 0, 0), 5)
cv2.rectangle(image, (384, 0), (510, 128), (0, 255, 0), 3)
cv2.circle(image, (447, 63), 63, (0, 0, 255), -1)
cv2.putText(image, 'OpenCV', (10, 500), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2)
cv2.imwrite('output.png', image)