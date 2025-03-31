def square_decomposition(n, n_max=-1):
    if n_max == -1:
        n_max = int(n ** 0.5)
    if n == n_max ** 2:
        return [n_max]
    else:
        for k in range(n_max, 0, -1):
            new_n = n - k ** 2
            remainder = square_decomposition(new_n,
                                             min(k - 1, int(new_n ** 0.5)))
            if len(remainder) > 0:
                return remainder + [k]
        return []


for n in range(100):
    decomp = square_decomposition(n)
    somme_carre = 0
    for nb in decomp:
        somme_carre += nb ** 2
    assert len(decomp) == 0 or somme_carre == n
    print("%i \t%s" % (n, str(decomp)))
