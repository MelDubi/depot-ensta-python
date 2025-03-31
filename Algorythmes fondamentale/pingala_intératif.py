def pingala_rec(a, n):
    if n == 0:
        return 1
    else:
        p = pingala_rec(a, n // 2)
        if (n % 2) == 0:
            p = p * p
        else:
            p = p * p * a
    return p


def pingala_iter(a, n):
    q_tab = []
    nb_q = 1
    q_tab.append(n)
    p = 1

    while q_tab[nb_q - 1] > 0:
        q_tab.append(q_tab[nb_q - 1] // 2)
        nb_q = nb_q + 1

    while nb_q > 0:
        p = p * p
        if (q_tab[nb_q - 1] % 2) != 0:
            p = p * a
        nb_q = nb_q - 1
    return p


print("p:", pingala_iter(5, 13))



