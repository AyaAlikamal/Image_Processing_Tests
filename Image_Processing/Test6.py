import cv2
import numpy
def click_event(event, x, y, flage, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ',', y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ' , ' + str(y)
        cv2.putText(img , strXY,(x, y), font, .5, (255,255, 0), 2)
        cv2.imshow('image', img)
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[x, y , 0]
        green = img[x, y , 1]
        red = img[x, y , 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strRGB = str(blue) + ' , ' + str(green) + ' , ' + str(red)
        cv2.putText(img , strRGB,(x, y), font, .5, (0, 255,255), 2)
        cv2.imshow('image', img)  

# img = numpy.zeros((512,512,3), numpy.uint8)
img = cv2.imread("lena.jpg", 1)
cv2.imshow("image", img)
cv2.setMouseCallback('image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
       