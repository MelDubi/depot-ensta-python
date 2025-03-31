import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy
from scipy.stats import chi2


# Question 0.1: Estimer la moyenne et la variance de l’échantillon. Indication: on utilisera les opéra- teurs terme
# à terme python: ** et *?

# Moyenne
from scipy.stats import stats

nbr_sat = [1,2,3,4,5,6,7,8,9]
nbr_obs = [6,15,9,25,17,10,8,7,3]

# somme des xi*ni/somme des nombres d'observations
moy = sum(nbr_sat[i]*nbr_obs[i] for i in range(0, len(nbr_sat)))/sum(nbr_obs)
print(moy)

# Variance
var = []
n = 9
variance = 0
for i in range(n):
    var.append((nbr_sat[i]-moy)**2)
    variance = (1/(n-1))*sum(var)
print(variance)

# Question 0.2: Approcher la loi sous-jacente à l’aide d’une loi de Poisson de paramètre λ = 4.47. Déter- miner les
# effectifs théoriques pour 0 à 16 satellites. Indication: on utilisera la fonction poisspdf ou poisson.pmf.

# Création d'un tableau de taille 16
tab = np.arange(0, 17)
# Calcul du tableau poisson par la fonction poisson avec en paramètre tableau de taille 16 et lambda = 4.47
tab_poisson = scipy.stats.poisson.pmf(tab, 4.47)
# Création du tableau d'effectifs théoriques
effectifs_theoriques = []

# Calcul des effectifs
effectifs = 0
for i in range(len(nbr_obs)):
    effectifs += nbr_obs[i]

for i in range(len(tab)):
    effectifs_theoriques.append(effectifs * tab_poisson[i])

print(effectifs_theoriques)

#Question 0.3: Peut-on, à un seuil de 95%, considérer que l’échantillon a été produit par cette loi de Poisson ?

chi2_obs = 0
# Hypothèse
for i in range(len(nbr_obs)):
    chi2_obs = (nbr_obs[i]-effectifs_theoriques[i])**2 / effectifs_theoriques[i]

print(chi2_obs)

chi_theor = 23.59
print(chi_theor < chi2_obs)


# Question 0.4: Peut-on conclure que les étudiants masculins et féminins ont un comportement différent lors de
# l’"initiation" ? Quel test allez vous effectuer pour le prouver ?

# Grandeur d'intérêt : homogénéité/indépendance

# Hypothèse 0 : distributions identiques entre les deux populations

# Hypothèse alternative : distributions non identiques entre les deux populations

# Test statistique

# Niveau de confiance à 95%
a = 0.05

# Région critique si X2_obs > X2alpha,(p-1)(q-1)



# X2 observé sous H0 devrait donc suivre une loi du X² à (2-1)*(5-1) = 4 degré de liberté

nij = [[3, 9, 18, 36, 29], [3, 3, 1, 14, 13]]
ni = [95, 34]
nj = [6, 12, 19, 50, 42]
n = 129

pi = []
Npij = []
X20 = 0
X2Obs = 0

# Calcul du X2_O et du X2_obs
for i in range(2):
    for j in range(5):
        X2_0_ = X20 + (((nij[i][j] - (ni[i] * nj[j] / n)) ** 2 / n) / (ni[i] * nj[j] / n))

        npij = (ni[i]*nj[j]) / n
        Npij.append(npij)

        X2_Obs = X2Obs + (((npij-nij[i][j])**2)/npij)

print("X2_0 =", X20)
print("Effectifs attendus :", Npij)
print("X2_Obs =", X2Obs)

# Calcul du X2 des tables
X2_alpha_4 = scipy.stats.chi2.ppf(1 - a, 4)
print("X2(0.05,4)=", X2_alpha_4)

# Calcul de la p_valeur du X2_O
p_valeurs_1 = 1 - scipy.stats.chi2.cdf(X20, 4)
print("p_valeurs =", p_valeurs_1, " pour X2_0")

# Calcul de la p_valeur du X2_obs
p_valeurs_2 = 1 - scipy.stats.chi2.cdf(X2Obs, 4)
print("p_valeurs =", p_valeurs_2, " pour X2_Obs")