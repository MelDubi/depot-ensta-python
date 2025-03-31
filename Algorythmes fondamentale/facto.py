import numpy as np
import matplotlib.pyplot as plt
import time


def factorielle(n):
    if n <= 1:
        return 1
    f = n * factorielle(n - 1)
    return f


def fibo(n):
    x = 0
    y = 1
    for i in range(n - 1):
        z = x + y
        x = y
        y = z


def fibo_recu(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo_recu(n - 1) + fibo_recu(n - 2)


def fibo_term(Unow, Ubefore, n):
    if n == 0:
        return Ubefore
    if n == 1:
        return Unow
    else:
        return fibo_term(Unow+Ubefore, Unow, n-1)


print(fibo_term(1, 0, 12))
