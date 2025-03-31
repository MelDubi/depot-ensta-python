#1 Pair ou Impair

# n = int(input("Entrez un nombre :"))
#
# if (n%2 == 0):
#     print("n est pair")
# else :
#     print("n est impair")




#2 Nombre de division par 2

#nb = int(input("Saisir un nombre :"))
# i =0
#
# while nb % 2 == 0:
#     nb=nb//2
#     i+=1
#
# print(i)

#print("Nombre de division par 2 : ",i)

# entier_utilisateur = 28
# entier_utilisateur_sauvegarde = entier_utilisateur # pour l'affichage
# compteur_de_divisions = 0
# while entier_utilisateur % 2 == 0:
#     entier_utilisateur = entier_utilisateur // 2
#     compteur_de_divisions += 1 # permet d'écrire plus vite compteur_de_divisions = compteur_de_divisions + 1
#
# print(entier_utilisateur_sauvegarde, "est divisible", compteur_de_divisions, "fois par 2")




#3 Table de 7 et divisible de 3

# for i in range(1,20):
#     table = 7*i
#     if table%3 == 0:
#         print(table,end=" * \n") #ou print(" ") pour le retour à la ligne
#         #print(" ")
#     else :
#         print(table)





#4 nombre de factorielle de 1000


# fact_max = 1000
# facto = 1
# while fact_max > 1:
#     facto *= fact_max
#     fact_max -= 1
#
# print(facto)
# # Pas très élégant
# facto_en_chaine = str(facto)
# print("Le nombre de chiffres de factorielle 1000 est", len(facto_en_chaine))




#5 Suite de Fibonacci

# x = 0
# y = 1
#
# while(y<267914296):
#    z = x + y
#    x = y
#    y = z
#    print("Valeur de la suite :",y)





#6 Calcul de PI méthode itérative

# s = 0
# u = 0
# for i in range (100001):
#    u = 8*(-1)**i/((2*i+1)*(2*i+3))
#    s += u
#
# Valeur = (s+4)/2
# print("Valeur :",Valeur)





#7 Compteur de caractères dans string

# var = input("Saisir des caractères : ")
# string = var.lower()
# cpt = 0
# for c in string:
#   if c == "y" :
#        cpt += 1
# print(string)
# print("Trouvé",cpt,"y")






#8 Chaine de caractère inversé

# var = input("Saisir des caractères : ")
# chaine = ''
# for i in range(len(var)):
#    chaine += var[len(var)-1-i]
#
# print(chaine)















