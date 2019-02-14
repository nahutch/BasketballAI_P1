#following tutorial: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_core/py_optimization/py_optimization.html

import time
import cv2

img1 = cv2.imread("frame0.jpg")

#stores the start of code execution. Can also use python's time module or profile module to measure code performance
event1 = cv2.getTickCount() #uses cv's tick timing
time1 = time.time() #uses python's timing module

#run code you want to measure here
for i in range(5, 49, 2):
    img1 = cv2.medianBlur(img1,i)

#calculates time it took to run the code
event2 = cv2.getTickCount()
time2 = time.time()
time = (event2 - event1) / cv2.getTickFrequency()
print ("OpenCV's time measurement:" ,time)
print ("python's time module measurment:", (time2 - time1))


print("is cv running optimized code:",cv2.useOptimized()) #optimization should be enabled by default
cv2.setUseOptimized(False); print("turn off optimization")
print("is cv running optimized code:",cv2.useOptimized())

"""
performance optimization techniques
1. avoid loops
2. vectorize the algorithm/code. Numpy and OpenCV are optimized for vector operations
3. exploit cache coherence
4. avoid making copies of arrays

Cython and other similar libraries can speed up code 

can also measure performance with Ipython but I don't currently use that
"""
