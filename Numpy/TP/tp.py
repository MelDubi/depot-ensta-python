import numpy as np
import numpy.linalg as npla
import matplotlib.pyplot as plt
import matplotlib.colors as mcol
import matplotlib.ticker as mtick
from matplotlib import cm
import matplotlib.patches as patches
#
# ######### Partie 1 #####################
#

# A = np.array([1, 0, 87, 23, 0 , 6])
# print(A)
# print(A[1])
# print(A[0])
# print(A[-1])
# print(A.size)
# print(A.shape)
# print(A[5])
#
# B = np.array([[1, 0], [87, 23], [0 ,6]])
# print(B)
# print(B[0])
# print(B[0, 1])
# print(B[-1, 0])
# print(B[:, 1])
# print(B.size)
# print(B.shape)

# n=2
# m=3
#
# C = np.zeros((n, m))
#
# print(C)
#
# D = B @ C
# print(D)
# #
# L = np.array([0, 8, 9, 3])
# A = np.array([5, 4, 1, 2])
# ratio_LA = L / A
# A_carre = A**2
# prod_AL = A * L
#
# print(prod_AL)

# A = np.arange(16).reshape((4, 4))
# X = np.array([5, 4, 1, 2])
# print(A)
# print(X)
# B = A @ X
# print(B)
# print(A)

# A = np.arange(16).reshape((4, 4))
# X = np.array([5, 4, 1, 2])
# print(A.T)
# print(X.T)
# #
# #
# # #
# # # import time
# # #
# # #
# # # def average(a):
# # #     """
# # #     Compute the average value of ``a``
# # #
# # #     Parameters
# # #     ----------
# # #     a : ndarray
# # #         Input array.
# # #
# # #     Returns
# # #     -------
# # #     avg : int
# # #         The average value of ``a``
# # #     """
# # #
# # #     average = 0
# # #     for i in range(a.shape[0]):
# # #         average += a[i]
# # #     return average/a.shape[0]
# # #
# # #
# # # if __name__ == "__main__":
# # #     rand_array_1 = np.random.randint(0, 10000, 10000)
# # #
# # #     t0 = time.perf_counter_ns()
# # #     average_value = average(rand_array_1)
# # #     print(time.perf_counter_ns() - t0)
# # #
# # #     t0 = time.perf_counter_ns()
# # #     average_value = np.mean(rand_array_1)
# # #     print(time.perf_counter_ns() - t0)
# #
# foo = np.random.randint(0, 10, (np.random.randint(50, 60), np.random.randint(42, 69)))
# #
#foo2= foo.astype(np.float)
#print(foo2)
#print(foo)
#loc = np.where(foo<5)
#foo2 = np.where(foo<5,foo,0)
#foo3 = 2*foo2
#print(foo3)
# print(foo)
#print(foo2)
# bar = foo[:, 0:13:1]
# bar_copy = foo[:, 0:13:2].copy()
#
#
# print(bar)
# print(bar.shape)
# print("")
# print(bar_copy)
# foo[5,6]=42
# bar_copy = foo[:, 0:13:2].copy()
# baz = foo[4:14,(1,6,11,26)]
# print(baz)
# print(baz.shape)
#
# foo[5,6]=42
#
# print(foo[5,6])
# print(bar[5,3])
# print(baz[1,1])
#
# #Exercice 3
#
short_sides = np.random.randint(1, 10, (200,2))

print(short_sides)
print(short_sides.shape)

hypotenus = np.sqrt(short_sides[:,0]**2+short_sides[:,1]**2)

cos1 = np.arccos(short_sides[:,0]/hypotenus)
sin1 = np.arcsin(short_sides[:,1]/hypotenus)
tan1 = np.arctan(short_sides[:,1]/short_sides[:,0])

triangle = np.column_stack((short_sides,hypotenus,cos1,sin1,tan1))

