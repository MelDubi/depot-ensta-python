# quelques exemples
pression1 = 10
pression2 = 20
pression3 = 30

pression = [10, 20, 30, 40, 50]
intensite = [0.123, 0.345] # etc

print(pression[2])
pression.append(42)
pression[2] = 55 # on remplace l'élement à l'indice 2 par 55

# attention l'indice visé doit exister
# pression[345] = 28

# ON N'ECRIT PAS
# pression = pression.append(42)

pression_supp = [3, 4, 56]
pression.extend(pression_supp)

# attention ce n'est équivalent à:
# pression.append(pression_supp)

pression.append("pouet")
pression.append(42.12)
del pression[-1] # enlève 42.12
del pression[-1] # enlève "pouet

# trie la liste pression en place
pression.sort()
print("Les pressions triées", pression)
# trie la liste pression dans une nouvelle variable sans toucher à pression
# pression_triee = sorted(pression)

# slicing
# exemple on cherche à extraire 10, 20, 30, 40
# leurs indices respectifs sont 2, 3, 4, 5
# on utilise la syntaxe [debut:fin:pas] pour aller chercher les éléments aux indices
# compris dans l'ensemble [debut, fin[ avec un pas de pas.

pression_court = pression[2:6] # pas besoin de préciser le pas, par défaut c'est 1
pression_court_inv = pression[5:1:-1] # idem pression[2:6] mais à l'envers
pression_a_l_envers = pression[::-1] # de la fin au début par pas de -1 (identique reverse)


mes_entiers_range = range(4,9,2)
mes_entiers_liste = list(range(4,9,2)) # attention souvent ce n'est pas utile de transformer en liste

# par exemple ces deux codes font la même chose, inutile de passer par "mes_entiers_liste"
for i in range(len(mes_entiers_range)):
    print("range", i, mes_entiers_range[i])

for i in range(len(mes_entiers_liste)):
    print("liste", i, mes_entiers_liste[i])

# on repart sur pression
# comment parcourir pression ?

for i in range(len(pression)): #déjà vu ci-dessus parcours pas indice
    print(i, pression[i])

for p in pression: # parcours par éléments
    print(p)

pression_long = pression + mes_entiers_liste # concaténation, mettre bout à bout
pression_tres_long = pression * 3 # répète trois fois la liste pression et met le resultat dans pression_tres_long

# ceci ne marche pas
# pression_marche_pas = pression + 4

# ceci peut marcher
pression_peut_marcher = pression + [4]


# exemples sur les dicos

# eleves = {} # dictionnaire vide
eleves = {"Alexandre Rama": [8, 3, 2000, "Groupe A"], "Arthur Maupas": [6, 5, 2000, "Groupe C"]}

# on peut rajouter des éléments au fur et à mesure
eleves["Aurélien Palmier"] = [17, 12, 2000, "Groupe B"]

# on peut aussi faire n'importe quoi
# eleves[42] = "pouet"

# si je veux les infos de Arthur Maupas
print(eleves["Arthur Maupas"])
jj, mm, aa, grp = eleves["Arthur Maupas"]
infos_maupas = eleves["Arthur Maupas"]

cles_du_dico = eleves.keys()
print(cles_du_dico) # eventuellement le transformer en liste si besoin

valeurs_du_dico = eleves.values()
print(valeurs_du_dico)

if "Blandine Chavane" in eleves:
    print("Elle est là")
else:
    print("Il faut l'ajouter")

eleves["Blandine Chavane"] = [30, 6, 1999, "Groupe A"]

if "Blandine Chavane" in eleves:
    print("Elle est là")
else:
    print("Il faut l'ajouter")

# in marche aussi avec les listes
# if 40 in pression:
#     print("40 est là")

# exercice 1
L = [45, 32, 78, 9, 3, 2, 10, 76, -35]
max_L = L[0] # on n'a rien de plus intelligent comme choix de départ
for i in range(1, len(L)): # on a déjà fait pour i = 0 sur la ligne au dessus
    if L[i] > max_L:
        max_L = L[i]

print(max_L)
# attention ne pas écrire vous même une fonction qui calcule le max, ça existe déjà !! Idem pour min
max_L_bis = max(L)
print(max_L_bis)

# exercice 2
pairs = []
impairs = []

for nb in L:
    if nb % 2: # equivalent if nb % 2 == 1
        impairs.append(nb)
    else:
        pairs.append(nb)

# for idx in range(len(L)):
#     if L[idx] % 2: # equivalent if nb % 2 == 1
#         impairs.append(L[idx])
#     else:
#         pairs.append(L[idx])

print("pairs de L", pairs)
print("impairs de L", impairs)

notes = []
while True:
    note = float(input("Entrez une note: "))
    if note < 0:
        break
    notes.append(note)
    print(len(notes), min(notes), max(notes), sum(notes)/len(notes))

# Exercice 4
t1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
t2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

for i in range(len(t1)):
    t2.insert(2 * i + 1, t1[i]) # au fur et à mesure t2 grandit

print(t2)

# Exercice 5
mots=["lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit"]

lettre_choisie = input("Entrez une lettre:").lower()
mots_trouves = []
occurences_totales = 0
longueur_totale = 0
for mot in mots:
    nb_occurrences = 0
    for lettre in mot:
        if lettre == lettre_choisie:
            nb_occurrences += 1
    # quand on est plus à l'aise avec le langage on peut directement écrire
    # nb_occurrences = mot.count(lettre_choisie)
    if nb_occurrences > 0:
        occurences_totales += nb_occurrences
        longueur_totale += len(mot)
        mots_trouves.append(mot)

print("Fréquence:", occurences_totales / longueur_totale)
print("Mots trouvés", mots_trouves)
print("Nombre de mots", len(mots_trouves))


# Exercice 6
liste_premiers = [True] * 1000 # de 0 à 999

# 0 et 1 ne sont pas premiers
liste_premiers[0] = 0
liste_premiers[1] = 0

# On peut fortement optimiser ce code mais ce n'est pas le but ici.
# Voir https://fr.wikipedia.org/wiki/Crible_d%27%C3%89ratosth%C3%A8ne
for i in range(2, len(liste_premiers)):
    if liste_premiers[i]:
        for j in range(2 * i, len(liste_premiers), i):
            liste_premiers[j] = False

for i in range(len(liste_premiers)):
    if liste_premiers[i]:
        print(i)


