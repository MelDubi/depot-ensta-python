import matplotlib.pyplot as plt
import numpy as np

a = -1


def toto(t, y):
    return -a * y


def euler(t0, tmax, h, y0, f):
    t = t0
    saveT = [t0]
    saveY = [y0]
    y = y0
    while t < tmax:
        y = y + h * f(t, y)
        t = t + h
        saveT.append(t)
        saveY.append(y)
    return saveT, saveY


[TA, YA] = euler(0, 10, 0.01, 1, toto)

plt.plot(TA, YA)
plt.show()

plt.plot(TA, np.exp(-a*TA))
plt.show()
