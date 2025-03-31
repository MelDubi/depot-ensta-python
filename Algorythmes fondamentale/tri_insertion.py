import numpy as np


def get_random_tab(size=10, max_val=100, seed=4242):
    np.random.seed(seed)
    return np.random.randint(0, max_val, size)


def tri_insertion(tab):
    for i in range(1, len(tab)):
        x = tab[i]
        j = i
        while j > 0 and tab[j - 1] > x:
            tab[j] = tab[j - 1]
            j = j-1
        tab[j] = x
    return tab


n = 10000
m = 20000
list = get_random_tab(n, m)
tri = tri_insertion(list)
print(tri[200])
print(tri[9090])

