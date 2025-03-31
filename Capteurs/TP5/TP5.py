import numpy as np
import matplotlib.pyplot as plt

F = np.arange(0,200,5)

K=2.08
R=10

v = 0.3
S=10 ** -8
E=1.6* 10 **11
DR=(K*R*F)/(S*E)
Ia=10 ** -3

Vmes = ((R * DR) / (4*R + DR)) * Ia


plt.figure()
pente, oo = np.polyfit(F,Vmes,1)
plt.plot (F,Vmes, 'r')
plt.plot (F,pente*F+oo, 'b')
plt.title ("Vmes en fonction de F")
plt.xlabel ("F")
plt.ylabel ("Vmes")
plt.show()

# Q9 : Erreur de linéarité
# """

print(pente*F+oo)
print(Vmes)
erreur_lin = np.max(pente*F+oo - Vmes)
print(erreur_lin)




