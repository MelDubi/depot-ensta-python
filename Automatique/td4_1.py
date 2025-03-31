# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import math

g = 9.81
m = 1
l = 2 * m
u = 0
mu = 0.1

def evolution_function (X,u):

    x1_p = X[1]
    x2_p = 1/(m * (l**2)) * (u - (m * g * l * np.sin(X[0])) - (mu * X[1]))
    Xdot = np.array([x1_p,x2_p])

    return(Xdot)

h=0.05
#T= np.arange(0,11,h)
T= np.linspace(0,10,200)
X = np.array([1,0])

etats_euler = []
etats_RK2 = []

for t in T:
    k1 = evolution_function(X,u)
    a= X + h*k1
    k2 = evolution_function(a,u)
    X = X+h * k1
    RK2 = X+(h/2 * (k1 + k2))
    etats_euler.append(X)
    etats_RK2.append(RK2)

plt.figure(1)

etats_euler = np.array(etats_euler)
plt.plot(T,etats_euler[:,0])
plt.plot(T,etats_euler[:,1])

plt.figure(2)

etats_RK2 = np.array(etats_RK2)
plt.plot(T,etats_RK2[:,0])
plt.plot(T,etats_RK2[:,1])
plt.show()