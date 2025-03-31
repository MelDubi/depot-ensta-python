# Melvin Dubée FIPA 2024 Code Examen Pratique de Traitement Numérique des Images
import numpy as np
import cv2
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
from OutilsTNI import divide
from OutilsTNI import formate_resultat
import numpy as np
from skimage import feature
from sklearn.cluster import KMeans



# Exercice 1

# Détection et dénombrement d’éoliennes

# 1. Lecture de l’image « Eoliennes_1m.jpg » et conversion en niveaux de gris. Soit
# eole_gray cette image

eole_gray = cv2.imread('/Users/melvindubee/iCloud Drive (archives)/Documents/ENSTA/Traitement-image/data/Eoliennes_1m.jpg', 0)
plt.figure()
plt.imshow(eole_gray, cmap='gray'), plt.title('Eoliennes_1m'), plt.xlabel('indice colonne n'), plt.ylabel(
    'indice ligne m')
plt.show()

# 2. Binarisation

#Question.1
# binariser eole_gray par une méthode pertinente. Reporter en commentaires la valeur du seuil retenu et la justifier

seuil = 250

ret, eole_binaire = cv2.threshold(eole_gray, seuil, 255, cv2.THRESH_BINARY_INV)
plt.figure()
plt.imshow(eole_binaire, cmap="gray")
plt.title("Image binaire")
plt.show()

# On peut retenir deux valeurs de seuil en fonction de ce que l'on veut :

# -seuil à 250 si l'on essaye de dénombrer le nombre d'éolienne au premier plan (ici 4), avec ce seuil
# on isole bien de l'image les éoliennes.

# -seuil à 200 si l'on essaye de dénombrer toutes les éoliennes, c'est à dire celles au premier plan mais également
# celles qui se situent à l'arrière plan (8 en tout).

#Question.2
# sauvegarder l’image binaire sous « eole_binaire.jpg »
cv2.imwrite("eole_binaire.jpg", eole_binaire)

#Question.3
# Préfiltrer l’image eole_gray par un filtre gaussien de taille 5x5 ou 7x7

# Filtrage Gaussien

taille = 7
img_gauss = cv2.GaussianBlur(eole_gray,(taille, taille),0)
img_gauss2 = cv2.GaussianBlur(eole_gray,(taille, taille),4,4, cv2.BORDER_DEFAULT)
plt.figure()
plt.subplot(121)
plt.imshow(img_gauss, cmap='gray')
plt.title("Filtre Gaussien")
plt.subplot(122)
plt.imshow(img_gauss, cmap='gray')
plt.title("Filtre Gaussien 2")
plt.show()

#Question.4
# binariser l’image de la question c.

seuil = 250

ret, img_gauss_bin = cv2.threshold(img_gauss, seuil, 255, cv2.THRESH_BINARY_INV)
plt.figure()
plt.imshow(img_gauss_bin, cmap="gray")
plt.title("Image gauss binaire")
plt.show()

#Question.5
#Selon vous, y-a-t-il un intérêt à préfiltrer cette image avant de la binariser et pourquoi ?

# Dans notre cas ici un va flouter l'image avec le filtre gaussien ce qui va permettre de lisser l'image
# et donc de réduire le bruit présent sur l'image de départ. Finalement flouter cette image permet de simplifier
# l'image en général avant de faire d'autre opération sur celle-ci comme ici la binarisation.

#Question.6
# Remplacer le filtre gaussien par un filtre médian de taille appropriée. Quelles différences observez-vous ?

# Filtrage non-linéaire Median

taille= 7
img_median = cv2.medianBlur(eole_gray, taille)
plt.figure()
plt.imshow(img_median, cmap='gray')
plt.title("Image après Median")

plt.show()

# binarisation
seuil = 250

ret, img_median_bin = cv2.threshold(img_median, seuil, 255, cv2.THRESH_BINARY_INV)
plt.figure()
plt.imshow(img_median_bin, cmap="gray")
plt.title("Image median binaire")
plt.show()

# Si je reste au même seuil de 250 pour dénombrer les éoliennes du premier, je remarque que le filtre
# Median est plus efficace puisqu'il enlève plus d'impureté de l'image pour un même seuil.


# Post-traitement

