from matplotlib.pyplot import contour
import numpy as np
import matplotlib.pyplot as plt


A = np.array([[5,2],[2,4]])
B = np.array([4,-2])
C = 2
X = np.linspace(-2,1,101)
Y = np.linspace(-1,2,151)
Z = np.zeros((X.shape[0],Y.shape[0]))


def f(x):
    return np.transpose(x) @ A @ x + np.transpose(B) @ x + C


def fp(x):
    return 2 * np.transpose(x) @ A + np.transpose(B)

def f1(x):
    return np.transpose(x) @ A @ x + np.transpose(B) @ x + C


def f1p(x):
    return 2 * np.transpose(x) @ A + np.transpose(B)

for i in range(X.shape[0]):
    for j in range(Y.shape[0]):
        point = np.array((X[i],Y[j]))
        Z[i,j] = f(point)


print(Z)

extent = [np.min(X), np.max(X), np.min(Y), np.max(Y)] #permet de donner l'étendu (l'échelle)
plt.imshow(Z, extent=extent)
plt.colorbar(label='valeur de Z')
CS=plt.contour(Z, extent=extent, colors='black')
plt.clabel(CS)
plt.show()

X=-(1/2) * np.linalg.inv(A) @ B

print(X)

Xg = np.array([-1.5,1.5])

for t in range (42):
    Xg = Xg - 0.042 * fp(Xg)

print(Xg)


