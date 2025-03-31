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

#2.5 Effectif de chaque modalité
nb_setosa = species.tolist().count('Iris-setosa')
nb_versicolor = species.tolist().count('Iris-versicolor')
nb_virginica = species.tolist().count('Iris-virginica')

print("Les effectif d'Iris-setosa sont de: ", nb_setosa)
print("Les effectif d'Iris-versicolor sont de", nb_versicolor)
print("Les effectif d'Iris-virginica sont de", nb_virginica)

#2.6

# Représentation en secteurs
labels = ['Iris-setosa','Iris-versicolor','Iris-virginica']
sizes = [nb_setosa, nb_versicolor, nb_virginica]
plt.pie(sizes)
plt.legend(labels)
plt.title("Représentation en secteurs de la population d'Iris")
plt.show()

# Histogramme
plt.hist(species)
plt.title("Représentation en histogramme de la population d'iris")
plt.show()

#Première approche graphique
#2.7
#Histogramme des fréquences
#Nombre d’intervalles de l’histogramme de 50
plt.hist(petallength, bins=50, edgecolor='black')
plt.title("Histogramme en fréquences de la variable petalLength")
plt.show()

#Nombre d’intervalles de l’histogramme de 100
plt.hist(petallength, bins=100, edgecolor='black')
plt.title("Histogramme en fréquences de la variable petalLength")
plt.show()

#Histogramme cumulé des fréquences
#Nombre d’intervalles de l’histogramme de 50
plt.hist(petallength, bins=50, cumulative=True, edgecolor='black')
plt.title("Histogramme en fréquences cumulées de la variable petalLength")
plt.show()

#Nombre d’intervalles de l’histogramme de 100
plt.hist(petallength, bins=100, cumulative=True, edgecolor='black')
plt.title("Histogramme en fréquences cumulées de la variable petalLength")
plt.show()

#2.9
#Boite à moustache
plt.boxplot(petallength)
plt.title("boite à moustaches des longueurs d'iris")
plt.show()

#2.10
#Deuxième approche : résumés numériques
#Médiane
mediane = np.median(petallength)
#Moyenne
moy = petallength.mean()
#Ecart_type
ecart_type = np.std(petallength)
#Variance
var = np.var(petallength)
#1er Quartil
quartil1 = np.percentile(petallength, 25)
#3eme quartil
quartil3 = np.percentile(petallength, 75)


print("Médiane :", mediane)
print("Moyenne :", moy)
print("Ecart type :", ecart_type)
print("Variance :", var)
print("1er quartil :", quartil1)
print("3eme quartil:", quartil3)





