# -*- coding: utf-8 -*-
"""
@author: Christophe Osswald. WTFPL
"""

def fibonacci(n):
    return fibonacci_term(0, 1, n)

def fibonacci_term(a, b, n):
    if n>1:
        return fibonacci_term(b, a+b, n-1)
    elif n==1:
        return b
    else:
        return a

print(fibonacci(92))