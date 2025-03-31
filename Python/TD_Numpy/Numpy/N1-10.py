import numpy as np
from numpy import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import time
import collections

coquilles = np.load("coquilles.npy")
t = arange(196)
n = arange(13400)
longitude = coquilles[42*196+t,(2)]
latitude = coquilles[42*196+t,(3)]
#plt.plot(longitude,latitude)
#plt.show()

mask=(coquilles[59+n*196,(4)]==5)
liste=column_stack([n,mask])
#print(list(liste))

ptDepart = coquilles[n*196,2:4]
#plt.plot(ptDepart[:,(0)],ptDepart[:,(1)])
#plt.show()

coquilles_fragmented = np.take(coquilles, [4], 1)
coquilles_fragmented = np.reshape(coquilles_fragmented, (13400, 196))
it = np.count_nonzero(coquilles_fragmented == 1, axis=1)

coquilles_sorted = np.sort(it)
print(coquilles_sorted)