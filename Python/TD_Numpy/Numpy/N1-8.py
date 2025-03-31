import numpy as np
from numpy import *
import matplotlib.pyplot as plt

#plt.axis((-pi,pi,-pi/2,3*pi/2))

x = np.arange(-pi, pi, 0.1)
y = np.arange(-pi/2, 3*pi/2, 0.1)
xx, yy = np.meshgrid(x, y, sparse=True)
z = np.cos(xx) + np.sin(yy)
im = plt.imshow(z,extent=[-pi,pi,-pi/2,3*pi/2])

plt.colorbar(label = 'color color color color color')
plt.contour(z,levels=[-1.5,-1,-0.5,0,0.5,1,1.5],colors=['black'],extent=[-pi,pi,-pi/2,3*pi/2])

plt.title("Awesome Graph you exist")
plt.xlabel('x')
plt.ylabel('y')
plt.show()