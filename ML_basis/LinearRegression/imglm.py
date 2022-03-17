from sklearn import linear_model
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from PIL import *


# Read image to numpy array or pandas dataframe
imFrame = Image.open('../LinearRegression/beach.jpg')
[width, height] = imFrame.size
npFrame = np.array(imFrame.getdata())
print(npFrame)

# Fitting model of RGB
x1 = np.array([npFrame[:, 0]]).T
x2 = np.array([npFrame[:, 1]]).T
y = np.array([npFrame[:, 2]]).T
A = np.concatenate((x1, x2), axis=1)
# print(A)
lr = linear_model.LinearRegression()
lr.fit(A, y)
print(lr.coef_)

img_new = im = Image.new(mode="RGB", size=(width, height))

for i in range(width):
    for j in range(height):
        [r, g, b] = imFrame.getpixel((i, j))
        b = lr.predict([[r, g]])
        value = (r, g, int(b))
        img_new.putpixel((i, j), value)

# for i in range(len(img_new)):
#     img_new[i] = [img[i][0], img[i][1], lr.predict([[img[i][0], img[i][1]]])]
# img_new = img_new.reshape(height, width, 3)
plt.imshow(img_new)
plt.pause(60)