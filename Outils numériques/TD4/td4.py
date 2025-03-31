#Exercice 1

# def end():
#     print("Terminé")
#
# def rempl():
#     print("Remplissage du dictionnaire")
#     while 1:
#         nom = str(input("Entrez le nom (ou <enter> pour terminer) :"))
#         if nom == "":
#             break
#         age = int(input("Entrez l'âge (nombre entier !) :"))
#         taille = float(input("Entrez la taille (en mètres) :"))
#         dico[nom] = (age, taille)
#
#     return()
#
# def read():
#     print("Consultation du dictionnaire")
#     while 1:
#         recherche = str(input("Quel nom recherchez-vous ? (<entrer> pour terminer) "))
#         if recherche == "":
#             break
#         if recherche not in dico.keys():
#             print("Le nom n'existe pas - Nouvel essai")
#         else:
#             print("Nom :{} - âge :{} ans - taille :{} m.".format(recherche, dico[recherche][0], dico[recherche][1]))
#
#
# dico = {}
# nom=''
# #Choix de l'utilisateur
#
# print("Quelle action voulez-vous faire ?")
#
# while 1:
#     choix = str(input("Choisissez : (R)emplir - (C)onsulter - (T)erminer :"))
#
#     if choix.upper() == "T":
#         end()
#         break
# # Premier bloc : remplissage du dictionnaire
#     elif choix.upper() == "R":
#         rempl()
# # Deuxième bloc : consultation du dictionnaire
#     elif choix.upper() == "C":
#         read()

#Exercice 2

# Définition de la chaîne de caractères
# def tri():
#     l_av_conv=[]
#     s = 'Quarante-deux, dit Compute-Un, avec infiniment de calme et de majesté.'
#     for x in s:
#         l_av_conv.append(x)
#     l_ap_conv = [ord(x) for x in s]
#     l_ap_conv.sort()
#     print(l_av_conv)
#     print(l_ap_conv)
# tri()

# #Exercice 3
# mot = input("Choisir un mot :")
# césar = int(input("Choisir chiffre de césar :"))
# l = len(mot)
# list_code = []
# list_decode = []
# liste = [ord(x) for x in mot]
# m_decod =0
#
#
# def chif():
#     for i in range(l) :
#         liste[i]=liste[i]-96
#     for j in range(l):
#         liste[j]=(liste[j]+césar)%26
#
#     for h in range(l):
#         liste[h]=liste[h]+96
#     for k in range(l):
#         list_code.append(chr(liste[k]))
#     print(list_code)
#
#
#
# #def dechif(n_list):
# #     for i in range(l):
# #     m_decod = ord(n_list[i])
# #     print(m_decod)
# #     # for p in range(l):
# #     #     n_list[p] = n_list[p] - 96
# #     # for j in range(l):
# #     #     n_list[j] = (n_list[j])%26
# #     # print(n_list)
#
#
#         #print(m_decod)
#         #list_decode.append(chr(m_decod))
# chif()
#
#
#
# #decod(n_list)
#
# #mot="python"
# # def code_cesar(mot,table):
# #     res = ""
# #     for lettre in mot:
# #         code_lettre = ord(lettre)-ord("a")
# #         lettre_cesar = table[code_lettre]
# #         res+=lettre_cesar
# #     return res
# #
# # cesar_3=table(3)
# # test="python"
# # test_chiffre = code_cesar(test,cesar_3)
# print(test_chiffre)

# exercice3 du TDSaison1Episode4

# # fabric du dictionnaire pour le mot
#
def fabricdico(mot):
    for e in mot:
        dic_chiff[e] = chr(((ord(e) - ord('a') + cesar) % 26) + ord('a'))
        print(ord(e))  # code ascii en decimal
        print(chr(ord(e)))

def chiffrermot(mot):
    mot_chiff = ''
    for e in mot:
        mot_chiff += dic_chiff[e]
    print(" le mot chiffre in : ", mot_chiff)
    return mot_chiff


def dechiffrermot(mot_chiff):
    for (c, val) in dic_chiff.items():
        dic_dech[val] = c
    #    dic_dech = dict((val, c) for c, val in dic_chiff.items())

    print("le dico de dechiff : ", dic_dech)

    # for mot in mots_chiff:
    print("coucou ", mot)
    print("coucou ", mot_chiff)
    mot_init = ''
    for e in mot_chiff:
        mot_init += dic_dech[e]
    print("le chiffrement de '{0}' est : {1} ".format(mot_chiff, mot_init))


#programme pricipal

mot = "python"

dic_chiff = {}  # dictionnaire de chiffrement
dic_dech = {}  # dictionnaire de dechiffrement
cesar = int(input("Donner le chiffre de César (<26) :"))
if cesar < 26 and cesar > 0:
    fabricdico(mot)
    mot_chiffre = chiffrermot(mot)
    print(" le mot chiffre out : ", mot_chiffre)
    dechiffrermot(mot_chiffre)
else:
    print("Merci d'introduire un nombre <26 et >0 !")
    cesar = 1  # valeur par defaut