#1 Volume d'un cône

pi = 3.14
r = 3.25
h = 42.18
v = (pi * (r ** 2) * h) / 3
print("Le volume est de:", v, "mettre ici la bonne unité !")



#2 TVA

# prix_ht = 100.
# taux_tva = 20 # ici au sens 20%
#
# prix_ttc = prix_ht * (1 + taux_tva / 100)
# print("Le prix ttc est de:", prix_ttc)



#3 Séparateur de ville

# ville_1 = "Brest"
# ville_2 = "Landerneau"
# distance = 25
# tirets_distance = "-" * distance
# print(ville_1, tirets_distance, ville_2, sep="x")



#4 Nombre de Marches dans un phare

# marches = int(input("Entrez le nombre de marche :"))
# hauteur = int(input("Entrez la hauteur d'une marche :"))
# Parcours = float(marches*hauteur*10*7)/100
#
# print("Pour",marches,"marches de",hauteur,"cm, il parcourt par semaine",Parcours,"mètres")



#5 Seconde en années, mois, jour, jours, heures, minutes, secondes

# Time = float(input("Nombre de seconde :"))
#
# Ans = Time//31540000
# Reste1 = Time%31540000
# Mois = Reste1//2628000
# Reste2 = Reste1%2628000
# Jour = Reste2//86400
# Reste3 = Reste2%86400
# Heures = Reste3//3600
# Reste4 = Reste3%3600
# Min = Reste4//60
# Seconde = Reste4%60
#
# print("Ans :",Ans,"Mois :",Mois,"Jours :",Jour,"Heures :",Heures,"Min :",Min,"Seconde",Seconde)

# seconde = int(12345678912)
#
# ans = 60*60*24*365
# mois = 60*60*24*31
# jour = 60*60*24
# heure = 60*60
# minutes = 60
#
# nb_ans = seconde//ans
# reste_ans = seconde%ans
# nb_mois = reste_ans//mois
# reste_mois = reste_ans%mois
# nb_jour = reste_mois//jour
# reste_jour = reste_mois%jour
# nb_heure = reste_jour//heure
# reste_heure = reste_jour%heure
# nb_minutes = reste_heure//minutes
# nb_seconde = reste_heure%minutes
#
# print(seconde,"vaut",nb_ans,"années",nb_mois,"mois",nb_jour,"jours",nb_heure,"heures",nb_minutes,"minutes",nb_seconde,
#       "secondes")






#6 Radians, degré, minutes, secondes

# AngleD = int(input("Angle en degré : "))
#
# AngleR = AngleD/360
# Minutes = AngleD*30/180
# Secondes = AngleD*1800/180
#
# print("L'angle en radian vaut : ",AngleR)
# print("L'angle en minutes vaut : ",Minutes)
# print("L'angle en Secondes vaut : ",Secondes)





#7 Degré celcius et Fahrenheit

#TempC = float(input("Temperature en degré celcius :"))
#TempF = float(input("Temperature en degré Fahrenheit :"))
#C = (TempF-32)/1.8
#F = TempC*1.8+32

#print("La temperature en degre celcius :",TempC,"vaut en degre Fahrenheit : ",F)
#print("La temperature en degre Fahrenheit :",TempF,"vaut en degre celcius : ",C)





#8 Vitesse km/h, m/s et miles/h

#VitesseM = float(input("Vitesse en miles/heure : "))
#VitesseK = 1.60934*VitesseM
#VitesseS = VitesseK*0.277778

#print("La vitesse en miles/heure",VitesseM,"vaut en km/h :",VitesseK,"et en m/s vaut :",VitesseS)











