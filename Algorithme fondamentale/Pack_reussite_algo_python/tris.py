# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 13:34:02 2020

@author: Irvin Probst
"""

from numpy import random
import numpy as np
import time

def generate(nb=10, m=100, seed_to_set=4242):
    """
    Génère un array de nb éléments, compris entre 0 inclus et
    m exclus. La graine du générateur de nb aléatoires est initialiséé
    à seed
    """
    random.seed(seed_to_set)
    rnd_array = random.randint(0, m, nb)
    return rnd_array

def is_sorted(array_to_test):
    """
    On va parcourir array_to_test et comparer l'élément i
    à l'élément i+1. 
    pour tous les i de la première à l'avant avant dernière case du tableau:
    	si array_to_test[i] > array_to_test[i +1]
            	=> STOP renvoyer faux
    
    Renvoyer vrai
    """
    for i in range(len(array_to_test) - 1):
        if array_to_test[i] > array_to_test[i + 1]: #le tableau n'est pas trié
            return False
  
    return True


def selection_sort(array_to_sort_orig):
     # utile seulement dans le cadre du TP pour éviter de trier le tableau en paramètre
    array_to_sort = array_to_sort_orig.copy()
    t_start = time.time()
    last = len(array_to_sort)
    while last: # tant que last != 0
        max_idx = 0
        for idx in range(last):
            if array_to_sort[idx] > array_to_sort[max_idx]:
                max_idx = idx
        array_to_sort[last - 1], array_to_sort[max_idx] = array_to_sort[max_idx], array_to_sort[last - 1]
        last -= 1
    delta_t = time.time() - t_start
    return delta_t, array_to_sort
    

def insertion_sort(array_to_sort_orig, step=1, copy_data = True):
     # utile seulement dans le cadre du TP pour éviter de trier le tableau en paramètre
    if copy_data:
        array_to_sort = array_to_sort_orig.copy()
    else:
        array_to_sort = array_to_sort_orig
        
    t_start = time.time()
    # procédure tri_insertion(tableau T, entier n)
    #      pour i de 1 à n - 1
    for i in range(step, len(array_to_sort)):
        #           # mémoriser T[i] dans x
        #           x ← T[i]                            
        key = array_to_sort[i]
        # décaler vers la droite les éléments de T[0]..T[i-1] qui sont plus grands que x en partant de T[i-1]
        # j ← i
        j = i                               
        # tant que j >= step et T[j - 1] > x
        while (j >= step and array_to_sort[j - step] > key):
            # T[j] ← T[j - 1]
            array_to_sort[j] = array_to_sort[j - step]
            # j ← j - 1
            j -= step

        # placer x dans le "trou" laissé par le décalage
        array_to_sort[j] = key

    delta_t = time.time() - t_start
    return delta_t, array_to_sort

def shell_sort(array_to_sort_orig):
     # utile seulement dans le cadre du TP pour éviter de trier le tableau en paramètre
    array_to_sort = array_to_sort_orig.copy()
    t_start = time.time()
    
    # en fonction de la taille du tableau à trier trouver le plus grand pas de départ possible
    # selon la suite Un+1 = 3 * Un + 1
    
    Un = 1 # U0 = 1
    while Un < len(array_to_sort):
        Un = 3 * Un +1
    
    # le premier pas à choisir est l'antécédant de Un suivant la suite
    step = (Un - 1) // 3 # attention division entière
    
    while step >= 1: # le dernier passage doit être un tri par insertion, ie pas = 1
        # faire un tri pas insertion avec un pas qui vaut "pas" au lieu de 1 par défaut
        
        _, array_to_sort = insertion_sort(array_to_sort, step, False)
        # le pas suivant à traiter:
        step = (step - 1) // 3
    
    delta_t = time.time() - t_start
    return delta_t, array_to_sort


if __name__ == "__main__":
#    q1_array = generate(1000, 1000)
#    print(sum(q1_array))
#    
#    test_q2 = np.arange(50)
#    #=> en principe is_sorted(test_q2) doit renvoyer vrai
#    print(is_sorted(test_q2))
#    test_q2[30] = 42
#    #=> en principe is_sorted(test_q2) doit renvoyer faux
#    print(is_sorted(test_q2))
    
    # graine = 0
    # tant que ce que renvoie generate(les_bons_arguments, seed=graine) n'est pas trié
    #   => incrémenter graine
    # afficher la graine en sortie de "tant que"
    
#    graine = 0
#    while not is_sorted(generate(10, 10, graine)):
#        graine += 1
#    print(graine)
    
    test_array = generate(1000, 1000)
    dt_shell, shell_sort_array = shell_sort(test_array)
    print("shell sort works", is_sorted(shell_sort_array))
    print("Time in shell sort", dt_shell)
    # on teste sur un tableau déjà trié
    dt_shell_sorted, _ = shell_sort(shell_sort_array)
    print("Time in shell sort on sorted array", dt_shell_sorted)

    dt_select, select_sort_array = selection_sort(test_array)
    print("select sort works", is_sorted(select_sort_array))
    print("Time in select sort", dt_select)
    # on teste sur un tableau déjà trié
    dt_select_sorted, _ = selection_sort(select_sort_array)
    print("Time in select sort on sorted array", dt_select_sorted)

    dt_insertion, insertion_sort_array = insertion_sort(test_array)
    print("insertion sort works", is_sorted(insertion_sort_array))
    print("Time in insertion sort", dt_insertion)
    # on teste sur un tableau déjà trié
    dt_insertion_sorted, _ = insertion_sort(select_sort_array)
    print("Time in insertion sort on sorted array", dt_insertion_sorted)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
