# Quelques exemples

a = 6
if a > 2 and a < 8:
    print("Bonjour")

a = -42
if a > 2:
    if a < 8:
        print("bonjour")
    else:
        print("A est trop grand")
else:
    print("A est trop petit")


# elements = range(debut, fin, pas) # l'ensemble [debut, fin[ par pas de "pas"
# elements = range(2, 6) # l'ensemble [2, 6[
# elements = range(8) # l'ensemble [0, 8[
elements = range(3, 23, 4) # l'ensemble [3, 23[ par pas de 4
for x in elements:
    print(x)

chaine = "Bonjour le monde"
print(chaine[5:12]) # affiche les caractres de l'indice 5 compris à l'indice 12 non compris

for lettre in chaine:
    print(lettre)


# chaine_utilisateur = input("Entrez des lettres")
#
# for lettre_entree in chaine_utilisateur:
#     if lettre_entree == "e":
#         print("Lettre interdite")
#         break # interromp la boucle si on a la lettre "e"
#     elif lettre_entree == "z":
#         print("Je ne veux pas trater cette lettre")
#         continue
#     else:
#         print(lettre_entree)
#
# print("Fin boucle")


a = 5134887
a_en_chaine = str(a)
print(a, a_en_chaine)
print(a_en_chaine[3])
print(len(a_en_chaine)) # nombre de chiffres qui composent a

b_en_chaine = "44378979"
b = int(b_en_chaine)
c = b / 10

a = 3
while a < 42:
    a = a * 2
print(a)

# Exercice 1 (à décommenter)
# entier_utilisateur = int(input("Entrez un entier"))
# if entier_utilisateur % 2: # sous entendu entier_utilisateur % 2 != 0
#     print("L'entier est impair")
# else:
#     print("L'entier est pair")

# Exercice 2
# on va considérer qu'on cherche combien de fois le nombre tapé par l'utilisateur peut être divisé par 2
# avant de tomber sur un nombre impair

# tant que reste de la division entière de "le_nombre" par 2 vaut 0:
#   diviser le_nombre par 2 avec une division entière

entier_utilisateur = 42
entier_utilisateur_sauvegarde = entier_utilisateur # pour l'affichage
compteur_de_divisions = 0
while entier_utilisateur % 2 == 0:
    entier_utilisateur = entier_utilisateur // 2
    compteur_de_divisions += 1 # permet d'écrire plus vite compteur_de_divisions = compteur_de_divisions + 1

print(entier_utilisateur_sauvegarde, "est divisible", compteur_de_divisions, "fois par 2")

# Exercice 3
nb_mul = 1
table_7 = 1
while nb_mul <= 20:
    table_7 = nb_mul * 7
    nb_mul += 1
    print(table_7, end=" ")
    if table_7 % 3 == 0:
        print("*", end=" ")
print("") # pour mettre un retour à la ligne après

# Exercice 4
fact_max = 1000
facto = 1
while fact_max > 1:
    facto *= fact_max
    fact_max -= 1

print(facto)
# Pas très élégant
facto_en_chaine = str(facto)
print("Le nombre de chiffres de factorielle 1000 est", len(facto_en_chaine))

nb_chiffres_facto = 0
while facto != 0:
    facto //= 10
    nb_chiffres_facto += 1

print("Le nombre de chiffres de factorielle 1000 est", nb_chiffres_facto)



# Exercice 5
x = 0
y = 1

n = 1
n_max = 11 # le terme qu'on cherche
while n < n_max:
    z = x + y
    x = y
    y = z
    n += 1 # on n'oublie pas d'incrémenter le compteur de boucle

print("La suite vaut", y, "au bout de", n, "iterations")

# Exercice 6
n_max = 100000
sn = 0
i = 0
while i < n_max:
    ui = 8 * (-1) ** i / ((2 * i + 1) * (2 * i + 3))
    sn += ui
    i += 1

print("Au bout de", n_max, "itérations, la valeur approchée de pi calculée est de:", (sn + 4) / 2)