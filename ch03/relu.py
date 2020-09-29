# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt


def relu(x):
    return np.maximum(0, x)


X = np.arange(-0.5, 5.0, 0.1)
Y = relu(X)
plt.plot(X, Y)
plt.ylim(-1.0, 5.5)
plt.show()
