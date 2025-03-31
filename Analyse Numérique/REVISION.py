import math
import numpy as np

def f1(x):
    return x ** 3 + x

def f2(x) :
    return math.sin(x)

def f3(x):
    return 2 * x * math.exp(-x**2)

def f4(x):
    return 4 * x + 2

def F1(x):
    return (x**4)/4 - (x**2)/2


def F2(x):
    return -np.cos(x)


def F3(x):
    X = -x**2
    return -np.exp(X)


def F4(x):
    return 2*(x**2)+2*x

def erreur()

