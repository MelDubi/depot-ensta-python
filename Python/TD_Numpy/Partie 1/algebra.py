import numpy as np
import numpy.linalg as npla

A = np.array([8, 2, 1, 1, 5,
              1, 9, 1, 3, 2,
              3, 5, 42, 28, 5,
              1, 9, 1, -50, 12,
              6, 5, 3, 12, -38]
             ).reshape((5, 5))

print("Le rang de A est:", npla.matrix_rank(A))
eigvals, eigvects = npla.eig(A)
inv_eigvects = npla.inv(eigvects)
print(np.allclose(A, eigvects @ np.diag(eigvals) @ inv_eigvects))
# La limite ici est qu'on fait des calculs sur des valeurs approchées (calcul numérique)
# par opposition au calcul formel qu'on fait sur une feuille ou avec des logiciels spécialisés

B = np.array([42, 12, 28, 90, 32])
X = np.linalg.solve(A, B)
print(X)


erreur_absolue = np.abs(A@X - B)
erreur_relative = erreur_absolue / B
print("Vecteur d'erreur absolue", erreur_absolue)
print("Vecteur d'erreur relative", erreur_relative)
# En général on s'intéresse au max
print("Maximum d'erreur absolue", np.max(erreur_absolue))
print("Maximum d'erreur relative", np.max(erreur_relative))
