import cv2     # for capturing videos
import math   # for mathematical operations
#import matplotlib.pyplot as plt    # for plotting the images
#%matplotlib inline
#import pandas as pd
#from keras.preprocessing import image   # for preprocessing the images
import numpy as np    # for mathematical operations
#from keras.utils import np_utils
#from skimage.transform import resize   # for resizing images


count = 0
videoName = "film_1"
videoFile = "2K_Footage/" + videoName + ".mp4"
cap = cv2.VideoCapture(videoFile)
frameRate = cap.get(5)
x=1
while(cap.isOpened()):
    frameID = cap.get(1)
    ret, frame = cap.read()
    if(ret != True):
        break
    if(frameID % math.floor(frameRate)==0):
        filename = videoName + "/frame%d.jpg" % count; count+=1
        cv2.imwrite(filename,frame)
cap.release()