#Question.1
# afin d’améliorer la qualité de l’image binaire, appliquer un traitement morphologique pertinent, en considérant un
#é́lément structurant compact, à l’image obtenue en 2.a ou en 2.d

ksize = 3
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (ksize, ksize))

erode = cv2.erode(eole_binaire, kernel)
dilate = cv2.dilate(eole_binaire, kernel)
opening = cv2.dilate(erode, kernel)
closing = cv2.erode(dilate, kernel)
open_closing = cv2.erode(cv2.dilate(opening, kernel), kernel)

plt.figure()
plt.subplot(331)
plt.imshow(eole_binaire, cmap='gray')
plt.title("Image binaire")
plt.subplot(332)
plt.imshow(erode, cmap='gray')
plt.title("Érosion")
plt.subplot(333)
plt.imshow(dilate, cmap='gray')
plt.title("Dilatation")
plt.subplot(334)
plt.imshow(opening, cmap='gray')
plt.title("Ouverture")
plt.subplot(335)
plt.imshow(closing, cmap='gray')
plt.title("Fermeture")
plt.subplot(336)
plt.imshow(open_closing, cmap='gray')
plt.title("Ouverture-Fermeture")
plt.show()

#Question.2
# Critiquer le résultat obtenu, l’expliquer et conclure sur la pertinence de ce traitement.

# On peut faire différent commentaire sur chacunes des images obtenues :

# Tout d'abord l'érosion nous permet de bien combler les trous dans l'image
# on arrive facilement à distinguer les éoliennes après ce traitement

# Après dilatation on a carrément isoler les 4 éoliennes et surtout éliminé
# le point noir du dôme de l'image qui restait à chaque filtrage. Pour avoir un meilleur rendu
# pour mieux distinguer les éoliennes, peut-être changer le seuil de départ.

# Les trois dernières images (Ouverture, Fermeture, les deux combinées) montrent qu'il y a un choix à faire
# entre distinguer les éoliennes et leur pâles mais avoir le point noir du dôme ou bien
# ne pas parfaitement distinguer les pâles mais ne pas avoir le point du dôme.


# Question.3

ksize = 6
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (ksize, ksize))

