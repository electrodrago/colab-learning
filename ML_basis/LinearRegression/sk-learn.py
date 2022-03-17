import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from sklearn import linear_model

# Data
A = np.array([[2, 5, 7, 9, 11, 16, 19, 23, 22, 29, 29, 35, 37, 40, 46]]).T
b = np.array([[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]]).T

# print(A)

lr = linear_model.LinearRegression()
lr.fit(A, b)
print(lr.intercept_[0])
print(lr.coef_[0][0])

plt.plot(A, b, 'ro')
x0 = np.array([[1, 46]]).T
y0 = x0*lr.coef_ + lr.intercept_
plt.plot(x0, y0)
plt.show()
