import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np

# Read the image to the variable namely img
img = plt.imread("b.jpg")
# plt.imshow(img)
# plt.pause(60)
print(img.shape)
height = img.shape[0]
width = img.shape[1]
print(height)
print(width)
# Reshape the image to one line image
img = img.reshape(width * height, 3)
print(img.shape)

# Using k - means algorithm
kMeans = KMeans(n_clusters=16).fit(img)
# Take the labels and clusters from the trained model
labels = kMeans.predict(img)
clusters = kMeans.cluster_centers_

# Create new image with the same dimension to the reshaped img

# img_new = np.zeros_like(img)
# for i in range(len(img_new)):
#     img_new[i] = clusters[labels[i]]
# img_new = img_new.reshape(height, width, 3)

img_new = np.zeros((height, width, 3), dtype=np.uint8)

for i in range(height):
    for j in range(width):
        img_new[i][j] = clusters[labels[i * width + j]]
plt.imshow(img_new)
plt.pause(30)
