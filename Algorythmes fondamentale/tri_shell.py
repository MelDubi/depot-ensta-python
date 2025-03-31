import numpy as np
import time


def get_random_tab(size=10, max_val=100, seed=4242):
    np.random.seed(seed)
    return np.random.randint(0, max_val, size)


n = 100000
m = 500000
tableau = get_random_tab(n, m-1)
#
#
# def gaps(value):
#     gaps = [1]*value
#     u = 0
#     for i in range(0, value, 1):
#         u = 3*u + 1
#         gaps[i] = u
#     return gaps[::-1]
#
#
# gap = gaps(5)
#
#
# def tri_insertion(tab, gap=1):
#     for i in range(gap, len(tab)):
#         x = tab[i]
#         j = i
#         while j >= gap and tab[j - gap] > x:
#             tab[j] = tab[j - gap]
#             j = j-gap
#         tab[j] = x
#     return tab
#
# print(tri_insertion(tableau, gap))
#
# def tri_shell (tab, gaps):
#     for gap in gaps:
#         # Pour chaque sous-tableau
#         for i in range(0, gap):
#             # on fait un tri par insertion
#             tab = tri_insertion(tab, gap)
#     return tab
#
#
# # tri = tri_shell(tab, gaps)
# print(tri[100])
# print(tri[80808])

# code de tanguy

def tri_shell(tab):
    global tab_sort
    start_time = time.time()

    def get_gaps(tableau):
        gap = 0
        gaps = []
        while gap < len(tableau):
            gap = 3 * gap + 1
            gaps.append(gap)

        return np.flip(gaps)

    def tri_insert(tab, gap=1):
        for i in range(gap, len(tab)):
            x = tab[i]

            j = i
            while j >= gap and tab[j - gap] > x:
                tab[j] = tab[j - gap]
                j = j - gap

            tab[j] = x

        return tab

    gaps = get_gaps(tab)

    for gap in gaps:
        tab_sort = tri_insert(tab, gap)

    end_time = time.time()
    process_time = end_time - start_time

    return tab_sort, process_time



print("tab avant tri shell: ", tableau)
tab_sorted, process_time = tri_shell(tableau)
print("tab après tri shell: ", tab_sorted)
print("val de l'index 100: ", tableau[100])
print("val de l'index 80808: ", tableau[80808])
print("Temps d'execution", process_time)