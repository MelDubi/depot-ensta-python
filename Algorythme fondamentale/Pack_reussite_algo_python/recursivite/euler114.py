# -*- coding: utf-8 -*-
"""
@author: Christophe Osswald. WTFPL.
"""

""" compte le nombre de façons de remplir n cases"""
def euler(n):
    # si moins de trois cases : tout en noir !
    if n<3:
        return 1
    
    poss = 1 # initialisé avec l'option "tout en noir"
    # red est le nombre de cases rouges que l'on place au début
    for red in range(3, n+1):
        if n-red==0:     # Tout en rouge
            poss += 1
            continue
        poss += 1 # Cas où on ne met pas de rouge, mais juste un noir
        for black in range(1, n-red+1):
            poss += euler(n-red-black)
    return poss

""" compte le nombre de façons de remplir n cases
utilise un dictionnaire pour éviter de calculer plusieurs fois la même chose."""
def euleropt(n, known={}):
    # si moins de trois cases : tout en noir !
    if n<3:
        known[n]=1
        return 1
    
    poss = 1 # initialisé avec l'option "tout en noir"
    # red est le nombre de cases rouges que l'on place au début
    for red in range(3, n+1):
        if n-red==0:     # Tout en rouge
            poss += 1
            continue
        poss += 1 # Cas où on ne met pas de rouge, mais juste un noir
        for black in range(1, n-red+1):
            if (n-red-black) in known:
                poss += known[n-red-black]
            else:
                poss += euleropt(n-red-black, known)
    known[n]=poss
    return poss

if __name__=="__main__":
    for n in range(51):
        #print("n = {} : {} possibilités".format(n, euler(n)))
        print("n = {} : {} possibilités".format(n, euleropt(n)))