# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 14:12:37 2020

@author: Irvin Probst
"""

DEBUG = False

# on importe decode et on s'en sert pour lire le script des Monty Python
from read_file import decode
import heapq
import time
import numpy as np
import matplotlib.pyplot as plt

def count_intersect(vocabulary, ref):
    # compter le nombre de mots en commun entre la structure de données qui
    # est dans "vocabulary" et la liste de mots "ref".

    # mesurer l'heure qu'il est

    # pour chaque mot dans ref
        # regarder si ce mot est dans vocabulary
        # si oui:
            # incrémenter un compteur


    cpt = 0
    t0 = time.process_time_ns() # !!!! ATTENTION il faut utiliser la bonne fonction suivant votre ordi, cf moodle ou forum
    for word in ref:
        if word in vocabulary:
           cpt += 1

    # trouver le temps passé dans la fonction
    dt = time.process_time_ns() - t0
    # renvoyer le compteur et le temps passé
    return cpt, dt


if __name__ == "__main__":
    holy_script_list = decode("grail.txt")
    # ouverture du fichier de vocabulaire
    fd_voc = open("dico_gb.txt", "r")
    voc_list = []

    # on parcours le fichier ligne à ligne
    for line in fd_voc: # chaque ligne est en fait un mot
        voc_list.append(line.strip()) # on fait le ménage avant de stocker

    fd_voc.close() # on est propres et on ferme derrière nous


    if DEBUG: # pour la mise au point on tronque le dictionnaire.
        voc_list = voc_list[:100]
        # on affiche quelques mots pour tester
        print(voc_list[:10])
        print(len(voc_list))
        print(holy_script_list[:10])


    #nb_common, dt = count_intersect(voc_list, holy_script_list)
    #print("le nombre de mots trouvé une ou plusieurs fois en commun est ", nb_common)
    nb_mots = 100, 500, 1000, 5000, 10000, 30000, 50000, 70000, 80000, 100000, len(voc_list)
    dt_list = []
    dt_dico = []
    print("Ne pas hésiter à supprimer la recherche dans une liste si c'est trop long")
    for i in nb_mots:
        print(i)
        voc_list_short = voc_list[:i]
        voc_list_set = set(voc_list_short)
        _, dt = count_intersect(voc_list_short, holy_script_list)
        dt2 = 0
        # on répète pour avoir une mesure la plus fiable possible
        for _ in range(100):
            _, dt2_new =  count_intersect(voc_list_set, holy_script_list)
            dt2 += dt2_new
        dt_list.append(dt)
        dt_dico.append(dt2_new / 100)

    # tracer dt_list en fonction de nb_mots
    plt.figure()
    plt.subplot(211)
    plt.plot(nb_mots, dt_list)
    plt.xlabel("Nombre de mots")
    plt.ylabel("Temps de recherche (s)")
    plt.title("Analyse de performance des listes")
    plt.subplot(212)
    plt.plot(nb_mots, dt_dico)
    plt.xlabel("Nombre de mots")
    plt.ylabel("Temps de recherche (s)")
    plt.title("Analyse de performance des sets")
    plt.show()


