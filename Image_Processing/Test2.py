
import cv2
capature = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("output.avi",fourcc , 20.0, (640,480))
while(capature.isOpened()):
    ret , frame = capature.read()
    if ret == True:
       print(capature.get(cv2.CAP_PROP_FRAME_WIDTH))
       print(capature.get(cv2.CAP_PROP_FRAME_HEIGHT))
       out.write(frame)
       gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
       cv2.imshow('frame', gray)
       if cv2.waitKey(1) & 0xFF == ord('q'):
          break
    else:
       break   

capature.release() 
cv2.destroyAllWindows()       

