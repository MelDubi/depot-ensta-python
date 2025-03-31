# -*- coding: utf-8 -*-

import car
import numpy as np
import pylab as plt
from scipy.signal import place_poles

plt.close("all")


def car_dyn(x, u):
    """
    Compute the derivative of the car's state vector x according to
    x and the control u
    Input: x, u, 1D numpy array
    Output: time derivative of x, 1D numpy array
    """
    pass


def output_sensors(x, track):
    """
    Simulate the car's sensors.
    Input:  x: state vector, 1D numpy array
            track: track edges, 2D numpy array
    Output: 1D numpy array containing:
            distance to the track, float
            speed, float
            wheels angle, float
    """

    d = car.dist_to_track(x, track)
    # print("Measured distance --> ", d)
    pass


def evol_regulator(xr, w, y):
    """
    Compute the time derivative of the state vector / observer
    used into the regulator.
    Input:  xr, regulator state vector, 1D numpy array
            w, set point, 1D numpy array
            y, output sensors, 1D numpy array
    Output: time derivative of xr, 1D numpy array
    """
    pass

L_car = 3  # car length (don't mess it up with L from KLH control)
r0 = 5  # reference distance to track
v0 = 7  # reference speed

# track
track = np.array([[-10, -12, -10, 0, 10, 20, 32, 35, 30, 20, 0, -10],
                  [-5, 0, 5, 15, 20, 20, 15, 5, 0, -10, -15, -5]])

# linear system
# define here A, B and C

# Eigenvalues
# compute and display eigenvalues of matrix A, is it a stable system ?

# compute KLH control matrices

# linearization point

# initial conditions
X = np.array([-17, 0, np.pi / 2, 1, -0.15])  # initial state for car
print("X dim :", X.shape)
Xr = np.zeros(4)
W = np.zeros(2)
Y = np.zeros(3)
d = car.dist_to_track(X, track)

# the following line draws once the car and the track. Subsequent calls should
# update the car position in order to show its trajectory around the track.
car.draw(X, d, track)

# Regulator
# Compute Ar, Br, Cr and Dr for the regulator

# intial control
U = np.array([0, 0])
# initial state for observer
Xr = np.zeros(4)

# Simulation time
dt = 0.05
tmax = 40
T = np.arange(0, tmax, dt)
D = np.zeros_like(T)

for k, t in enumerate(T):
    # this loop does nothing useful in its current state
    # update the control
    U = U

    # RK2 for regulator
    Xr = Xr

    # RK2 for car
    X = X

    print("t --> ", t)
    print("U --> ", U)
    print("X --> ", X)
    D[k] = car.dist_to_track(X, track)
    print("Distance d --> ", D[k])

    # DRAW !
    car.draw(X, Y[0], track, size=90)


plt.figure(2)
plt.plot(T, D, label="Distance")
plt.plot(T, r0*np.ones_like(T), label="Target")
plt.ylim((0, 10))
plt.grid()
plt.ylabel("Distance from wall")
plt.xlabel("Time")
plt.legend()

plt.show()
