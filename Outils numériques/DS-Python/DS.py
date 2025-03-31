#Exercice 1
#Question 1
#1

#liste_nombres = [15, 34, 89, 33, 11, 28, 18, 981, 42, 12, 69]

# def min_liste(liste_nombres):
#     minl = liste_nombres[0]
#     for i in range(len(liste_nombres)):
#         if liste_nombres[i] < minl:
#             minl = liste_nombres[i]
#     return minl
#
# min = min_liste(liste_nombres)
# print(min)

#2

# def moy_liste(liste_nombres):
#     total_moy = 0
#     for i in range(len(liste_nombres)):
#         total_moy += liste_nombres[i]
#
#     moy = total_moy/(len(liste_nombres))
#     return moy
#
# moy = moy_liste(liste_nombres)
# print(moy)
#
# moy_verif=(15+34+89+33+11+28+18+981+42+12+69)/11
# print(moy_verif)

#Question 2

# def mult3_liste(liste_nombres):
#     mult3=[]
#     for i in range(len(liste_nombres)):
#         if liste_nombres[i] % 3 == 0:
#             mult3.append(liste_nombres[i])
#     return mult3
#
# mult3 = mult3_liste(liste_nombres)
# print(mult3)


#Exercice 2

#Question 1
#Pour U=0 et U=1

# def suracuse0(h, n):
#     U=[1]*n
#     U[0]=h
#     if U[0] % 2 == 0:
#         U[1] = U[0]//2
#     else :
#         U[1] = 1 + 3*U[0]
#     return U[1]
#
# U = suracuse0(15,20)
# print(U)

# def suracuse(h, n):
#     U=[1]*n
#     U[0]=h
#     for i in range(n):
#         if U[i] % 2 == 0:
#             U[i+1] = U[i]//2
#         else :
#             U[i+1] = 1 + 3*U[i]
#     return U[i+1]
#
# suracuse(15,20)
#
# def suracuse(h, n):
#    u=h
#    for i in range(n):
#        if u % 2 == 0:
#             u = u//2
#        else :
#             u= 1 + 3*u
#    return u
#
# U = suracuse(15,20)
# print(U)
#
#
# #Question 2
# #
# # def suracuse_liste(h, n):
# #     liste_U = [1]*n
# #     liste_U[0]=h
# #     for i in range(n):
# #         if liste_U[i] % 2 == 0:
# #             liste_U[i+1] = liste_U[i]//2
# #         else :
# #             liste_U[i+1] = 1 + 3*liste_U[i]
# #         liste_U.append(liste_U[i+1])
# #     return liste_U
# #
# # U = suracuse_liste(15,20)
# # print(U)
#
# def suracuse_liste(h, n):
#    liste_U =[]
#    u=h
#    for i in range(n):
#        if u % 2 == 0:
#             u = u//2
#        else :
#             u= 1 + 3*u
#        liste_U.append(u)
#    return liste_U
#
# U = suracuse_liste(15,20)
# print(U)
#
#
#
# #Question 3
#
#
# def temps_de_vol(h):
#     liste_U=[1]*20
#     liste_U[0]=h
#     for i in range(20):
#         if liste_U[i] % 2 == 0:
#             liste_U[i+1] = liste_U[i]//2
#             if liste_U[i+1] == 1:
#                 print("Le nombre d'itérations pour atteindre 1 est de :",i+1)
#
#         else :
#             liste_U[i+1] = 1 + 3*liste_U[i]
#             if liste_U[i+1] == 1:
#                 print("Le nombre d'itérations pour atteindre 1 est de :",i+1)
#     return i+1
#
# temps_de_vol(15)
#
#
#
# def temps_de_vol(h):
#     u = h
#     liste_U=[]
#     while u != 1 :
#         if u % 2 == 0:
#             u = u // 2
#         else:
#             u = 1 + 3 * u
#         liste_U.append(u)
#     return len(liste_U)
#
# U = temps_de_vol(15)
# print(U)

#Question 4
# liste_maxT=[]
# def temps_de_vol_max(h):
#     for i in range(1,h):
#         val = temps_de_vol(i)
#         liste_maxT.append(val)
#     return liste_maxT
#
# def max_liste(liste_maxT):
#     maxl = 0
#     maxi = 0
#     for i in range(1,len(liste_maxT)):
#         if liste_maxT[i] > maxl:
#             maxl = liste_maxT[i]
#             maxi = i
#     return (maxl,maxi)
#
# print(temps_de_vol_max(101))
# print(max_liste(liste_maxT))