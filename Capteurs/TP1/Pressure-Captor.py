import numpy as np
import matplotlib.pyplot as plt

# Lecture des données
nom_fich = "td1_pressure_measurements.txt"
mesures = np.loadtxt('données')
print(mesures)

# """
# Q3 : tableau représentant les pressions mesurées
# """
pressions = np.arange(0, 41, 5)
print(pressions)
#
#
# """
# Q3 : Moyenne des mesures ( avec mean de numpy )
# """
#
mesures_moy = np.mean(mesures, 0)  # moyenne des colonnes (indice 1 = moyenne des lignes)
#
# """
# Q3 : Affichage des moyennes des mesures pour chaque mesurande
# """
#
plt.figure(1)
plt.title("Mesures Moyennes")
plt.xlabel("Pression (PSI)")
plt.ylabel("Courant (mA)")
plt.plot(pressions, mesures_moy, 'c-s')
#
# """
# Q4 : Sensibilités
# utiliser les valeurs moyennes autour de la valeur pour laquelle on souhaite
# estimer la sensibilité
# """
#

S_5 = (mesures_moy[2] - mesures_moy[0]) / (pressions[2] - pressions[0])
S_20 = (mesures_moy[5] - mesures_moy[3]) / (pressions[5] - pressions[3])
S_35 = (mesures_moy[8] - mesures_moy[6]) / (pressions[8] - pressions[6])

print("sensibilité à 5 PSI : %.2f" % (S_5))
print("sensibilité à 20 PSI : %.2f" % (S_20))
print("sensibilité à 35 PSI : %.2f" % (S_35))
#
# """
# Q5 :  Caractéristiques de la réponse théorique données par le constructeur
# passant par les points terminaux
# """

pente_constructeur = 0.4
ordonnee_origine_constructeur = 4
courbe_constructeur = pente_constructeur * pressions + ordonnee_origine_constructeur

plt.figure(2)
plt.title("Courbe Théorique")
plt.xlabel("Pression (PSI)")
plt.ylabel("Courant (mA)")
plt.plot(pressions, courbe_constructeur, 'c-o', label="Courbe théorique")

plt.plot(pressions, mesures_moy, "r+", label="Moyenne des mesures")
plt.legend()
#
# """
# Q6 : Erreur de fidélité
# la fidélité pour chaque colonne du tableau de mesure (donc pour chaque
# valeur de mesurande)
# """
erreur_fidel_mA = np.std(mesures, 0, ddof=1)  # écart-type en colonne de nos mesures(mA)
erreur_fidel_PSI = (erreur_fidel_mA) / 0.4  # écart-type en colonne de nos mesurandes

erreur_fidel_max_mA = np.max(erreur_fidel_mA)  # maximum d'un tableau(array)
erreur_fidel_max_PSI = np.max(erreur_fidel_PSI)
print("L'erreur de fidélité est %5.2f mA ou %5.2f PSI" % (erreur_fidel_max_mA, erreur_fidel_max_PSI))
#
plt.figure(3)
plt.xlabel("Pression (PSI)")
plt.ylabel("Erreur de fidélité (PSI)")
plt.title("Erreur de fidélité en fonction de la pression")
plt.plot(pressions, erreur_fidel_PSI)
#
# """
# Q7 : Meilleure courbe estimée au sens des moindres carrés
# """
###Exemple d'approximation d'une courbe###
# xm = np.linspace(1,10,10) # mesurande
# a_theo = 2.0
# b_theo = -1.0
# ym = a_theo*xm + b_theo + np.random.uniform(-0.2,0.2,10)  # mesures bruitées
# deg = 1 # degré du polynome
# a_lin, b_lin = np.polyfit(xm, ym, deg) # pente , ordo. à l’orig.
# print ("pente = %.2f (théorique = %.2f)"%(a_lin,a_theo))
# print ("ord. orig. = %.2f (théorique = %.2f)"%(b_lin,b_theo))
# ylin = a_lin*xm + b_lin # meilleure droite

