# following tutorial on this page: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_drawing_functions/py_drawing_functions.html
import numpy as np
import cv2

#creates black image
img = np.zeros((512,512,3), np.uint8)

#inputs: image, line start, line end, color, thickness
img = cv2.line(img, (0,0), (511,511), (255,0,0), 5)

#inputs: image, top-left corner, bottom-right corner, color, thickness
img = cv2.rectangle(img, (384,0), (510,128), (0,255,0), 3)

#inputs: image, center, radius, color, thickness
img = cv2.circle(img,(447,63), 63, (0,0,255), -1)

#inputs: image, center location, axes length (major,minor), angle of rotation, startAngle, endAngle, color, thickness
img = cv2.ellipse(img,(256,256),(100,50),0,0,360,255,-1)

#array of vertex cordinates
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
#draws a polygon
#note can also be used to effeciently draw a lot of lines
img = cv2.polylines(img,[pts],True,(0,255,255))

#adds text to image
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)

#note: passing -1 for thickness will use the objects default thickness which will fill in most objects

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
