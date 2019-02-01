# following tutorial: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_core/py_basic_ops/py_basic_ops.html#basic-ops

import numpy as np
import cv2

img = cv2.imread("frame0.jpg")

px = img[100,100]
print ("pixel value:", px)
#prints pixel value,
#for color photos, prints BGR value
# for grayscale, prints intensity

blue = img[100,100,0]
print ("pixel blue value:", blue)

img[100,100] = [255,255,255]
print ("changed pixel value:", img[100,100])

#faster pixel accessing and editing method using numpy
print ("pixel red value:", img.item(10,10,2))
img.itemset((10,10,2), 100)
print ("new pixel red value:", img.item(10,10,2))

print ("image shape:", img.shape)

print("image size", img.size)

#note: a large number of OpenCV-python errors are caused by invalid datatypes
print("image datatype", img.dtype)

#copies part of the picture to another part of picture
# height then width
ball = img[243:263, 323:343]
img[300:320, 600:620] = ball

#splits and merges different pixel types. these are slow
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

#uses numpy indexing which is much faster than cv2 operations
b = img[:,:,0] #gets just blue pixels
#sets all red pixels to zero
img[:,:,2] = 0

print("replicated ball and removed red coloring")
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()






BLUE = [255,0,0]

img1 = cv2.imread('opencv-logo-white.png')

#inputs: source image, top border width (bw), bottom bw, left bw, right bw, borderType
replicate = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_WRAP)
constant= cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)

print("made image borders")
cv2.imshow("image",img1)
cv2.imshow("replicate",replicate)
cv2.imshow("reflect",reflect)
cv2.imshow("reflect101",reflect101)
cv2.imshow("wrap",wrap)
cv2.imshow("constant",constant)
cv2.waitKey(0)
cv2.destroyAllWindows()


""" commenting out because pyplt is throwing error
error seems to be caused by the interaction between python and OSX.
Need to install python framework build
more info: https://matplotlib.org/faq/osx_framework.html

from matplotlib import pyplot as plt

plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')

plt.show()
"""
