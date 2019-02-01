#following tutorial on this page: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_mouse_handling/py_mouse_handling.html
import cv2
import numpy as np

drawing = False #true if mouse pressed
mode = True #True draws rectangles, False draws circles
ix,iy = -1,-1

def listAllAvailableEvents():
    events = [i for i in dir(cv2) if "EVENT" in i]
    print (events)

def drawObject(event,x,y,flags,param):
    global ix,iy,drawing,mode

    if (event == cv2.EVENT_LBUTTONDOWN):
        drawing = True
        ix,iy = x,y
    elif (event == cv2.EVENT_MOUSEMOVE):
        if (drawing == True):
            if (mode == True):
                #cv2.rectangle(img, (ix,iy), (x,y), (0,255,0), -1) #comment out to draw only at the end of the mouse click
                return
            else:
                cv2.circle(img, (x,y), 5, (0,0,255), -1)
    elif (event == cv2.EVENT_LBUTTONUP):
        drawing = False
        if (mode == True):
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),1)
        else:
            cv2.circle(img,(x,y),5,(0,0,255),-1)


img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',drawObject)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if (k == ord("m")):
        mode = not mode
    elif (k == 27): #checks for esc key
        break

cv2.destroyAllWindows()
