import numpy as np
from numpy import *
import matplotlib.pyplot as plt

X = np.linspace(0, 4*pi, int(4*pi/(10**-4)))
plt.plot(X, sin(X), 'r', label='sin(x)')
plt.plot(X, cos(X), 'b', label='cos(x)')
plt.ylabel('y=f(x)')
plt.xlabel('x')
plt.grid()
plt.title("Awesome Graph you exist")
plt.legend()
plt.show()