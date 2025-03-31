import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy
from scipy.stats import chi2


# 1 Bien doser l’alliage

# Question 1.1: Identifier la nature des deux variables aléatoires de ce problème.

# Résistance à la traction
# Pourcentage carbone présent

# Question 1.2: Calculer les moyennes et les variances de chaque sous-population définie par la proportion de carbone.
# Représenter les boites à moustaches sur une même figure. Commenter qualitativement la figure résultante quant à
# l’influence de la proportion de carbone sur la résistance à la traction.

# Moyenne

# Acier 0.1% carbone
tab1 = [23.05, 36, 31.1, 32.65, 30.9, 31.4, 30.85]

# Acier 0.2% carbone
tab2 = [41.85, 25.65, 46.7, 34.5, 36.65, 31.45, 36.13]

# Acier 0.4% carbone
tab4 = [47.05, 43.45, 43, 38.65, 41.85, 35.45, 41.57]

# Acier 0.6% carbone
tab6 = [49.65, 73.9, 66.45, 74.55, 62.4, 63.75, 65.11]

# Moyenne

Moy1 = np.mean(tab1)
print("Moyenne 0.1% : ", Moy1)
Moy2 = np.mean(tab2)
print("Moyenne 0.2% : ", Moy2)
Moy4 = np.mean(tab4)
print("Moyenne 0.4% : ", Moy4)
Moy6 = np.mean(tab6)
print("Moyenne 0.6% : ", Moy6)

# Variance
Var1 = np.var(tab1)
print("Variance 0.1% : ", Var1)
Var2 = np.var(tab2)
print("Variance 0.2% : ", Var2)
Var4 = np.var(tab4)
print("Variance 0.4% : ", Var4)
Var6 = np.var(tab6)
print("Variance 0.6% : ", Var6)

# Test Fisher :  comparaison des variances des sous-population avec la variance de la population globale

# Moyenne globale

Moy_globale = (sum(tab1)+sum(tab2)+sum(tab4)+sum(tab6))/28
print("La moyenne globale de la population est : ", Moy_globale)

# Dispersion/Variance intraclasse totale
Disp_intra_globale = (7*(Var1+Var2+Var4+Var6))/28
print("La dispersion intraclasse globale est :", Disp_intra_globale)


# Dispersion/variance interclasse
Disp_inter_globale = (7*(Moy1-Moy_globale)**2+7*(Moy2-Moy_globale)**2+7*(Moy4-Moy_globale)**2+7*(Moy6-Moy_globale)**2)/28
print("La dispersion interclasse globale est :", Disp_inter_globale)

# Question 1.3: Mener ce test en adoptant la procédure générale des tests. Répondre à la question: la
# proportion de carbone a-t-elle une influence sur la résistance à la traction ? On utilisera

# Grandeur d'intérêt : indépendance

# H0 : Les moyennes des 4 sous populations sont égales, donc la proportion de carbone n'influe pas sur la résistance
# de traction

# H1 : Les moyennes des 4 sous populations ne sont pas égales, donc la proportion de carbone n'influe pas sur la
# résistance de traction

# Test statistique

# Calcul de F0 doit suivre une loi de Fisher de paramètres p-1 N-p
p = 4
F0 = (Disp_inter_globale/(p-1))/(Disp_intra_globale/(28-4))
print(F0)

# Test du rejet de H0
N = 28
a = 0.05
Fa = scipy.stats.f.ppf(a, p-1, N-p)
print (Fa)

# Région critique si f0 > fα,(p−1),(N −p) = F −1 (1 − α) . F0
if F0 > Fa:
    print("Rejet de l'Hypothèse 0 dans la région critique")
else:
    print("Pas de rejet de l'Hypothèse 0 dans la région critique")

# # Critère de rejet pour p-valeur : p-valeur = P(F0 >f0)=1−P(F0 ≥f0)≤0.05
# print("La valeur de p-valeur est de", p_value)
#
# # Si p-valeur < 0.05 -> rejet de H0
# if p_value < 0.05:
#     print("Rejet de l'Hypothèse 0 pour p-valeur")
# else:
#     print("Pas de rejet de l'Hypothèse 0 pour p-valeur")






