import cv2
import datetime
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("Copy_video2.avi", fourcc, 20.0, (640,480))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width : ' + str(cap.get(3)) + ' ' +  'Height' + str(cap.get(4))
        datet = str(datetime.datetime.now())
        frame = cv2.putText(frame, datet ,(10,50) , font, 1 , (0, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow('frame', frame)
        out.write(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else: 
        break
cap.release() 
cv2.destroyAllWindows()       




