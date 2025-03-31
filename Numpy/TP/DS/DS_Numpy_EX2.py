import numpy as np
import numpy.linalg as npla
import matplotlib.pyplot as plt
import matplotlib.colors as mcol
import matplotlib.ticker as mtick
from matplotlib import cm
import matplotlib.patches as patches

#Exercice 2

#Préliminaires

X = np.linspace(-2.6, 0.6, 100)
Y = np.linspace(-1.2, 1.2, 100)

Cr, Ci = np.meshgrid(X, Y)

Zr = np.zeros(Cr.shape)
Zi = np.zeros(Cr.shape)
res = np.zeros(Cr.shape)

#Algorithme
mask=[]
for k in range(0,100):
    Zr, Zi = Zr**2 + Zi**2 + Cr, 2 * Zr * Zi + Ci
    Calcul = Zr**2 + Zi**2
    mask = Calcul > 4
    Zr [mask == True] = np.nan
    Zi [mask == True] = np.nan
    res [mask == True] = k

#Affichage du résultat

plt.imshow(res, extent=[np.min(X), np.max(X), np.min(Y), np.max(Y)], cmap="turbo")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Tracé")
plt.show()






