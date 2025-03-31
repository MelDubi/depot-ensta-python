import numpy as np
#
#
#
# def tab_numpy(n=1000, m=1000, seed=4242):
#     somme = 0
#     np.random.seed(seed)
#     list = np.random.randint(0, m-1, n)
#     for i in range(n):
#         somme += list[i]
#     return somme
#
# def  is_sorted(tab):
#     for i in range(np.size(tab) - 1):
#         if tab[i + 1] < tab[i]:
#             return False
#     return True

def get_random_tab(size=10, max_val=100, seed=4242):
    np.random.seed(seed)
    return np.random.randint(0, max_val, size)
#
#
# sorted_tab = False
# i = -1
# while not sorted_tab:
#     i += 1
#     leau = get_random_tab(10, 10, i)
#     sorted_tab = is_sorted(leau)
#     print(leau)
#
# print(i)
# print(leau)

# import time
# tab = [5, 8, 9, 1, 4, 0]
# t_start = time.time()
# last = len(tab)
# while last:
#     max_idx = 0
#     for idx in range(last):
#         if tab[idx] > tab[max_idx]:
#             max_idx = idx
#     tab[last - 1], tab[max_idx] = tab[max_idx], tab[last - 1]
#     last -= 1

# print("Temps pour trier %d éléments: %f s" % (len(tab), time.time() - t_start))
# print(tab)




