import numpy as np
from numpy import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches

B = np.linspace(0, 5, 10000)
D0 = 1/(sqrt((1-B**2)**2))
D1 = 1/(sqrt((1-B**2)**2+4*0.1**2*B**2))
D2 = 1/(sqrt((1-B**2)**2+4*0.2**2*B**2))

plt.axis((0,2.5,0,10))

plt.plot(B, D0, 'r', label='test\n0')
plt.plot(B, D1, 'g', label='0.1')
plt.plot(B, D2, 'b', label='0.2')
plt.title("Awesome Graph you exist")
plt.text(2, 5, 'My Little POOOONYYYYYYY')
plt.text(2, 4, 'My Little POOOONYYYYYYY')
plt.text(2, 3, 'aaaHAAAHAAAA HAAAAAAA!!!!!')

ax = plt.gca()
p1 = patches.FancyArrowPatch((2, 2), (4, 2.5), arrowstyle='<->', mutation_scale=20)
ax.add_patch(p1)

plt.legend()
plt.show()