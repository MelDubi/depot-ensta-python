import numpy as np


def dichotomie(a, b, f, eps=1e-6, last_c=0):
    global cnt

    if not (f(a) < 0 and f(b) > 0):
        return None

    c = (a + b) / 2
    if np.abs(f(c)) > eps:
        cnt += 1

        if f(a) * f(c) < 0:
            dichotomie(a, c, f, last_c=c)
        else:
            dichotomie(c, b, f, last_c=c)
    else:
        print("En utilisant la recherche par Dichotomie z = ", last_c)
        print("En utilisant la recherche par Dichotomie : %s < %s < %s" %(a, last_c, b))
        print("cnt:", cnt, end="\n\n")
        return last_c


def f(x):
    return np.sin(x) - (x / 2)

cnt = 0
dichotomie(- np.pi / 2, np.pi / 3, f)