opening = cv2.morphologyEx(eole_binaire, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(eole_binaire, cv2.MORPH_CLOSE, kernel)
morph_grad = cv2.morphologyEx(eole_binaire, cv2.MORPH_GRADIENT, kernel)
morph_tophat = cv2.morphologyEx(eole_binaire, cv2.MORPH_TOPHAT, kernel)
morph_blackhat = cv2.morphologyEx(eole_binaire, cv2.MORPH_BLACKHAT, kernel)

plt.figure()
plt.subplot(331)
plt.imshow(eole_binaire, cmap='gray')
plt.title("Image binaire")
plt.subplot(332)
plt.imshow(opening, cmap='gray')
plt.title("Ouverture")
plt.subplot(333)
plt.imshow(closing, cmap='gray')
plt.title("Fermeture")
plt.subplot(334)
plt.imshow(morph_grad, cmap='gray')
plt.title("Gradient morphologique")
plt.subplot(335)
plt.imshow(morph_tophat, cmap='gray')
plt.title("Top hat")
plt.subplot(336)
plt.imshow(morph_blackhat, cmap='gray')
plt.title("Black hat")
plt.show()

# Question.4
# d. comparer le résultat obtenu en c) avec celui obtenu en a) et conclure. Sauvegarder l’image post-traitée la plus
#propre sous « eole_posttraitee.jpg »

# On voit qu'après ce dernier traitement l'image du gradient morphologique fait bien ressortir les éoliennes mais
# également le dôme ce qui pose soucis. L'image la plus intéressante ici est Black hat, le dôme est minime et le bruit
# inexistant, les éoliennes sont plus visibles sur cette image. Cette image est la différence entre l'image obtenue
# après la fermeture et l'image d'entrée. Cette opération met en évidence les zones sombres qui sont plus petites
# que l'élément structurant.

cv2.imwrite("eole_posttraittee.jpg", morph_blackhat)

# Question.5
# déterminer automatiquement le nombre d’éoliennes et l’indiquer dans votre code. Ce nombre est -il celui attendu ?
# Dans le cas contraire, expliquez d’où peuvent venir les erreurs

# On va chercher à etiqueter en composantes connexes l’image binaire obtenue de la question précédente
num_features, comp_conn = cv2.connectedComponents(morph_grad)
print("Nombre d'éoliennes: ", num_features-1)

plt.figure()
plt.imshow(comp_conn, cmap='jet')
plt.title("Composantes connexes")
plt.show()

# On voit que sur l'image de composantes connexes que j'ai affiché
# il reste énomément de bruit dans le bas de l'image, cela n'a pas été enlevé par
# les filtres appliqués. Il aurait été peut-être nécessaire en post-traitement de
# segmenter l'image en deux régions, l'herbe et le ciel et les éoliennes. On trouve 139
# puisque la fonction connectedComponents d'OpenCV est utilisée pour étiqueter les composantes connexes d'une image
# binaire. En d'autres termes, elle identifie et étiquette les groupes de pixels connectés ayant la même intensité
# (généralement des pixels blancs) dans une image binaire, ici c'est le cas pour l'herbe.

# Comparaison

# Affichage de l'image en niveaux de gris
eole_gray2 = cv2.imread('/Users/melvindubee/iCloud Drive (archives)/Documents/ENSTA/Traitement-image/data/Eoliennes_2m.jpg', 0)
plt.figure()
plt.imshow(eole_gray, cmap='gray'), plt.title('Eoliennes_2m'), plt.xlabel('indice colonne n'), plt.ylabel(
    'indice ligne m')
plt.show()

# Binarisation de l'image

seuil = 210

ret, eole_binaire2 = cv2.threshold(eole_gray2, seuil, 255, cv2.THRESH_BINARY_INV)
plt.figure()
plt.imshow(eole_binaire2, cmap="gray")
plt.title("Image binaire")
plt.show()

# Filtrage Gaussien

taille = 7
img_gauss3 = cv2.GaussianBlur(eole_gray2,(taille, taille),0)
img_gauss4 = cv2.GaussianBlur(eole_gray2,(taille, taille),4,4, cv2.BORDER_DEFAULT)
plt.figure()
plt.subplot(121)
plt.imshow(img_gauss3, cmap='gray')
plt.title("Filtre Gaussien 3")
plt.subplot(122)
plt.imshow(img_gauss4, cmap='gray')
plt.title("Filtre Gaussien 4")
plt.show()

# Binarisation + filtre gaussien

seuil = 210

ret, img_gauss_bin2 = cv2.threshold(img_gauss3, seuil, 255, cv2.THRESH_BINARY_INV)
plt.figure()
plt.imshow(img_gauss_bin2, cmap="gray")
plt.title("Image gauss binaire")
plt.show()

# Filtrage non-linéaire Median

taille= 7
img_median2 = cv2.medianBlur(eole_gray2, taille)
plt.figure()
plt.imshow(img_median2, cmap='gray')
plt.title("Image après Median")

plt.show()

# binarisation
seuil = 210

ret, img_median_bin2 = cv2.threshold(img_median2, seuil, 255, cv2.THRESH_BINARY_INV)
plt.figure()
plt.imshow(img_median_bin2, cmap="gray")
plt.title("Image median binaire 2")
plt.show()

# Element structurant compacte

ksize = 3
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (ksize, ksize))

erode = cv2.erode(img_median_bin2, kernel)
dilate = cv2.dilate(img_median_bin2, kernel)
opening = cv2.dilate(erode, kernel)
closing = cv2.erode(dilate, kernel)
open_closing = cv2.erode(cv2.dilate(opening, kernel), kernel)

plt.figure()
plt.subplot(331)
plt.imshow(img_median_bin2, cmap='gray')
plt.title("Image binaire")
plt.subplot(332)
plt.imshow(erode, cmap='gray')
plt.title("Érosion")
plt.subplot(333)
plt.imshow(dilate, cmap='gray')
plt.title("Dilatation")
plt.subplot(334)
plt.imshow(opening, cmap='gray')
plt.title("Ouverture")
plt.subplot(335)
plt.imshow(closing, cmap='gray')
plt.title("Fermeture")
plt.subplot(336)
plt.imshow(open_closing, cmap='gray')
plt.title("Ouverture-Fermeture")
plt.show()

