# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# Q4 : Réponse du capteur avec capteur considéré linéaire (faible erreur de linéarité)
#---------------------------------------------------------------------------------------
pressions = np.array([0.0,50.0])
sortie_ma = np.array([4.0,20.0])
plt.figure()
plt.title ("Courbe caractéristique de réponse du capteur")
plt.xlabel ("Pression (bar)")
plt.ylabel ("Courant (mA)")
plt.ylim(0,20)
plt.grid(True)
plt.plot (pressions,sortie_ma,'c-o')

# Q5 : Constante de temps
#      il faut utiliser np.log() pour ln()
#----------------------------
tau = -5.0/np.log(0.1)   # np.log() pour ln()
print ("La constante de temps est de %4.2f ms"%(tau))

# Q6.a : Dérive thermique du zéro
#---------------------------------
t_amb = 20.0    # température ambiante de 20°C
t_min = -20.0   # température minimum (domaine de température compensé)
t_max = 80.0    # température maximum (domaine de température compensé)

zero = 4.0      # 4 mA à 20°C
em_bar = 50.0   # Etendue de mesure = 50 bars
em_ma = 16.0    # Etendue de Mesure = [4,20] mA soit 16 mA

err_zero_deg = 0.015/100.0*em_ma # Dérive du zéro pour 1°C = 0.015%Em d'après la fiche technique

zero_min =  zero - err_zero_deg*(t_amb-t_min)
print ("valeur minimale du zéro = %5.2f mA"%(zero_min))

zero_max =  zero + err_zero_deg*(t_max-t_amb)
print ("valeur maximale du zéro = %5.2f mA"%(zero_max))

plt.figure()
plt.title ("Erreur due à la dérive thermique du zero")
plt.xlabel ("Pression (bar)")
plt.ylabel ("Courant (mA)")
plt.ylim(1,21)
plt.grid(True)

sensibilite = em_ma/em_bar # Sensibilité constante (capteur linéaire)
droite_zero = pressions*sensibilite+zero # Droite parfaite
droite_zero_min = pressions*sensibilite+zero_min # Droite pour température min
droite_zero_max = pressions*sensibilite+zero_max # Droite pour température max

plt.plot (pressions,droite_zero_min,'r-o')
plt.plot (pressions,droite_zero_max,'r-o')

err_zero_min = np.max(np.abs(droite_zero_min-droite_zero))
err_zero_max = np.max(np.abs(droite_zero_max-droite_zero))

err_zero = np.max([err_zero_min, err_zero_max])  # utiliser np.max()
print ("erreur maximale due à la dérive thermique du zéro = %5.2f ma"%(err_zero))

# Q6.b : dérive thermique de la sensibilité
#------------------------------------------

err_sens_deg = 0.015/100.0*em_ma # erreur à la pleine échelle (EM) due à la dérive de la sensibilité pour 1 $^o$C
err_temp_min = err_sens_deg*(t_amb-t_min) # erreur pour la temperature min
err_temp_max = err_sens_deg*(t_max-t_amb) # erreur pour la temperature max
#print (err_temp_min,err_temp_max)

sensibilite_min = sensibilite - err_temp_min/em_bar
sensibilite_max = sensibilite + err_temp_max/em_bar

droite_sens = pressions*sensibilite+zero # Droite parfaite
droite_sens_min = pressions*sensibilite_min+zero  # Droite à température min
droite_sens_max = pressions*sensibilite_max+zero  # Droite à température max

plt.figure()
plt.title ("Erreur due à la dérive thermique de sensibilité")
plt.plot (pressions,droite_sens_min,'b-o')
plt.plot (pressions,droite_sens_max,'b-o')

# Autre possibilité de calcul avec les droites
# err_sens_min1 = np.max(np.abs(droite_sens_min-droite_sens)) # idem err_temp_min
# err_sens_max1 = np.max(np.abs(droite_sens_max-droite_sens)) # idem_err_temp_max
# print (err_sens_min1,err_sens_max1)
# err_sens1 = np.max([err_sens_min1, err_sens_max1])

err_sens = np.max([err_temp_min, err_temp_max])
print ("erreur maximale due à la dérive thermique de la sensibilité = %5.2f ma"%(err_sens))

# Q6.c : erreur globale de dérive thermique
#-------------------------------------------

plt.figure()
plt.title ("Erreur globale due à la dérive thermique (zero, sensibilité)")
plt.plot (pressions,droite_zero_min+droite_sens_min-droite_sens,'g-o')
plt.plot (pressions,droite_zero_max+droite_sens_max-droite_sens,'g-o')

err_deriv_therm_ma = err_zero+err_sens
print ("erreur maximale due à la dérive thermique = %5.2f ma"%(err_deriv_therm_ma))

err_deriv_therm_ma_relative = err_deriv_therm_ma/em_ma*100.0
print ("erreur maximale due à la dérive thermique relative à l'EM = %5.2f %%"%(err_deriv_therm_ma_relative))

err_deriv_therm_bar =  err_deriv_therm_ma/sensibilite # passage des ma aux bars
print ("erreur maximale due à la dérive thermique = %5.2f bar"%(err_deriv_therm_bar))
err_deriv_therm_bar_relative = err_deriv_therm_bar/em_bar*100.0
print ("erreur maximale due à la dérive thermique relative à l'EM = %5.2f %%"%(err_deriv_therm_bar_relative))

# Q7.d : erreur globale, comparaison avec le fiche technique du constructeur
#---------------------------------------------------------------------------
# incertitude globale de -20°C à +80°C inférieure à 2% de l'étendue de mesure (EM) d'après fiche technique
# notre calcul donne 1.8 % de l'EM avec une température de référence de 20°C, l'ordre de grandeur est respecté


plt.show ()