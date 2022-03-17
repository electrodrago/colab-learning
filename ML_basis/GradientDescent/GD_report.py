import numpy as np
import matplotlib.pyplot as plt


eta = 0.2 # Learning rate


def cost(x):
    return 0.5 * (x-1)**2 - 2


def grad(x):
    return x - 1


def GD(x0):
    x_list = [x0]
    for i in range(10000):
        x_step = x_list[-1] - eta * grad(x_list[-1])
        if abs(grad(x_step)) < 0.001:
            break
        x_list.append(x_step)
    return x_list, i


x = np.linspace(-10, 10, 200)
y = 0.5 * (x-1)**2 - 2

plt.plot(x, y, 'r')
x_list1, i1 = GD(-8)
x_list2, i2 = GD(8)
print(i1, i2)
for i in range(len(x_list1)):
    fx = cost(x_list1[i])
    plt.scatter(x_list1[i], fx, color='blue')
plt.show()

for i in range(len(x_list2)):
    fx = cost(x_list2[i])
    plt.scatter(x_list2[i], fx, color='green')
plt.show()