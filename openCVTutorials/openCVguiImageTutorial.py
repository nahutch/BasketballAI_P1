#following tutorial on this page: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_image_display/py_image_display.html
import numpy as np
import cv2

#path to image either through the working directory or full path
path = "frame0.jpg"

#function imread reads an image
#first argument is path
#optional second argument specifies how image is read. default is cv2.IMREAD_COLOR. other options are cv2.IMREAD_GRAYSCALE, cv2.IMREAD_UNCHANGED
imgColor = cv2.imread(path, cv2.IMREAD_COLOR)
imgGray = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
imgUnchanged = cv2.imread(path, cv2.IMREAD_UNCHANGED)
#if it can't find the image, will put a null object, but won't throw an error

cv2.namedWindow("imageGray",cv2.WINDOW_NORMAL)

#function imshow displays an image using cv
#first arugment is window name, can be any name
#second argument is image variable
cv2.imshow ("imageColor",imgColor)
cv2.imshow ("imageGray",imgGray)
cv2.imshow("imgageUnchanged",imgUnchanged)

k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyWindow("imageGray")
elif k == ord('s'): # wait for 's' key to save and exit
    #function imwrite saves an image
    cv2.imwrite('grayImage.png',imgGray)
    cv2.destroyWindow("imageGray")

#note waitKey only works when while the window is in focus. If the command line is in focus nothing happens
cv2.waitKey(0)
cv2.destroyAllWindows()

#can also use matplotlib to load and/or display images
#warning color images loaded by openCV will not be displayed properly by matplotlib and vice versa because openCV uses BGR, but matplotlib uses RGB