print(np.all(cos1 == sin1))
print(np.all(cos1 == tan1))
print(np.all(sin1 == tan1))
print(np.any(cos1 == sin1))
#
#
# #Exercice 4
#
# #Partie 1
# # A = np.array([[8,2,1,1,5],[1,9,1,3,2],[3,5,42,28,5],[1,9,1,-50,12],[6,5,3,12,-38]])
# # B = np.array([[42],[12],[28],[90],[32]])
# # A=A.reshape(5,5)
# #
# # print('rang de A :',npla.matrix_rank(A))
# #
# # valp,vectp = npla.eig(A)
# # P = vectp
# # D = np.diag(valp)
# #
# # P2=npla.inv(P)
# # A2 = np.dot(P,D)
# # A3 = np.dot(A2,P2)
# #
# # print(np.allclose(A,A3))
# #
# # X = npla.solve(A,B)
# # B1 = np.dot(A,X)
# # print(X)
# # print(np.allclose(B,B1))
#
#
#
#
#
# ######### Partie 2 #####################
#
# import numpy as np
# import matplotlib.pyplot as plt
#
# X = np.linspace(0, 10, 100) # 100 points entre 0 et 10
# plt.plot(X, np.sin(X))
# plt.ylabel('Ordonnée')
# plt.xlabel('Abscisse')
# plt.show()
#
# #Exercice 5
#
# # # Les bases
# # X = np.linspace(0, 10, 100) # 100 points entre 0 et 10
# # X=np.arange(0,4*np.pi,1e-4) # Pour représenter sur 2 péridoes avec un pas de 10-4
# # plt.plot(X, np.sin(X),label="sinus")
# # plt.plot(X, np.cos(X),label="cosinus",color="r")
# # #plt.legend()
# # plt.xlabel("Temps")
# # plt.ylabel("Amplitude")
# # plt.title("Représentation d'un sinus")
# #
# # plt.show()
#
#
#
# #Exercice 6
#
# Pm=[1.0, 1.02, 1.05, 1.07, 1.1, 1.12, 1.15, 1.18, 1.2, 1.23, 1.26, 1.29, 1.32, 1.35, 1.38, 1.42, 1.45, 1.48, 1.52, 1.56, 1.59, 1.63, 1.67, 1.71, 1.75, 1.79, 1.83, 1.87, 1.92, 1.96, 2.01, 2.06, 2.1, 2.15, 2.21, 2.26, 2.31, 2.36, 2.42, 2.48, 2.54, 2.6, 2.66, 2.72, 2.78, 2.85, 2.92, 2.98, 3.05, 3.13, 3.2, 3.27, 3.35, 3.43, 3.51, 3.59, 3.68, 3.76, 3.85, 3.94, 4.04, 4.13, 4.23, 4.33, 4.43, 4.53, 4.64, 4.75, 4.86, 4.98, 5.09, 5.21, 5.34, 5.46, 5.59, 5.72, 5.86, 5.99, 6.14, 6.28, 6.43, 6.58, 6.73, 6.89, 7.05, 7.22, 7.39, 7.56, 7.74, 7.92, 8.11, 8.3, 8.5, 8.7, 8.9, 9.11, 9.33, 9.55, 9.77, 10.0]
# Po=[2.51, 2.75, 3.71, 2.28, 2.13, 1.92, 4.28, 2.31, 3.31, 1.77, 4.32, 2.25, 5.5, 2.31, 2.83, 3.72, 2.63, 6.28, 6.08, 6.91, 6.89, 3.22, 4.29, 5.87, 4.7, 4.49, 5.24, 6.84, 8.54, 6.83, 8.94, 11.2, 7.66, 12.65, 7.52, 14.32, 13.53, 10.69, 5.93, 15.08, 18.23, 20.04, 12.13, 18.32, 21.33, 15.16, 12.49, 10.88, 22.25, 15.39, 20.57, 14.61, 30.77, 19.6, 33.46, 26.79, 41.86, 53.54, 40.62, 48.61, 64.58, 33.77, 81.54, 62.5, 79.17, 94.5, 133.09, 83.2, 83.37, 182.57, 186.02, 196.24, 123.59, 178.63, 325.9, 213.13, 446.09, 599.6, 363.89, 505.19, 909.76, 596.79, 1063.83, 1335.95, 1521.91, 787.45, 1856.59, 2884.75, 2633.02, 1564.78, 3285.46, 4193.35, 4748.44, 4035.98, 5373.65, 6705.32, 15623.23, 19650.54, 23973.92, 27795.41]
#
# #Phenomene représenté simplement
#
# plt.subplot(211)
# plt.plot(Pm, Po,label="phenomene")
# plt.legend()
# plt.xlabel("Voiture")
# plt.ylabel("Accident")
# plt.title("Représentation des accidents")
#
# #Echelle semi-logarithmique
#
# plt.subplot(212)
# plt.semilogy(Pm,Po) #semi logarithmique en y
# plt.grid()

#
# # Subplot et graduations numériques
#
# #1ere méthode Horizontale
# #
# fig, axs = plt.subplots(1,2)
# fig.suptitle('Subplot horizontal')
# axs[0].plot(Pm)
# axs[1].plot(Po)
# #
# # #Sans les abscisses horizontales
# #
# for ax in axs.flat:
#     ax.label_outer()

