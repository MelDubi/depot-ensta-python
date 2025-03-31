import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('iris.csv', sep=',')
print(df.values)
sepallength = df["sepallength"].values
sepalwidth = df["sepalwidth"].values
petallength = df["petallength"].values
petalwidth = df["petalwidth"].values
species = df["class"].values
speciesname = np.unique(species)
variablename = df.keys().values[0:-1]

print(petallength)

#2.1 Nuage de points

plt.scatter(petalwidth,petallength)
plt.xlabel("Largeur de pétale")
plt.ylabel("Longueur de pétale")
plt.title("Nuage de points de la longueur du pétale en fonction de la largeur du pétale pour 150 Iris")


#2.2 Coefficient de corrélation

corrcoeff = np.corrcoef(petallength, petalwidth)
print("La matrice du coefficient de corrélation est de : ", corrcoeff)


#2.3
#Equation y = â x + b

# Calcul de â
# â = corrcoeff * Sn-1,Y/Sn-1,X

#Ecart-type
#Sn-1,Y
ecart_type_y = np.std(petallength)
#Sn-1,X
ecart_type_x = np.std(petalwidth)

a = corrcoeff[0,1] * ecart_type_y / ecart_type_x
print(a)
# Calcul de b
# b = moy_Y - corrcoeff * Sn-1,Y/Sn-1,X * moy_X

#Moyenne
#Y
moy_Y = petallength.mean()
#X
moy_X = petalwidth.mean()

b = moy_Y - corrcoeff[0,1] * ecart_type_y/ecart_type_x * moy_X

#Equation de régression linéaire
y = a * petalwidth + b

print(y)

plt.plot(petalwidth, y)
plt.xlabel("Largeur de pétale")
plt.ylabel("Longueur de pétale")
plt.title("Fonction de régression linéaire")
plt.show()

#2.5


# for specie in speciesname:
#     for fleur in species:
#         if fleur == specie :
#
#
# plt.hist()
# plt.title("Représentation en histogramme de la population d'iris")
# plt.show()


tab_Setosa = [0]*50
tab_Versicolor = [0]*50
tab_Virginica = [0]*50

for i in range (0,50):
        tab_Setosa[i] = df.values[i,2]
print("tableau Setosa",tab_Setosa)

i = 0
for j in range (50,100):
        tab_Versicolor[i] = df.values[j,2]
        i+=1
print("tableau Versicolor",tab_Versicolor)

l=0
for k in range (100,150):
        tab_Virginica[l] = df.values[k,2]
        l+=1
print("tableau Virginica",tab_Virginica)

#Histogramme longueur du pétale Iris_Setosa
plt.hist(tab_Setosa, bins=10, edgecolor='black')
plt.hist(tab_Versicolor, bins=20, edgecolor='black', alpha=0.9)
plt.hist(tab_Virginica, bins=20, edgecolor='black', alpha=0.7)
labels = ['petallenght Iris-setosa','petallenght Iris-versicolor',' petallenght Iris-virginica']
plt.legend(labels)
plt.title("Histogramme longueur du pétale des Iris")
plt.show()


#2.7
# Rapport de corrélation # A comprendre et changer

def variance_interclasse (tab,n):
    somme = 0
    Y_mean = np.mean(tab)
    for i in range(0, n):
        Y_mean_i = np.mean(tab[i * 50:(i + 1) * 50])
        somme += (50 / n) * (Y_mean_i - Y_mean) ** 2
    sol = somme / 150
    return sol

def variance_intraclasse (tab, n):
    somme = 0
    for i in range(0, n):
        Y_i = np.var(tab[i*50:(i+1)*50])
        somme += (50 / n) * Y_i
    sol = somme / 150
    return sol

def correlation(inter, intra):
    return np.sqrt(inter / (inter + intra))

Variance_inter = variance_intraclasse(petallength, 3)
Varaince_intra = variance_intraclasse(petallength, 3)
Rapport_correlation = correlation(Variance_inter, Varaince_intra)
print("Variance inter-classe :", Variance_inter)
print("Variance intra-classe :", Varaince_intra)
print("Rapport de corrélation :", Rapport_correlation)

plt.show()
