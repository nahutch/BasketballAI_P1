#following tutorial on this page: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html
import numpy as np
import cv2

#argument can be name of video file or a device index (0 for first device like built in camera)
cap = cv2.VideoCapture("film_0.mp4")

if (not cap.isOpened()):
    print("error opening video stream")
    quit()

#get takes in a property identifier 0-18.
fps = cap.get(5) #this property is the frames per second
waitTime = int(1000/fps) #calculates the time to wait in between displaying frames. can be altered to speed up or slow down watching a video

#set modifies a propery identifier. Note not all propIDs can be modified
#this should modify the width then height
#currently not working properly
ret = cap.set(3,224)
print (ret)
ret = cap.set(4,224)
print (ret)

width = int(cap.get(3))
height = int(cap.get(4))

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v') #code used to specify the codec. it is platform dependent. pass -1 instead of this variable and system will print out available codes
out = cv2.VideoWriter('output.mp4',fourcc, fps, (width,height))

while (cap.isOpened()):
    ret, frame = cap.read()

    if(ret != True): #checks if frame read correctly. Generally returns false at end of file
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame",gray)

    out.write(frame)

    if cv2.waitKey(waitTime) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
