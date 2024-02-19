import cv2 


img = cv2.imread("lena.jpg", 1)

img = cv2.line(img , (0,0) , (255,255) , (147 , 96 , 44), 5)
img = cv2.arrowedLine(img , (0,255) , (255,255), (255, 0 , 0) , 3)
img = cv2.rectangle(img, (384, 0), (510,128) , (0,0,255), 10)
img = cv2.circle(img, (447,63), 63, (0,243,76), -1)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'open cv', (10,500), font, 4, (156, 187, 87), 7, cv2.LINE_AA)

cv2.imshow("image.png", img)
cv2.imwrite("Copy_of Image.png", img)
cv2.waitKey(0)
cv2.destroyAllWindows()