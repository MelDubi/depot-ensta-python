# -*- coding: utf-8 -*-
"""
@author: Christophe Osswald. WTFPL
"""

def pgcd(a, b):
    if a<b:
        return pgcd(b,a)
    if b==0:
        return a
    return pgcd(b, a%b)

print(pgcd(477865542,717173730))