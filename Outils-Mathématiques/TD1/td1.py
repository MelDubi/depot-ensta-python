import math


def volume_cone(r, h):
    volume = (math.pi * (r ** 2) * h) / 3
    return volume


def prix_ttc(prix):
    return prix + prix * 0.2


def trace_villes(v1, v2, distance):
    separateur = '-'
    print(v1, v2, "Tanguy", sep=separateur * distance)


def phare():
    marches = int(input("Combien de marches ?\n"))
    hauteur = int(input("hauteur ?(en cm)\n"))
    distance = str(5 * 2 * (marches * hauteur / 100) * 7)
    marches = str(marches)
    hauteur = str(hauteur)
    print("Pour " + marches + " marches de " + hauteur + " cm, il parcours par semaine " + distance + " mètres\n")


def conv_de_temps(temps):
    annee = temps // (365 * 24 * 60 * 60)
    mois = temps // (30 * 24 * 60 * 60)
    jour = temps // (24 * 60 * 60)
    minute = temps // 60
    print(annee)
    print(mois)
    print(jour)
    print(minute)


def conv_radians(angle):
    return angle / (360 / (2 * math.pi))


def conv_celcius(tempf):
    return (tempf - 32) / 1.8


def conv_vitesse(v):
    return v * 1.609


print(volume_cone(5, 5))
print(prix_ttc(20))
trace_villes("Paris", "Lyon", 10)
# phare()
conv_de_temps(12345678912)
print(conv_radians(360))
print(conv_celcius(120.20))
print(conv_vitesse(60))
