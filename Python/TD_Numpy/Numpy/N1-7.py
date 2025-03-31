import numpy as np
from numpy import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches

cons = [1.03, 1.01, 1.03, 1.05, 1.03, 1.21, 1.25, 1.22, 1.24, 1.24, 1.68, 1.66, 1.69, 1.69, 1.62, 2.19, 2.3, 2.2, 2.36, 2.12, 3.14, 3.13, 2.94, 3.25, 3.19, 3.86, 3.95, 4.09, 4.11, 4.28, 5.01, 5.01, 4.95, 5.01, 5.17, 6.91, 6.99, 6.31, 6.14, 6.17, 8.71, 8.5, 8.96, 7.75, 8.18, 10.79, 9.68, 9.93, 10.39, 10.44, 11.04, 11.49, 11.38, 11.44, 12.0, 13.41, 15.08, 13.69, 14.04, 15.07, 15.51, 15.43, 15.58, 15.54, 17.46]
vit = np.arange(5,130,10)

#print(vit)

cons = np.reshape(cons,(int(len(cons)/5),5))
cons_moy = np.mean(cons, axis=1)

plt.plot(vit, cons_moy, 'ro', label='Oh wow')

coef = np.polyfit(vit, cons_moy, 2)
equa = (coef[0]*vit**2+coef[1]*vit+coef[2])
plt.plot(vit, equa, 'b', label='Oh me, oh my')

plt.grid()
plt.title("Awesome Graph you exist pt.2")
plt.axis((0,130,0,17))
plt.legend()
plt.show()