# Traitement morphologique

ksize = 6
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (ksize, ksize))

opening = cv2.morphologyEx(img_median_bin2, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img_median_bin2, cv2.MORPH_CLOSE, kernel)
morph_grad = cv2.morphologyEx(img_median_bin2, cv2.MORPH_GRADIENT, kernel)
morph_tophat = cv2.morphologyEx(img_median_bin2, cv2.MORPH_TOPHAT, kernel)
morph_blackhat = cv2.morphologyEx(img_median_bin2, cv2.MORPH_BLACKHAT, kernel)

plt.figure()
plt.subplot(331)
plt.imshow(img_median_bin2, cmap='gray')
plt.title("Image binaire")
plt.subplot(332)
plt.imshow(opening, cmap='gray')
plt.title("Ouverture")
plt.subplot(333)
plt.imshow(closing, cmap='gray')
plt.title("Fermeture")
plt.subplot(334)
plt.imshow(morph_grad, cmap='gray')
plt.title("Gradient morphologique")
plt.subplot(335)
plt.imshow(morph_tophat, cmap='gray')
plt.title("Top hat")
plt.subplot(336)
plt.imshow(morph_blackhat, cmap='gray')
plt.title("Black hat")
plt.show()

# Composantes connexes

num_features, comp_conn = cv2.connectedComponents(morph_grad)
print("\n Nombre d'éoliennes image 2: ", num_features-1)

plt.figure()
plt.imshow(comp_conn, cmap='jet')
plt.title("Composantes connexes image 2")
plt.show()

# On a bien meilleur résultat pour l'image des composantes connexes. Je n'ai pas réussi à trouver
# Un bon seuil au départ ce qui explique le résultat de 48. Le filtre gaussien ne me paraît pas plus efficace
# pour avoir un meilleur résultat. Mais le filtre médian est très utilse pour cette image et permet de descendre le
# résultat obtenu. Si j'augmente le seuil ma valeur augmente et si je descend la valeur diminue mais ce ne sont
# pas les éoliennes qui sont dénombrées.

# Quelle autre approche pourrait être adoptée pour améliorer les résultats

# Une détection des contours serait à adopter pour encore mieux isoler les éoliennes.
# Pour cela un filtre de Canny serait utilisé.

# Exercice 2 : Analyse de la végétation


I1 = cv2.imread('/Users/melvindubee/iCloud Drive (archives)/Documents/ENSTA/Traitement-image/data/I1.jpg', 0)
plt.figure()
plt.imshow(eole_gray, cmap='gray'), plt.title('I1'), plt.xlabel('indice colonne n'), plt.ylabel(
    'indice ligne m')
plt.show()

I2 = cv2.imread('/Users/melvindubee/iCloud Drive (archives)/Documents/ENSTA/Traitement-image/data/I2.jpg', 0)
plt.figure()
plt.imshow(eole_gray, cmap='gray'), plt.title('I2'), plt.xlabel('indice colonne n'), plt.ylabel(
    'indice ligne m')
plt.show()

I3 = cv2.imread('/Users/melvindubee/iCloud Drive (archives)/Documents/ENSTA/Traitement-image/data/I3.jpg', 0)
plt.figure()
plt.imshow(eole_gray, cmap='gray'), plt.title('I3'), plt.xlabel('indice colonne n'), plt.ylabel(
    'indice ligne m')
plt.show()

# Génération des deux classes
Class1 = divide(I1,128)
Class2 = divide(I2,128)
Class3 = divide(I3,128)

# Définition des n imagette
n = 24 # imagette n d'une classe (n doit être entre 1 et la longueur de Class1 et Class2, soit 25 ici)

plt.figure()
plt.subplot(221)
plt.imshow(Class1[n],cmap='gray')
plt.title('imagette %d issue de I1'%n)
plt.subplot(222)
plt.imshow(Class2[n],cmap='gray')
plt.title('imagette %d issue de I2'%n)
plt.subplot(223)
plt.imshow(Class3[n],cmap='gray')
plt.title('imagette %d issue de I3'%n)

# Matrices de co-occurence
glcm1=[]
glcm2=[]
glcm3=[]
for patch in Class1:
    glcm1.append(feature.graycomatrix(patch, distances=[1],
          angles=[0,np.pi/4], levels=256,
          symmetric=True, normed=True))
