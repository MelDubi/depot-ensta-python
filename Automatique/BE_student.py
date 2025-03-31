# -*- coding: utf-8 -*-

import math

import numpy

import car
import numpy as np
import pylab as plt
from math import *
from scipy.signal import place_poles


def car_dyn(X, u):
    """
    Computes the derivative of the car's state vector x according to
    x and the control u
    """
    x, y, theta, v, delta = X

    xdot = np.array([v * np.cos(delta) * np.cos(theta),
                    v * np.cos(delta) * np.sin(theta),
                    (v * np.sin(delta)) / L_car,
                    u[0],
                    u[1]]
                    )
    return xdot


def observation_func(x, track):
    d = car.dist_to_track(x, track)
    return np.array([d, x[3], x[4]])


L_car = 3  # car length (don't mess it up with L from KLH control)
r0 = 5  # reference distance to track
v0 = 7  # reference speed

# linear system
# Compute A, B, C, D and E
A=np.array([[0,v0,0,0],[0,0,0,v0/L_car],[0,0,0,0],[0,0,0,0]])
B=np.array([[0,0],[0,0],[1,0],[0,1]])
C=np.array([[1,0,0,0],[0,0,1,0],[0,0,0,1]])
D=np.array([[0,0],[0,0],[0,0]])
E=np.array([[1,0,0,0],[0,0,1,0]])

# eigenvalues
# choose pcom and pobs
# Pole de commande
pcom=np.array([-2,-1.01,-1.02,-1.03])
# Pole observateur
pobs=np.array([-2.01,-2.02,-2.03,-2.04])

# compute KLH control

# Calcul de K
res = place_poles(A, B, pcom)
K = res.gain_matrix

# Calcul de L
res = place_poles(A.T, C.T, pobs)
L = res.gain_matrix.T

# Calcul de H
H = -np.linalg.inv(E@np.linalg.inv(A-B@K)@B)

# define the evolution function of the regulator
#(xr, w, y) --> (z, v, theta)
def regul(xr, w, y):
    xrdot = (A-B@K-L@C)@xr+B@H@(w-wbar)+L@(y-ybar)
    return xrdot


# equilibrium point
ubar = np.zeros(2)
xrbar = np.array([5, pi/2, 7, 0])
wbar = E@xrbar
ybar = np.array([5, 7, 0])

track = np.array([
                [-10, -12, -10, 0, 10, 20, 40, 32, 35, 30,  20,  0,   -10],
                [-5,   0,  5,  50, 60, 60, 50, 15, 5,  -10, -15, -15, -5]
                ])

#Initial conditions
x = np.array([-18, 0, np.pi/2, v0, 0])  # initial state for car
#xr =  # initial state for observer
xr = np.array([0, 0, 0, 0])
u = np.array([0, 0])  # only for testing purposes
w = np.array([r0, v0])  # reference


h = 0.05 # timestep
T = np.arange(0, 1200, h)
D = []  # list of distances from the car to the track at each timestep
for t in T:
    # sensors
    y = observation_func(x, track)
    D.append(y[0])
    # control
    u = -K @ xr + H @ (w-wbar)
    # updates for the car and the regulator
    # RK2 for regulator
    k1 = regul(xr, w, y)
    k2 = regul(xr + h * k1, w, y)
    xr = xr + h * (k1 + k2) / 2
    # RK2 for car
    k1 = car_dyn(x, u)
    k2 = car_dyn(x + h * k1, u)
    x = x + h * (k1 + k2) / 2
    car.draw(x, y[0], track, size=150)
    print(t)
# plot the tracking error wrt time
# plot the control signals wrt time

plt.show()