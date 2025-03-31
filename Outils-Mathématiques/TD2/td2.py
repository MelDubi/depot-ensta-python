import math


def is_pair(n):
    if n % 2 == 0:
        return True
    else:
        return False


def exo1():
    r = "Y"
    while r == "Y":
        n = int(input("Entrez un nombre\n"))
        if is_pair(n):
            print("PAIR")
        else:
            print("IMPAIRE")
        r = input("Voulez vous rejouer ?\n")
        r = r.upper()


def exo2():
    n = int(input("Entrez un nombre \n"))
    if not n%2:
        print("Vous pouvez diviser " + str(n // 2) +
              " fois le nombre " + str(n) + " par 2")
    else:
        print("Pas divisible par 2")


def exo3():
    for i in range(20):
        a = 7 * (i + 1)
        s = str(a)
        if (a % 3) == 0:
            s += "*"
        print(s)


def exo4():
    fact = math.factorial(1000)
    print(fact)
    print(len(str(fact)))


def exo5():
    u0 = 0
    u1 = 1
    n = int(input("n ?\n"))
    if n == 0:
        print("0")
        return
    for i in range(n - 1):
        tmp = u0 + u1
        u0 = u1
        u1 = tmp
    print(u1)


def exo6():
    n = int(input("Combien d'itération ? \n"))
    result = 0
    for i in range(n):
        result += (8 * (-1) ** i) / (((2 * i) + 1) * (2 * i + 3))
    result = (result + 4) / 2
    print(result)


def exo7():
    chaine = input("entrez une chaine : \n")
    print(chaine.count("y"))


def exo8():
    chaine = input("entrez une chaine : \n")
    tmp = ""
    for i in range(len(chaine)):
        tmp += chaine[len(chaine) - i - 1]
    print(tmp)


exo2()
