# -*- coding: utf-8 -*-
"""
@author: Christophe Osswald. WTFPL
"""

def factorielle(n):
    if n<=1:
        return 1
    f = n*factorielle(n-1)
    return f

print(factorielle(10))