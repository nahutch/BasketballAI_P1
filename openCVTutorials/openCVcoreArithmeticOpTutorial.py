#following tutorial: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_core/py_image_arithmetics/py_image_arithmetics.html

import numpy as np
import cv2



scalar1 = np.uint8([250])
scalar2 = np.uint8([10])

print (cv2.add(scalar1,scalar2)) #cv addition: 250 + 10 = 260 => 255

print (scalar1 + scalar2) #numpy addition: 250 + 10 = 260 % 256 = 4
#since they are 8 bit arrays, they max out their size at 2^8 - 1 = 255
#Both images should be of same depth and type, or second image can just be a scalar value.
#openCV provides better results when adding images

img1 = cv2.imread("frame0.jpg")
img2 = cv2.imread("opencv-logo-white.png")

#need same sized image in order to add them
img1_resized = cv2.resize(img1, (img2.shape[1], img2.shape[0]))

addedImg = cv2.add(img1_resized,img2)

#inputs: img1, alpha, img2, beta, lambda
#equation dst = alpha * img1 + beta * img2 + lambda
blendedImg = cv2.addWeighted(img1_resized, 0.7, img2, 0.3, 0)

cv2.imshow("added Image",addedImg)
cv2.imshow("blended Image",blendedImg)
cv2.waitKey(0)
cv2.destroyAllWindows()

#selecting region of image (roi)
rows,cols,channels = img2.shape
roi = img1[0:rows,0:cols]

#creates mask and inverse mask
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

#blacks out area of roi
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

#get only the logo
img2_fg = cv2.bitwise_and(img2,img2,mask=mask)

dst = cv2.add(img1_bg,img2_fg)
img1[0:rows,0:cols] = dst

cv2.imshow("grayed image",img2gray)
cv2.imshow("mask",mask)
cv2.imshow("inverse mask",mask_inv)
cv2.imshow("background image",img1_bg)
cv2.imshow("foreground image",img2_fg)
cv2.imshow("destination roi image",dst)
cv2.imshow("full result image" , img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
