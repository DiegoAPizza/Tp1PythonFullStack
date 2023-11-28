import cv2
import os
#import imutils
cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default')



while True:
    
    ret, frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
       
    
    cv2.imshow('frame',frame)
    k=cv2.waitKey(30)
    if k==27:
        break
cap.release()
cv2.destroyAllWindows()    