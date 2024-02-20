import cv2
import numpy as np
def event_click(event , x, y, flag ,param):
    if event ==cv2.EVENT_LBUTTONDOWN:
        blue = img[x,y,0]
        green = img[x,y,1]
        red = img[x,y,2]
        cv2.circle(img, (x, y), 3, (0,0,255), -1)
        mycolorImage = np.zeros((512,512,3), np.uint8)
        mycolorImage[:] = [blue, green, red]
        cv2.imshow("image", mycolorImage)

# img = np.zeros((512,512, 3), np.uint8)
img = cv2.imread('lena.jpg')
points = []
cv2.imshow("image", img)
cv2.setMouseCallback('image',event_click)
cv2.waitKey(0)
cv2.destroyAllWindows()