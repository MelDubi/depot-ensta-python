#Exercice 1

# def ajoute_1(mon_chiffre):
#     mon_chiffre+=1
#     return mon_chiffre
# chiffre = ajoute_1(0)
# print(chiffre)

#Exercice 2
# liste=[]
#
# def puissance(x,n):
#
#     for i in range(1,n+1):
#         liste.append(x**i)
#     return liste
#
#
# res = puissance(3,4)
# for i in range(len(liste)):
#     print(res[i])

#Exercice 3

# def nbpattes(p,v,c):
#     nbp=p*2
#     nbv=v*4
#     nbc=c*2
#     return nbp+nbv+nbc
#
# p=int(input("Rentrez le nombre de poulet :"))
# v=int(input("Rentrez le nombre de vache :"))
# c=int(input("Rentrez le nombre de canard :"))
#
# total=nbpattes(p,v,c)
# print(total)

#Exercice 4

# def f_trinome(a,b,c,x):
#     pol=a*x**2+b*x+c
#     return pol
#
# a=int(input("Rentrez a :"))
# b=int(input("Rentrez b :"))
# c=int(input("Rentrez c :"))
# x=int(input("Rentrez x :"))
#
# pol=f_trinome(a,b,c,x)
# print(pol)

#Exercice 5

# def f2(x):
#     return(x + 1)
# def f3(x, f23):
#     print(f23(x) * 2)
#
# res_f3 = f3(4, f2)

#Exercice 6

# def somme_carres(n):
#     res=0
#     for i in range(n+1):
#         res+= i**2
#     return res
#
# print(somme_carres(2))

#Exercice 8

# from math import sqrt, pi
# def suite_mystere(n):
#     res=0
#     for i in range(1,n+1):
#         res += 1/(1**2)
#     return sqrt(6*res)
#
#
# print(suite_mystere(10))

