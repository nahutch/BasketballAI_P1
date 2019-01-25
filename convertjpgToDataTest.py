import math   # for mathematical operations
import matplotlib.pyplot as plt    # for plotting the images
#%matplotlib inline
import pandas as pd
from keras.preprocessing import image   # for preprocessing the images
import numpy as np    # for mathematical operations
from keras.utils import np_utils
from skimage.transform import resize   # for resizing images


folderName = "film_2"
data = pd.read_csv(folderName+"/mapping.csv")

imgArr = []
for img_name in data.Image_ID:
    img = plt.imread("" + folderName + "/"+img_name)
    imgArr.append(img)

imgArr = np.array(imgArr)

y = data.Class
dummy_y = np_utils.to_categorical(y)

image = []
for i in range(0,x.shape[0]):
    a = resize(imgArr[i], preserve_range = True, output_shape = (224, 224)).astype(int)
    image.append(a)

imgArr = np.array(image)

from keras.applications.vgg16 import preprocess_input

imgArr = preprocess_input(imgArr, mode='tf')

from sklearn.model_selection import train_test_split
X_train, X_valid, y_train, y_valid = train_test_split(imgArr, dummy_y, test_size = 0.3, random_state = 42)

from keras.models import Sequential
from keras.applications.vgg16 import VGG16
from keras.layers import Dense, InputLayer, Dropout
base_model = VGG16(weights = 'imagenet', include_top = False, input_shape = (224,224,3))

X_train = base_model.predict(X_train)
X_valid = base_model.predict(X_valid)
X_train.shape, X_valid.shape

#X_train = X_train.reshape(208, 7*7*512)
#X_valid = X_valid.reshape(90, 7*7*512)
