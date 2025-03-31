#1 Plus grand nombre d'une liste

#1ère méthode

list = [7,5,1,9,3,17,2]
Max = max(list)
print("Le maximum de cette liste est : ",Max)

#2ème méthode

#list = [7,5,1,9,3,17,2]
#pg=list[0]
#for i in range(1,len(list)):
#    if list[i]>pg:
#        pg=list[i]
#print(pg)

#list = str([7,5,1,9,3,17,2])
#list.sort()
#L = len(list)
#print(L)
#print("Le maximum de cette liste est : ",list[L])





#2 Nombre pair et impair dans une liste

#list = [7,5,1,9,3,17,2]
#listP=[]
#listI=[]
#c=0
#print(len(list))
#for i in range(0,len(list)):
#    c=list[i]
#    if (c%2 == 0):
#        listP.append(c)
#    else :
#        listI.append(c)

#print(listP,listI)





#Exercice 3
#from statistics import mean
#list=[]
#Note=1
#while(Note > 0):
#    Note = int(input("Entrez une note :"))
#    if(Note > 0):
#        list.append(Note)
#    print(len(list))
#    print(max(list))
#    print(min(list))
#    print(mean(list))
#print(list)

#Exercice 4

#t1 = [31,28,31,30,31,30,31,31,30,31,30,31]
#t2 = ['Janvier','Février','Mars','Avril','Mai','Juin','Juillet','Aout','Septembre','Octobre', 'Novembre','Décembre']
#j=1

#for i in range(0,12):
#   t2.insert(i+j,t1[i])
#    j+=1
#print(t2)

#Exercice 5


# list = ['paris','melbourne','atlanta','monaco','lyon','vienne','brest','londres','stuttgart','munich','rungis']
#
# lettre = (input("Rentrez une lettre :"))
# lettre.lower()
# Test=''
# find=[]
# cptL = 0
# cptM = 0
#
# for i in range (0,len(list)):
#     for c in list[i]:
#         if c == lettre :
#             cptL += 1
#             if list[i] not in find:
#                 find.append(list[i])
#                 cptM += 1
#
# print("Trouvé",cptL,"fois la lettre :",lettre,"dans",cptM,"mots qui sont les suivants :",find)

#Exercice 6

# list=[1]*1000
# nbr_premier =[]
# print(list)
# np=[]
#
# for i in range(2,len(list)):
#   if list[i] == 1:
#        for j in range(i+1,len(list)):
#           if j%i == 0:
#                list[j] = 0
#
# for k in range(1,len(list)):
#    if list[k] == 1:
#        np.append(k)
# print(np)

#Exercice 7


#Saison 1 - Episode 3

#Exercice 7 "Base de données nom/âge/taille"

#Initialisation du dictionnaire
dico = {}

#Choix de l'utilisateur
print("Quelle action voulez-vous faire ?")

while 1:
    choix = str(input("Choisissez : (R)emplir - (C)onsulter - (T)erminer :"))

    if choix.upper() == "T":
        print("Terminé")
        break

# Premier bloc : remplissage du dictionnaire
    elif choix.upper() == "R":
        print("Remplissage du dictionnaire")
        while 1:
            nom = str(input("Entrez le nom (ou <enter> pour terminer) :"))
            if nom == "":
                break
            age = int(input("Entrez l'âge (nombre entier !) :"))
            taille = float(input("Entrez la taille (en mètres) :"))
            dico[nom] = (age, taille)

# Deuxième bloc : consultation du dictionnaire
    elif choix.upper() == "C":
        print("Consultation du dictionnaire")
        while 1:
            recherche = str(input("Quel nom recherchez-vous ? (<entrer> pour terminer) "))
            if recherche == "":
                break
            if recherche not in dico.keys():
                print("Le nom n'existe pas - Nouvel essai")
            else :
                print("Nom :{} - âge :{} ans - taille :{} m.".format(recherche, dico[recherche][0], dico[recherche][1]))






