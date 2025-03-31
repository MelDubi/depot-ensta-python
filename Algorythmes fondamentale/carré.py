def decomp1(n, k_max=-1):
    reste = 0
    if k_max == -1:
        k_max = int(n ** 0.5)
    if n == k_max ** 2:
        return k_max, reste
    else:
        reste = n - k_max ** 2
        return k_max, reste


def decomp(n, k_max=-1):
    if k_max == -1:
        k_max = int(n ** 0.5)
    if n == k_max ** 2:
        return [k_max]
    for k in range(k_max, 0, -1):
        new_n = n - k ** 2
        decomposition_partielle = decomp(new_n, min(k - 1, int(new_n ** 0.5)))
        if len(decomposition_partielle) > 0:
            return decomposition_partielle+[k]
    return []


print(decomp(42))
