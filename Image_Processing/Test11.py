import cv2
import numpy as np

img1 = np.zeros((512,512,3), np.uint8)
img4 = np.zeros((512,512,3), np.uint8)

img3 = cv2.rectangle(img1, (400,200), (300, 100), (255,255,255),-1)
img2 = cv2.rectangle(img4, (200,0), (300, 100), (255,255,255),-1)
and_operator = cv2.bitwise_and(img3, img2)
or_operator =  cv2.bitwise_or(img3, img2)
xor_operator =  cv2.bitwise_xor(img3, img2)
not_operator =  cv2.bitwise_not(img4)
# cv2.imshow("image",img3)
# cv2.imshow("image2",img2)
cv2.imshow("and_operator", and_operator)
cv2.imshow("or_operator", or_operator)
cv2.imshow("xor_operator", xor_operator)
cv2.imshow("not_operator", not_operator)
cv2.waitKey(0)
cv2.destroyAllWindows()