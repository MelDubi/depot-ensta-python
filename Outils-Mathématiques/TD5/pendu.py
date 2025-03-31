import fonctions

nbcoups = 8
mot_a_trouver = fonctions.choisir_mot()
lettres_trouvees = []
lettres_demandees = []
mot_masque = fonctions.recup_mot_masque(mot_a_trouver, lettres_trouvees)

while nbcoups > 0 and not fonctions.is_trouve(mot_masque):
    lettre = fonctions.recup_lettre()
    while fonctions.is_lettre_deja_choisi(lettre, lettres_demandees):
        print("Lettre déjà choisie, liste des lettres déjà demandées: \n", lettres_demandees)
        lettre = fonctions.recup_lettre()
    lettres_demandees.append(lettre)
    if mot_a_trouver.__contains__(lettre):
        print("Bien joué!")
        lettres_trouvees.append(lettre)
        mot_masque = fonctions.recup_mot_masque(mot_a_trouver, lettres_trouvees)
        print(mot_masque)
    else:
        print("raté")
        print(fonctions.recup_mot_masque(mot_masque, lettres_trouvees))
    nbcoups -= 1

if mot_masque == mot_a_trouver:
    print("gagné")
else:
    print("PENDU !!! Vous avez perdu.")
