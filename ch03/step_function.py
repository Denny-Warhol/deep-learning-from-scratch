# coding: utf-8
import numpy as np
import matplotlib.pylab as plt


def step_function(x):
    return np.array(x > 0, dtype=np.int)


X = np.arange(-5.0, 5.0, 0.1)
Y = step_function(X)
plt.plot(X, Y)
plt.ylim(-0.1, 1.1)  # specify y-axis range
plt.show()


def normal_step_function(x):
    # if x > 0:
    #     return 1
    # else:
    #     return 0
    return 1 if x > 0 else 0
