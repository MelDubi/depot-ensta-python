# -*- coding: utf-8 -*-

import car
import numpy as np
import pylab as plt
from scipy.signal import place_poles
from scipy import signal


def car_dyn(x, u):
    x1=x[3]*np.cos(x[4])*np.cos(x[2])
    x2=x[3]*np.cos(x[4])*np.sin(x[2])
    x3=x[3]*np.sin(x[4])/L_car
    x4=u[0]
    x5=u[1]

    xdot = np.array([
           x1,
           x2,
           x3,
           x4,
           x5
           ])
    return xdot
"""Computes the derivative of the car's state vector x according to
    x and the control u"""

def observation_func(x, track):
    d = car.dist_to_track(x, track)
    return np.array([d, x[3], x[4]])


L_car = 3  # car length (don't mess it up with L from KLH control)
r0 = 15  # reference distance to track
v0 = 9  # reference speed

# linear system
# Compute A, B, C, D and E
A=np.array([[0,9,0,0],[0,0,0,3],[0,0,0,0],[0,0,0,0]])
B=np.array([[0,0],[0,0],[1,0],[0,1]])
C=np.array([[1,0,0,0],[0,0,1,0],[0,0,0,1]])
D=np.array([[0,0],[0,0],[0,0]])
E=np.array([[1,0,0,0],[0,0,1,0]])

# eigenvalues
# choose pcom and pobs
pcom=np.array([-2,-1.01,-1.02,-1.03])
pobs=np.array([-2.01,-2.02,-2.03,-2.04])

# compute KLH control
res=place_poles(A,B,pcom)
K=res.gain_matrix
print("Command_poles : ", res.computed_poles)

res=place_poles(A.T,C.T,pobs)
L=res.gain_matrix.T
print("Commande_obs : ", res.computed_poles)

H=-np.linalg.inv(E@np.linalg.inv(A-B@K)@B)

#compute a state space representation of the linear regulator
# Ar, Br, Cr, Dr
Ar=A-B@K-L@C
Br=np.bmat([B@H,L])
Cr=-K
Dr=np.bmat([H,np.zeros((B.T@C.T).shape)])

# define the evolution function of the regulator
def regul(xr, w, y):
    xrdot = Ar@xr+B@H@(w-wbar)+L@(y-ybar)
    return xrdot


# equilibrium point
#ubar =
ubar=np.array([0,0])
#xbar =
xbar=np.array([r0, 0, np.pi/2, v0, 0])
#wbar =
wbar=np.array([r0, v0])
#ybar =
ybar=np.array([r0, v0, 0])

track = np.array([
                [-10, -12, -10, 0, 10, 20, 40, 32, 35, 30,  20,  0,   -10],
                [-5,   0,  5,  50, 60, 60, 50, 15, 5,  -10, -15, -15, -5]
                ])

#Initial conditions
x = np.array([-18, 0, np.pi/2, v0, 0])  # initial state for car
#xr =  # initial state for observer
xr=np.array([0,0,0,0])
u = np.array([0,0])  # only for testing purposes
w = np.array([r0, v0])  # reference


h = 0.05  # timestep
T = np.arange(0, 40, h)
D = []  # list of distances from the car to the track at each timestep
for t in T:
    # sensors
    y = observation_func(x, track)
    D.append(y[0])
    # control
    #u =
    u=ubar-K@xr+H@(w-wbar)
    # updates for the car and the regulator
    # RK2 for regulator
    #xr =
    k1=regul(xr,w,y)
    k2=regul(xr+h*k1,w,y)
    xr=xr+h*(k1+k2)/2
    # RK2 for car
    #x =
    k1=car_dyn(x,u)
    k2=car_dyn(x+h*k1,u)
    x=x+h*(k1+k2)/2

    car.draw(x, y[0], track, size=150)

# plot the tracking error wrt time
# plot the control signals wrt time

plt.show()