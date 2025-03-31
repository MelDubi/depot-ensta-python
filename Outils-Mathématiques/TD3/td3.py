def max_liste(liste):
    maxl = liste[0]
    for i in range(len(liste)):
        if liste[i] > maxl:
            maxl = liste[i]
    return maxl
    # return max(liste)


def tri_liste(liste):
    impair = []
    pair = []
    for i in range(len(liste)):
        if liste[i] % 2:
            impair.append(liste[i])
        else:
            pair.append(liste[i])
    pair.sort()
    impair.sort()
    return pair, impair


def moy_list(liste):
    return sum(liste) / len(liste)


def exo1():
    l1 = [1, 2, 3, 5, 3, 46, 4, 55, 0, -67]
    print(max_liste(l1))


def exo2():
    l1 = [1, 2, 3, 5, 3, 46, 4, 55, 0, -67]
    print(tri_liste(l1))


def exo3():
    notes = []
    note = float(input("Veuillez entrer une note : \n"))
    while note >= 0:
        notes.append(note)
        print("Nombre de notes entrées: ", len(notes))
        print("note maximale: ", max_liste(notes))
        print("note la plus basse: ", min(notes))
        print("Moyenne: ", moy_list(notes))
        note = float(input("Veuillez entrer une note : \n"))
    print("FIN\n\n")


def exo4():
    t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet',
          'Aout', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
    j = 0
    for i in range(len(t2)):
        t1.insert(j, t2[i])
        j += 2
    print(t1)


def exo5():
    liste = ['janvier', 'fevrier', 'mars', 'avril', 'mai', 'juin', 'juillet',
             'aout', 'septembre', 'octobre', 'novembre', 'decembre']
    lettre = input("entrez une lettre: \n").lower()
    cmp = 0
    cmp_total = 0
    liste_mots = []
    for i in range(len(liste)):
        entre = False
        for j in range(len(liste[i])):
            cmp_total += 1
            if liste[i][j] == lettre:
                cmp += 1
                if not entre:
                    liste_mots.append(liste[i])
                    entre = True

    print("La lettre ", lettre, " est utilisée ", cmp, " fois")
    print("Cette lettre apparait dans les mots suivants : ", liste_mots)
    print("La fréquence d'apparation de cette lettre est de :", cmp / cmp_total)


def exo6():
    liste = [1] * 1000
    print(liste)
    for i in range(2, len(liste)):
        if liste[i] == 1:
            for j in range(i + 1, len(liste)):
                if j % i == 0:
                    liste[j] = 0
    s = ""
    for k in range(len(liste)):
        if liste[k] == 1:
            s += str(k)
            s += ", "
    print("Liste des nombres premiers:\n", s)


def completer(dico):
    continuer = 'Y'
    while continuer == 'Y':
        nom = input("Nom ?\n")
        taille = float(input("Taille ?(en mètres)\n"))
        age = int(input("Age ?(en années)\n"))
        dico[nom] = (age, taille)
        continuer = input("ce copain a été entré dans la base de donnée, \n"
                          "voulez vouys encore enrichier celle-ci ? (Y/N)\n").upper()


def consulter(dico):
    nom = input("saisissez un nom\n")
    print(dico[nom])


def exo7():
    dico = {}
    cmd = int(input("Voulez vous :\n1:compléter\n2:consulter\n0:Quitter\n"))
    while cmd != 0:
        if cmd == 2:
            consulter(dico)
        if cmd == 1:
            completer(dico)
        if cmd == 0:
            break
        cmd = int(input("Voulez vous :\n1:compléter\n2:consulter\n0:Quitter\n"))
    print(dico)


exo7()
