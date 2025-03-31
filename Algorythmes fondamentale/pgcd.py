def pgcd(a, b):
    reste = a%b
    if reste == 0:
        return b
    return pgcd(b, reste)


print(pgcd(16, 20))