###Aapproximation de notre courbe###
pente_lin, ordonnee_origine_lin = np.polyfit(pressions,mesures_moy, deg=1)  # pente linéarisée, ordo. à l'orig. linéarisée
print("pente = %.2f (théorique = %.2f)" % (pente_lin, pente_constructeur))
print("ord. orig. = %.2f (théorique = %.2f)" % (ordonnee_origine_lin, ordonnee_origine_constructeur))
courbe_estimee = pente_lin * pressions + ordonnee_origine_lin
#
# """
# Q7 : Erreur de linéarité
# """
erreur_lin_mA = np.abs(mesures_moy - courbe_estimee)
erreur_lin_PSI = (erreur_lin_mA) / pente_constructeur

erreur_lin_max_mA = np.max(erreur_lin_mA)
erreur_lin_max_PSI = np.max(erreur_lin_PSI)
print("L'erreur de linéarité est %5.2f mA ou %5.2f PSI"%(erreur_lin_max_mA,erreur_lin_max_PSI))

plt.figure(4)
plt.plot(pressions,erreur_lin_PSI)
plt.xlabel("Pression (PSI)")
plt.ylabel("Erreur de linéarité (PSI)")
plt.title("Erreur de linéarité en fonction de la pression")
#
# """
# Q8 : Erreur de résolution
# """
nbits = 8
resol_mA =(20 -4)/ (2 ** nbits -1)

erreur_resol_mA = 0.5 * resol_mA
erreur_resol_PSI = erreur_resol_mA / pente_constructeur
print("L'erreur de résolution est %5.2f mA ou %5.2f PSI"%(erreur_resol_mA,erreur_resol_PSI))

# """
# Q9 : Erreur de justesse
# """
erreur_just_mA = np.sqrt(erreur_resol_mA ** 2 + erreur_lin_max_mA ** 2)
erreur_just_PSI = np.sqrt(erreur_resol_PSI ** 2 + erreur_lin_max_PSI ** 2)

print("L'erreur de justesse est %5.2f mA ou %5.2f PSI"%(erreur_just_mA,erreur_just_PSI))

# """
# Q10 : Erreur de précision
# """
erreur_prec_mA = np.sqrt(erreur_just_mA ** 2 + erreur_fidel_max_mA ** 2)
erreur_prec_PSI = np.sqrt(erreur_just_PSI ** 2 + erreur_fidel_max_PSI ** 2)

print("L'erreur de précision est %5.2f mA ou %5.2f PSI"%(erreur_prec_mA,erreur_prec_PSI))

# """
# Q11 : Classe de précision
# """
# class_psi = 100 * erreur_precision_PSI / étendue_de_mesure
class_psi = 100 * erreur_prec_PSI / 40

# # la classe doit être identique en mA et en PSI
# class_maa = 100 * erreur_prec_mA / étendue_de_mesure  # erreur sous estimée à cause de l'offset de 4 mA
class_ma = 100 * erreur_prec_mA / 16  # ok si on considère l'étendue de mesure convertie en mA
#
print (class_psi, class_ma)
# """
# Q12 : Garder les vecteurs jusqu'au dernier calcul et choisir la
# valeur maximale à la toute fin -méthode vectorielle
# """
v_erreur_just_PSI = np.sqrt(erreur_lin_PSI ** 2 + erreur_resol_PSI **2)
v_erreur_fidel_PSI = erreur_fidel_PSI
v_erreur_prec_PSI = np.sqrt(v_erreur_just_PSI ** 2 + v_erreur_fidel_PSI ** 2)
#
plt.figure(5)
plt.plot (pressions, v_erreur_just_PSI, 'b',label='justesse')
plt.plot (pressions, v_erreur_fidel_PSI, 'c',label='fidélité')
plt.plot (pressions, v_erreur_prec_PSI, 'r',label='précision')
plt.title ("Graphique des erreurs")
plt.xlabel ("Pression (PSI)")
plt.ylabel ("Erreur (PSI)")
plt.legend(loc='lower left')
#
print ("précision :")
print (v_erreur_prec_PSI)
#
erreur_prec_PSI_new = np.max(v_erreur_prec_PSI)
print ("précision ancienne méthode = %.2f PSI"%(erreur_prec_PSI))
print ("précision nouvelle méthode = %.2f PSI"%(erreur_prec_PSI_new))

plt.show()
