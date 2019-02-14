#following tutorial: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_colorspaces/py_colorspaces.html#converting-colorspaces

import numpy as np
import cv2

#there are more than 150 color-space conversions methods available in OpenCV
#why so many?

#gets all possible color space conversion flags
flags = [i for i in dir(cv2) if i.startswith("COLOR_")]
#print (flags)

#converts a bgr color to hsv
green = np.uint8([[[0,255,0]]])
hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
print (hsv_green)


#extracts any blue colored object using the built in video camera
#can detect my blue eyes if I get close and widen them
cap = cv2.VideoCapture(0)
while(1):
    #take each frame
    _, frame = cap.read()

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    mask = cv2.inRange(hsv,lower_blue,upper_blue)

    res = cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("result",res)
    k = cv2.waitKey(5)& 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
