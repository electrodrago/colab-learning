import numpy as np
import matplotlib
import matplotlib.pyplot as plt


# Data
A = [2, 5, 7, 9, 11, 16, 19, 23, 22, 29, 29, 35, 37, 40, 46]
b = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# plt.plot(A, b, 'ro')

A = np.array([A]).T
b = np.array([b]).T

ones = np.ones((A.shape[0], 1), dtype=np.int8)

A = np.concatenate((A, ones), axis=1)

# x = (At.A)^-1.At.b
x = (np.linalg.inv(A.transpose().dot(A)).dot(A.transpose())).dot(b)
print(x)
