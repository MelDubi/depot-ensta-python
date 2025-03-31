import donnees
import random


def is_ascii(lettre):
    ret = True
    ret = not ord(lettre) > 122
    ret = not ord(lettre) < 97
    return ret


def recup_lettre():
    lettre = ""
    while (not len(lettre) == 1) or (not lettre.isalpha()):
        lettre = input("Veuillez entrer une lettre: \n->").lower()
    return lettre


def choisir_mot():
    return random.choice(donnees.liste_mots)


def recup_mot_masque(mot_complet, lettres_trouvees):
    masque = ""
    for i in range(len(mot_complet)):
        trouve = False
        for j in range(len(lettres_trouvees)):
#            print("mot_complet[i]: ", mot_complet[i])
#            print("lettres_trouvees[j]", lettres_trouvees[j])
            if mot_complet[i] == lettres_trouvees[j]:
                masque += lettres_trouvees[j]
                trouve = True
                break
        if not trouve:
            masque += donnees.char_masque
    return masque


def is_trouve(mot):
    for i in mot:
        if i == donnees.char_masque:
            return False
    return True


def is_lettre_deja_choisi(lettre, liste_lettre):
    for let in liste_lettre:
        if lettre == let:
            return True
    return False






# lettres =['a', 'y']
# mot = "tanguy"
# print(recup_mot_masque(mot, lettres))
