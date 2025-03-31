import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats

#2 Fitness
# Grandeur d'intérêt : proportion

# Hypothèse 0 : p = p0 = 0.2

# Hypothèse alternative : p < p0

# Test statistique

# Nombre d'individus
n = 100
# Probabilité 0
p_zero = 0.2
# Proportion d'individus âgé de plus de 40 ans et faisant du sport au moins 2 fois par semaine
Proportion = 15/100
# Calcul de Z0
Z0 = (Proportion-p_zero)/(np.sqrt((p_zero*(1-p_zero))/n))
print("La valeur de Z0 est de", Z0)

# Niveau de confiance à 95%
a = 0.05
Z_alpha = scipy.stats.norm.ppf(1-a) # ppf pour erf-1(Z0)

# Région critique si Z0 < -Z_alpha -> rejet de H0
if Z0 < -Z_alpha:
    print("Rejet de l'Hypothèse 0 dans la région critique")
else:
    print("Pas de rejet de l'Hypothèse 0 dans la région critique")

p_value = scipy.stats.norm.cdf(Z0) # cdf pour erf(Z0)
print("La valeur de p-valeur est de", p_value)

# Si p-valeur < 0.05 -> rejet de H0
if p_value < 0.05:
    print("Rejet de l'Hypothèse 0 pour p-valeur")
else:
    print("Pas de rejet de l'Hypothèse 0 pour p-valeur")



#3 Météo

T16 = [39, 39, 40, 33, 36, 40, 37, 41, 39, 34, 42, 41, 42, 44, 42, 42, 39, 42, 41, 40, 43, 43, 40, 39, 37]

# Hypothèse 0 : T16 = Tmoy
# Hypothèse alternative 1 : T16 < Tmoy ou T16 > Tmoy
# H3 ?

# Moyenne temperature
moyTemp = 37.5
# Moyenne température calculée
moyT16 = np.mean(T16)
# Variance
variance = np.var(T16, ddof=1)
# Ecart-Type
ecart_type = np.sqrt(variance)
# Nombre d'individus
nTemp = len(T16)

# Moyenne d'une distribution normale, variance inconnue -> Critère de rejet : T0 > tn-1,a/2 ou T0 < -tn_1,a/2

# Calcul de T0
T0 = moyT16-moyTemp/(ecart_type/nTemp)
print("La valeur de T0 est de", T0)

# Calcul de tn-1,a/2 avec l'aide du tableau de la fonction de répartition de la loi de student : Fstudent_1,n-1,a/2
tn_1 = scipy.stats.t.ppf(1-a/2, df=nTemp)
print("La valeur de tn_1 est de", tn_1)



if T0 < -tn_1:
    print("Rejet de l'hypothèse 0 dans la zone critique")
else:
    print("Pas de rejet de l'hypothèse 0 dans la zone critique")

# Critère de rejet pour p-valeur : 2-2FT0{|T0|} < 0.05
p_value = 2-2*scipy.stats.t.cdf(np.abs(T0), df=nTemp)
print("La valeur de p-valeur est de", p_value)

if p_value < 0.05:
    print("Rejet de l'hyptohèse 0 avec p-valeur")
else:
    print("Pas de rejet de l'hyptohèse 0 avec p-valeur")


#4 Potency of an Antibiotic

# Nombre d'individus
n = 100
# Moyenne de puissance
moyPuis = 0.8
# Moyenne échantillon
moyEchantillon = 0.797
# Ecart-type
Sn_1 = 0.008

# Grandeur d'intérêt : moyenne

# Hypothèse 0 : moyEchantillon = moyPuis

# Hypothèse alternative : moyEchantillon < moyPuis

# Test statistique

# Moyenne, grand échantillon, variance connue -> slide 188
# Calcul de Z0
Z0 = (moyEchantillon-moyPuis)/(Sn_1/np.sqrt(n))
print("La valeur de Z0 est de", Z0)

# Niveau de confiance à 95%
a = 0.05
Z_alpha = scipy.stats.norm.ppf(1-a) # ppf pour erf-1(x)

# Région critique si Z0 < -Z_alpha -> rejet de H0
if Z0 < -Z_alpha:
    print("Rejet de l'Hypothèse 0 dans la région critique")
else:
    print("Pas de rejet de l'Hypothèse 0 dans la région critique")


# Critère de rejet pour p-valeur : erf(Z0) < 0.05
# Calcul de p-valeur = erf(Z0)
p_value = scipy.stats.norm.cdf(Z0) # cdf pour erf(Z0)
print("La valeur de p-valeur est de", p_value)

# Si p-valeur < 0.05 -> rejet de H0
if p_value < 0.05:
    print("Rejet de l'Hypothèse 0 pour p-valeur")
else:
    print("Pas de rejet de l'Hypothèse 0 pour p-valeur")


