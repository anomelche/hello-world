#!/usr/bin/env python

from matplotlib import pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 101)
y = x**2
plt.plot(x, y)
plt.plot([-3, -1], [90, 70], '-k')
plt.plot([-3, -1], [70, 90], '-k')
plt.plot([1, 3], [90, 70], '-k')
plt.plot([1, 3], [70, 90], '-k')
plt.ylim(-10, 100)
plt.show()
