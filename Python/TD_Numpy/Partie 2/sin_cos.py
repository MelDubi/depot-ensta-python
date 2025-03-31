import numpy as np
import matplotlib.pyplot as plt

#X = np.linspace(0, 10, 100) # 100 points entre 0 et 10
X = np.arange(0, 4 * np.pi, 1e-4)
plt.plot(X, np.sin(X), label="sinus")
plt.plot(X, np.cos(X), label="cosinus")
plt.legend()

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Représentation graphique de sin(x)")
plt.show()