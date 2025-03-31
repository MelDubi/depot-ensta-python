#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Création de tableaux aléatoires, tris.

.. codeauthor:: R. Moitié
"""

import numpy as np
from datetime import datetime


def genere(n=10, m=100, seed=4242):
    """Génération de tableau aléatoire.

    Parameters
    ----------
    n : int
        Taille du tableau (defaut 10).
    m : int
        Valeur maximale des éléments du tableau (defaut 100).
    seed : int
        Graine de génération de nombres aléatoires (defaut 4242).

    Returns
    -------
    Tableau aléatoire généré.
    """
    if seed is not None:
        np.random.seed(seed)
    return np.random.randint(0, m, n)


def est_trie(tab):
    """Teste si un tableau est trié.

    Parameters
    ----------
    tab : numpy.array
        Tableau à tester.
    """
    for i in range(len(tab) - 1):
        if tab[i] > tab[i + 1]:
            return False
    return True


def est_trie_2(tab):
    """Teste si un tableau est trié. Version sans boucle explicite en Python.

    Parameters
    ----------
    tab : numpy.array
        Tableau à tester.
    """
    return np.all(tab[1:] - tab[:-1] >= 0)


def question1():
    print('Initialisation du tableau')
    print(sum(genere()))
    tab = genere(1000, 1000)
    print(sum(tab))


def question2():
    print('\nTest de tableau trié')
    i = 0
    while not est_trie(genere(10, 10, i)):
        i += 1
    print(i, genere(10, 10, i))


if __name__ == '__main__':
    question1()
    question2()
