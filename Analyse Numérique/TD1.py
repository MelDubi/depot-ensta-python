import numpy as np
import matplotlib.pyplot as plt



def f1(x):
    return x**3 - x


def f2(x):
    return np.sin(x)


def f3(x):
    return 2*x*np.exp(-x**2)


def f4(x):
    return 4*x+2


def F1(x):
    return (x**4)/4 - (x**2)/2


def F2(x):
    return -np.cos(x)


def F3(x):
    X = -x**2
    return -np.exp(X)


def F4(x):
    return 2*(x**2)+2*x


def rectangleGauche(a,b,n,f):
    pas = (b-a)/n
    I=0
    for i in range(n):
        ai =a+i*pas
        I += f(ai)
    return I*pas


a = 0
b = 5
f_test = f1
F_test = F1

n_test = (10, 100, 1000, 10000)
res = []
I_true = F_test(b)-F_test(a)

for n in n_test:
    I_rg = rectangleGauche(a, b, n, f_test)
    res.append(np.abs(I_true-I_rg))

plt.loglog(n_test, res)
plt.show()