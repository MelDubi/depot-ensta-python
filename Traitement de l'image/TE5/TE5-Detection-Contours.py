import numpy as np
import cv2
from matplotlib import pyplot as plt


# 1. Image gris
img = cv2.imread('/Users/melvindubee/Documents/ENSTA/Traitement-image/DATA_TE5/Bateau2.jpg')
img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.figure()
plt.imshow(img_grey, cmap="gray")
plt.title("Image en gris")

# 2 & 3. Calculer le gradient horizontal et vertical

laplacian = cv2.Laplacian(img_grey,cv2.CV_64F)
sobelx = cv2.Sobel(img_grey,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(img_grey,cv2.CV_64F,0,1,ksize=5)

plt.figure()
plt.subplot(2,2,1),plt.imshow(img_grey,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

# 4. Calculer le module du gradient

modgrad = np.sqrt(sobelx**2 + sobely**2)

plt.figure()
plt.imshow(modgrad, cmap="gray")
plt.title("Module gradient")

# 5. Décrire l’étape supplémentaire nécessaire pour obtenir une carte
# des contours ne contenant que les points de contours (c’est-à-dire
# une image binaire avec des « 1 » là ou des contours sont trouvés et « 0 »
# ailleurs). L’implémenter et commenter le résultat.

# Il faut choisir un seuil T et seuiller l'image du module de gradient

S = 0.17 * np.max(modgrad)

Img_bin = modgrad > S # Seuillage

plt.figure()
plt.imshow(Img_bin, cmap="gray")
plt.title("Detection des contours")

############################################################
###### Détection des contours avec le filtre de Canny ######
############################################################

# 1. Enumérer et expliquer les paramètres du filtre de Canny

#Approche de type gradient, hypothèse de bruit blanc gaussien, éléments
# de l’approche type laplacien
#• 3 objectifs :
#• Faibles taux d’erreurs (Pndf,Pfa)
#• Bonne localisation des contours
#• Des contours de largeur 1 pixel
#• Filtre optimal de Canny  « dérivée première d’une gaussienne »

# 2. Appliquer ce filtre

edges = cv2.Canny(img_grey,100,200)
plt.figure()
plt.imshow(edges,cmap = 'gray')
plt.title('Detection des contours avec un filtre de Canny'), plt.xticks([]), plt.yticks([])

#########################
###### Application ######
#########################

# 1. Lire et convertir l’image img_ds.jpg en niveaux de gris

img = cv2.imread('/Users/melvindubee/Documents/ENSTA/Traitement-image/DATA_TE5/img_ds.jpg')
img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.figure()
plt.imshow(img_grey, cmap="gray")
plt.title("Image en gris")

# 2. Lui appliquer un filtre de réduction de bruit

blur = cv2.GaussianBlur(img_grey,(9,9),0)
plt.figure()
plt.imshow(blur, cmap="gray")
plt.title("Reduction de bruit par filtre gaussien")



# 3. Réaliser une détection de contours de l’image filtrée
# (privilégier la méthodede Canny pour gagner du temps)

# Méthode de Canny

edges = cv2.Canny(blur,100,200)
plt.figure()
plt.imshow(edges, cmap = 'gray')
plt.title('Detection des contours avec un filtre de Canny'), plt.xticks([]), plt.yticks([])

plt.show()

# 5. Réaliser un étiquetage en composantes
# connexes de l’image obtenue en 3

num_features, comp_conn1 = cv2.connectedComponents(edges)
print("Nbre de contours: ", num_features-1)

# 6. Quel post-traitement pourrait-on appliquer à l’image des
# contours obtenue à la question 3 pour améliorer le résultat ? Pourquoi ?

# Pour améliorer le résultat, nous pouvons faire une segmentation (methode otsu)
# composantes connexes -> cb