#
#
# #2eme méthode Horizontale
# fig, (ax1,ax2) = plt.subplots(1,2)
# fig.suptitle('Subplot horizontal')
# ax1.plot(Pm)
# ax2.plot(Po)
# # plt.show()
#
# #1ere méthode verticale
# #
# # fig, axs = plt.subplots(2)
# # fig.suptitle('Subplot horizontal')
# # axs[0].plot(Pm)
# # axs[1].plot(Po)
# #
# # #Sans les abscisses horizontales
# #
# # for ax in axs.flat:
# #      ax.label_outer()
# # plt.show()
#
# #2eme méthode verticale
# # fig, (ax1,ax2) = plt.subplots(2)
# # fig.suptitle('Subplot vertical')
# # ax1.plot(Pm,Po)
# # ax1.label_outer()
# # ax2.plot(Pm,Po)
# # plt.show()
#
#
#
#
#
# # Exercice 7
#
# cons =[1.03, 1.01, 1.03, 1.05, 1.03, 1.21, 1.25, 1.22, 1.24, 1.24, 1.68, 1.66, 1.69, 1.69, 1.62, 2.19, 2.3, 2.2, 2.36, 2.12, 3.14, 3.13, 2.94, 3.25, 3.19, 3.86, 3.95, 4.09, 4.11, 4.28, 5.01, 5.01, 4.95, 5.01, 5.17, 6.91, 6.99, 6.31, 6.14, 6.17, 8.71, 8.5, 8.96, 7.75, 8.18, 10.79, 9.68, 9.93, 10.39, 10.44, 11.04, 11.49, 11.38, 11.44, 12.0, 13.41, 15.08, 13.69, 14.04, 15.07, 15.51, 15.43, 15.58, 15.54, 17.46]
# speed = np.arange(5,126,10)
# tab = np.reshape(cons,(13,5))
#
# #moy  = np.mean(tab,axis=0) #moyenne des colonnes
# cons_moy  = np.mean(tab,axis=1) #moyenne des lignes
#
# #Utilisation de polyfit pour une équation d'ordre 2
# a, b, c = np.polyfit(speed, cons_moy, 2)
# cons_fit= a * speed**2 + b * speed + c
#
# plt.plot(speed, cons_moy,'.',label="Consommation")
# plt.plot(speed, cons_fit, label="Polynôme d'ordre 2 ajusté")
# plt.xlabel("Vitesse")
# plt.ylabel("Consommation")
# plt.title("Représentation de la consommation en fonction de la vitesse")
# plt.show()

##Exercice 8

# def somme_cos_sin(X, Y):
#     return np.cos(X) + np.sin(Y)
#
# x = np.linspace(-np.pi , np.pi, 100)
# y = np.linspace(- np.pi / 2 , 3 / 2 * np.pi, 100)
#
# XX, YY = np.meshgrid(x, y)
# cos_sin = somme_cos_sin(XX, YY)
# plt.imshow(cos_sin, extent=[np.min(x), np.max(x), np.min(y), np.max(y)])
# plt.colorbar(label="valeur de z")
# contours = plt.contour(XX, YY, cos_sin, colors="black")
# plt.clabel(contours)
# plt.xlabel("x")
# plt.ylabel("y")
# plt.title("z = cos(x) + sin(y)")
# plt.show()

# Exercice 9
#
# def facteur_amplification(beta, epsilon):
#     return 1 / np.sqrt((1 - beta**2)**2 + 4 * epsilon**2 * beta**2)
#
# Beta = np.linspace(0, 2*np.sqrt(2), 1000)
# for epsilon in (0, 0.1, 0.2):
#     plt.plot(Beta, facteur_amplification(Beta, epsilon), label=str(epsilon))
#
# plt.plot([0, 2], [1, 1], color="black")
# plt.plot([np.sqrt(2), np.sqrt(2)], [0, 8], color="black")
# plt.plot([1, 1], [1, 8], color="black")
#
# plt.legend(title=r"Valeurs de $\epsilon$")
# plt.ylim(0, 8)
# plt.xlim(0, np.max(Beta))
# plt.xlabel(r"$\frac{\omega}{\omega_0}$")
# plt.ylabel("Facteur d'amplification dynamique")
#
# plt.text(0.2, 6, "Amplification\ndynamique")
# ax = plt.gca()
# p1 = patches.FancyArrowPatch((0, 5.8), (np.sqrt(2), 5.8),
#                              arrowstyle='<->', mutation_scale=20)
# ax.add_patch(p1)
# plt.text(1.7, 6, "Atténuation\nvibratoire")
# p1 = patches.FancyArrowPatch((np.sqrt(2), 5.8), (2.5, 5.8),
#                              arrowstyle='<-', mutation_scale=20)
# ax.add_patch(p1)
#
# plt.annotate("Réponse statique\n"+r"sous l'effort $F_0$", xy=(0, 1),
#              xytext=(0.05, 2), arrowprops=dict(arrowstyle='->'))
#
# plt.annotate(r"$\frac{w}{w_0} = \sqrt{2}$", xy=(np.sqrt(2), 2),
#              xytext=(1.6, 2.1), arrowprops=dict(arrowstyle='->'))
#
# plt.title("Atténuation vibratoire par suspensions élastiques")
plt.show()

