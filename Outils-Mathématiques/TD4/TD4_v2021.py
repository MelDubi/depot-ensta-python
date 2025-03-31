import math as m

# exercice 1
def ajoute_1(x):
    return 1 + x

print(ajoute_1(2))
print(ajoute_1(3))

res = ajoute_1(42)
print(res)

# exercice 2
def puissances(x):
    # évidemment on utilisera un for en
    return x**1, x**2, x**3, x**4

# puissances renvoie 4 variables, la variable puissances_de_3 ci-dessous recevra donc un tuple de 4 éléments
puissances_de_3 = puissances(3)
trois_cube = puissances_de_3[2]
print(puissances_de_3, trois_cube)

# exercice 3
def nb_pattes(p, v, c):
    return 2 * (p + c) + 4 * v

pattes = nb_pattes(2, 3, 4)
# on s'attend à en avoir 24
print("2 poulets, 3 vaches et 4 canards ont un nombre de pattes égal à:", pattes)

# exercice 4
def somme_carres(n):
    res = 0
    for i in range(n+1): # on dit bien "n inclus" dans l'énoncé
        res += i ** 2
    return res

def somme_carres_malin(n):
    # on peut utiliser la division entière ici, le résultat étant par définition un entier
    return n * (n + 1) * (2 * n + 1) // 6

# dans somme_carres on fait n + 1 multiplications (i * i) et n + 1 additions
# dans somme_carres_malin on fait, quelle que soit la valeur de n, 2 additions, 3 multiplications et une division
# => dans somme_carres on fait 2 * (n + 1) opérations, dans somme_carres_malin on en fait 6, indépendamment de n
# il est donc extrèmement maladroit d'utiliser somme_carres dès que n = 2 (et elle ne sert à rien pour n < 2)

somme_carres_42 = somme_carres(42)
print(somme_carres_42, somme_carres_malin(42))

# exercice 5
def somme_carres_liste_v1(n):
    res = 0
    liste_res = []
    for i in range(n+1): # on dit bien "n inclus" dans l'énoncé
        res += i ** 2
        liste_res.append(res)
    return liste_res


def somme_carres_liste_v2(n):
    # la variable intermédiare res n'a aucun intérêt
    liste_res = [0]
    for i in range(1, n+1): # on dit bien "n inclus" dans l'énoncé
        liste_res.append(liste_res[-1] + i**2)
    return liste_res


# ici on doit calculer explicitement la somme de tous les carrés de 0 à n inclus pour pouvoir stocker
# les résultats intermédiaires. Le nombre de calculs nécessaires avec la boucle for n'a pas changé
# depuis l'exercice précédent, soit 2 * (n + 1) (ou 2 * n suivant la version)
# Quoi qu'on fasse on a besoin de tous les résultats intermédiaires. Si on souhaite exploiter le résultat
# sur la somme des carrés on écrira un code qui ressemble à la fonction ci_dessous

def somme_carres_liste_moins_malin(n):
    liste_res = [0]
    for i in range(1, n+1): # on dit bien "n inclus" dans l'énoncé
        liste_res.append(i * (i + 1) * (2 * i + 1) // 6)
    return liste_res

# dans cette fonction on fait 6 opérations à chaque tour de la boucle for qui fait n itérations
# soit 6 * n opérations, ce qui sera trois fois plus long que la version précédente indépendamment
# de la valeur de n

print(somme_carres_liste_v1(10), somme_carres_liste_v2(10), somme_carres_liste_moins_malin(10))

def suite_mystere(n):
    S = 0
    for i in range(1, n + 1):
        S += 1 / (i ** 2)
    return m.sqrt(6 * S)

# On conjecture que la limite de cette suite est pi.
print(suite_mystere((10)))
print(suite_mystere((100)))

# Attention ceci n'est pas une preuve:
for n_max in range(0, 10000, 100):
    print("Pour n=%d l'écart entre Pi et la suite Un est %lf"%(n_max, abs(m.pi - suite_mystere(n_max))))