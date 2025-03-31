import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcol
import matplotlib.ticker as mtick
from matplotlib import cm

def somme_cos_sin(X, Y):
    return np.cos(X) + np.sin(Y)

x = np.linspace(-np.pi , np.pi, 100)
y = np.linspace(- np.pi / 2 , 3 / 2 * np.pi, 100)

XX, YY = np.meshgrid(x, y)
cos_sin = somme_cos_sin(XX, YY)
plt.imshow(cos_sin, extent=[np.min(x), np.max(x), np.min(y), np.max(y)])
plt.colorbar(label="valeur de z")
contours = plt.contour(XX, YY, cos_sin, colors="black")
plt.clabel(contours)
plt.xlabel("x")
plt.ylabel("y")
plt.title("z = cos(x) + sin(y)")