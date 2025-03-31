import numpy as np
import cv2
from matplotlib import pyplot as plt


# Image gris
img = cv2.imread('/Users/melvindubee/Documents/ENSTA/Traitement-image/DATA_TE3/voilier_oies_blanches.jpg')
img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.figure()
plt.imshow(img_grey, cmap="gray")
plt.title("Image en gris")

# 1.a Binarisation 'à la main'

seuil = 100

ret, img_bin = cv2.threshold(img_grey, seuil, 255, cv2.THRESH_BINARY_INV)
plt.figure()
plt.imshow(img_bin, cmap="gray")
plt.title("Image binaire")

# 1.b & 1.c Erosion & Dilation
ksize = 3 #Taille element structurant (gomme)
noyaux = cv2.getStructuringElement(cv2.MORPH_RECT, (ksize, ksize))

img_erode = cv2.erode(img_bin, noyaux) # Erosion
img_dilat = cv2.dilate(img_bin, noyaux) # Dilatation

# 1.d & 1.e Ouverture (Erosion -> Dilatation) et Fermeture (Dilatation -> Erosion)
img_ouv = cv2.dilate(img_erode, noyaux)
img_ferm = cv2.erode(img_dilat, noyaux)

# 1.f Opening-closing (Ouverture -> Fermeture)(Erosion ->
img_Opening_Closing1 = cv2.dilate(img_ouv, noyaux)
img_Opening_Closing2 = cv2.erode(img_Opening_Closing1, noyaux)


# Affichage des traitement morpho
plt.figure()
plt.imshow(img_erode, cmap="gray")
plt.title("Erosion")

plt.figure()
plt.imshow(img_dilat, cmap="gray")
plt.title("Dilatation")

plt.figure()
plt.imshow(img_ouv, cmap="gray")
plt.title("Ouverture")

plt.figure()
plt.imshow(img_ferm, cmap="gray")
plt.title("Fermeture")

plt.figure()
plt.imshow(img_Opening_Closing2, cmap="gray")
plt.title("Opening-Closing")

plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.5, hspace=0.5)

# 2.3 Etiquetage
num_features, comp_conn1 = cv2.connectedComponents(img_bin)
print("Nbre oiseaux: ", num_features-1)


plt.show()