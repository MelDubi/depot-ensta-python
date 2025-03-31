import math
import matplotlib.pyplot as plt
import time


def log(x):
    return math.log(x, 10)


def racine(x):
    return math.sqrt(x)


def int_sup(x):
    return math.ceil(x)


def int_inf(x):
    return math.floor(x)


def sont_proches(x, y):
    atol = 10**-5
    rtol = 10**-8
    if abs(x-y) <= atol + abs(y) * rtol:
        return True
    else:
        return False


def mystere(x, y):
    if x < y:
        return 0
    else:
        return 1 + mystere(x/y, y)

#print(mystere(1001,10))
#print(log(1001))

N=100


# Crible d'Eratosthène
def erato_iter(N):
    if  N < 1 :
        return 0

    list_bool = [True]*N
    list_bool[0] = False

    for i in range(2, int(math.sqrt(N)+1)):
        if list_bool[i-1] :
            for j in range(len(list_bool)):
                if j % i == 0 and j != i:
                    list_bool[j-1] = False

    return list_bool

#print(erato_iter(20))

# Générateur de nombre premiers
def SieveOfAtkin(limit):
    if limit > 2:
        print(2, end=" ")
    if limit > 3:
        print(3, end=" ")
    sieve = [False] * (limit + 1)
    for i in range(0, limit + 1):
        sieve[i] = False
    x = 1
    while x * x <= limit:
        y = 1
        while y * y <= limit:
            n = (4 * x * x) + (y * y)
            if (n <= limit and (n % 12 == 1 or
                                n % 12 == 5)):
                sieve[n] ^= True

            n = (3 * x * x) + (y * y)
            if n <= limit and n % 12 == 7:
                sieve[n] ^= True

            n = (3 * x * x) - (y * y)
            if (x > y and n <= limit and
                    n % 12 == 11):
                sieve[n] ^= True
            y += 1
        x += 1
    r = 5
    while r * r <= limit:
        if sieve[r]:
            for i in range(r * r, limit + 1, r * r):
                sieve[i] = False

        r += 1
    for a in range(5, limit + 1):
        if sieve[a]:
            print(a, end=" ")



limit = 500
#SieveOfAtkin(limit)

def bbs(N):
    p1 = 24375763
    p2 = 28972763
    M = p1 * p2
    # calculer la graine
    xi = time.time()
    xi = int(( xi - int(xi)) *1e7)
    A=0
    for i in range(N):
        if xi % 2: # si xi est impair
            A = A + 2**i
            # calculer le nouvel xi
            xi = (xi ** 2 )% M
    return A

print(bbs(10000))









