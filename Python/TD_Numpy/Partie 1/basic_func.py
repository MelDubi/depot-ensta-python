# -*- coding: utf-8 -*-
import numpy as np
import time

def average(a):
    """
    Compute the average value of ``a``

    Parameters
    ----------
    a : ndarray
        Input array.

    Returns
    -------
    avg : int
        The average value of ``a``
    """

    sum_a = 0
    for i in range(len(a)):
        sum_a += a[i]
    return sum_a / len(a)


if __name__ == "__main__":
    # tableau de données pour les fonctions numpy
    rand_array_1 = np.random.randint(0, 10000, 10000)

    # le même sous forme de liste classique pour le calcul en Python seul
    rand_array_list = list(rand_array_1)

    t0 = time.perf_counter_ns()
    # on répète le calcul 100 fois pour tenter de minimiser l'influence
    # d'événements exterieurs qui ralentiraient momentanément l'ordinateur
    for _ in range(100):
        average_value = average(rand_array_list)
    dt_python = time.perf_counter_ns() - t0

    t0 = time.perf_counter_ns()
    # on répète le calcul 100 fois pour tenter de minimiser l'influence
    # d'événements exterieurs qui ralentiraient momentanément l'ordinateur
    for _ in range(100):
        average_value = np.mean(rand_array_1)
    dt_numpy = time.perf_counter_ns() - t0

    print("Temps en ns nécessaire en Python seul", dt_python)
    print("Temps en ns nécessaire avec Numpy", dt_numpy)
    print("Numpy est %lf fois plus rapide sur ce calcul"%(dt_python / dt_numpy))
