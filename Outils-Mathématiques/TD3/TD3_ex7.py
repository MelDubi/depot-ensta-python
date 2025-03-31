#Exercice 7 "Base de données nom/âge/taille"

#Initialisation du dictionnaire
dico = {}

#Choix de l'utilisateur
print("Quelle action voulez-vous faire ?")

while 1:
    choix = input("Choisissez : (R)emplir - (C)onsulter - (T)erminer :")
    if choix.upper() == "T":
        print("Terminé")
        break
    # Premier bloc : remplissage du dictionnaire
    elif choix.upper() == "R":
        print("Remplissage du dictionnaire")
        while 1:
            nom = input("Entrez le nom (ou <enter> pour terminer) :")
            if nom == "":
                break
            age = int(input("Entrez l'âge (nombre entier !) :"))
            taille = float(input("Entrez la taille (en mètres) :"))
            dico[nom] = (age, taille)
    # Deuxième bloc : consultation du dictionnaire
    elif choix.upper() == "C":
        print("Consultation du dictionnaire")
        while 1:
            recherche = input("Quel nom recherchez-vous ? (<entrer> pour terminer) ")
            if recherche == "":
                break
            if recherche not in dico:
                print("Le nom n'existe pas - Nouvel essai")
            else :
                print("Nom :{} - âge :{} ans - taille :{} m.".format(recherche, dico[recherche][0], dico[recherche][1]))