for patch in Class2:
    glcm2.append(feature.graycomatrix(patch, distances=[1],
                 angles=[0, np.pi / 4], levels=256,
                 symmetric=True, normed=True))
for patch in Class3:
    glcm3.append(feature.graycomatrix(patch, distances=[1],
                 angles=[0, np.pi / 4], levels=256,
                 symmetric=True, normed=True))

# Visualisations des matrices
plt.figure()
plt.imshow(glcm1[n][:,:,0,0],cmap='jet')
plt.title('glcm1 pour theta=0 deg')
plt.colorbar()
plt.figure()
plt.imshow(glcm1[n][:,:,0,1],cmap='jet')
plt.title('glcm1 pour theta=45 deg')
plt.colorbar()

plt.figure()
plt.imshow(glcm2[n][:,:,0,0],cmap='jet')
plt.title('glcm2 pour theta=0 deg')
plt.colorbar()
plt.figure()
plt.imshow(glcm2[n][:,:,0,1],cmap='jet')
plt.title('glcm2 pour theta=45 deg')
plt.colorbar()

plt.figure()
plt.imshow(glcm3[n][:,:,0,0],cmap='jet')
plt.title('glcm3 pour theta=0 deg')
plt.colorbar()
plt.figure()
plt.imshow(glcm3[n][:,:,0,1],cmap='jet')
plt.title('glcm3 pour theta=45 deg')
plt.colorbar()

# Paramètres d'Haralick
x1 = np.zeros((6,len(Class1)))
for i,patch in enumerate(Class1):
    glcm = feature.graycomatrix(patch, distances=[1], angles=[0],
          levels=256, symmetric=True, normed=True)
    x1[0,i]=feature.graycoprops(glcm, 'contrast')[0, 0] # Contrast
    x1[1,i]=feature.graycoprops(glcm, 'homogeneity')[0, 0] # Homogénéité
    x1[2,i]=feature.graycoprops(glcm, 'dissimilarity')[0, 0]
    x1[3,i]=feature.graycoprops(glcm, 'ASM')[0, 0]
    x1[4,i]=feature.graycoprops(glcm, 'energy')[0, 0] # Uniformité de l'énergie
    x1[5,i]=feature.graycoprops(glcm, 'correlation')[0, 0] # Corrélation
plt.figure()

# Paramètres d'Haralick
x2 = np.zeros((6,len(Class2)))
for i,patch in enumerate(Class2):
    glcm2 = feature.graycomatrix(patch, distances=[1], angles=[0],
          levels=256, symmetric=True, normed=True)
    x2[0,i]=feature.graycoprops(glcm2, 'contrast')[0, 0] # Contrast
    x2[1,i]=feature.graycoprops(glcm2, 'homogeneity')[0, 0] # Homogénéité
    x2[2,i]=feature.graycoprops(glcm2, 'dissimilarity')[0, 0]
    x2[3,i]=feature.graycoprops(glcm2, 'ASM')[0, 0]
    x2[4,i]=feature.graycoprops(glcm2, 'energy')[0, 0] # Uniformité de l'énergie
    x2[5,i]=feature.graycoprops(glcm2, 'correlation')[0, 0] # Corrélation
plt.figure()

# Paramètres d'Haralick
x3 = np.zeros((6,len(Class3)))
for i,patch in enumerate(Class3):
    glcm3 = feature.graycomatrix(patch, distances=[1], angles=[0],
          levels=256, symmetric=True, normed=True)
    x3[0,i]=feature.graycoprops(glcm3, 'contrast')[0, 0] # Contrast
    x3[1,i]=feature.graycoprops(glcm3, 'homogeneity')[0, 0] # Homogénéité
    x3[2,i]=feature.graycoprops(glcm3, 'dissimilarity')[0, 0]
    x3[3,i]=feature.graycoprops(glcm3, 'ASM')[0, 0]
    x3[4,i]=feature.graycoprops(glcm3, 'energy')[0, 0] # Uniformité de l'énergie
    x3[5,i]=feature.graycoprops(glcm3, 'correlation')[0, 0] # Corrélation
plt.figure()




