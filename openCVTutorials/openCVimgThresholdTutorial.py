#following tutorial: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_thresholding/py_thresholding.html

import numpy as np
import cv2
from matplotlib import pyplot as plt

#second argument of zero loads image as grayscale. required for threshold function
img = cv2.imread("frame0.jpg",0)

#threshold inputs: source image (should be grayscale), threshold value, max value (given to a pixel if it exceeds the threshold), thresholding style constant
ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

titles = ["Original Image", "Binary", "Binary Inv", "Trunc", "To Zero", "To Zero Inv"]
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],"gray")
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show() #example plot that shows different threshold effects: https://opencv-python-tutroals.readthedocs.io/en/latest/_images/threshold.jpg

img = cv2.medianBlur(img,5)

ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

#adaptive threshold inputs: source image, max value, adaptive thresholding constant, thresholding style constant, block size, C (subtracted from mean)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

titles = ["Original Image", "Globabl Thresh", "Adaptive Mean Thresh", "Adaptive Gaussian Thresh"]
images = [img, th1, th2, th3]

for i in range(4):
    plt.subplot(2,3,i+1), plt.imshow(images[i],"gray")
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show() #example plot: https://opencv-python-tutroals.readthedocs.io/en/latest/_images/ada_threshold.jpg

img = cv2.imread("frame0.jpg",0)

#global thresholding
#here ret value is just the threshold value you pass into the function
ret1,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

# Otsu's thresholding
#here the ret values returned is the optimal thresh value found by Otsu's algorithm
ret2,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Otsu's thresholding after Gaussian filtering
blur = cv2.GaussianBlur(img,(5,5),0)
ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# plot all the images and their histograms
images = [img, 0, th1,
          img, 0, th2,
          blur, 0, th3]
titles = ['Original Noisy Image','Histogram','Global Thresholding (v=127)',
          'Original Noisy Image','Histogram',"Otsu's Thresholding",
          'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]

for i in range(3):
    plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
    plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
    plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
    plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
plt.show() #example plot: https://opencv-python-tutroals.readthedocs.io/en/latest/_images/otsu.jpg

#skipped part on implementation of Otsu's Binarization. It just shows how it works.
