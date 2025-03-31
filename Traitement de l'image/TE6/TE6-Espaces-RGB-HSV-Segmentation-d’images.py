import numpy as np
import cv2
from matplotlib import pyplot as plt

# 1.1.1 Affichage image via --> affichage format RGB
img = cv2.imread('/Users/melvindubee/Documents/ENSTA/Traitement-image/DATA_TE6/house.jpg')
img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.figure()
plt.imshow(img)
plt.figure()
cv2.imshow('Image normale', img)
plt.figure()
plt.imshow(img_grey, cmap="gray")
plt.title("Image en gris")

# 1.1.2

b, g, r = cv2.split(img)
img2 = cv2.merge([r,g,b])

plt.figure()
plt.subplot(131)
plt.imshow(b, cmap='gray')
plt.title("Mon image B plt")
plt.subplot(132)
plt.imshow(g, cmap='gray')
plt.title("Mon image g plt")
plt.subplot(133)
plt.imshow(r, cmap='gray')
plt.title("Mon image r plt")





# 1.2 Conversion de format

# Convertir l'image au format HSV

imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v= cv2.split(imgHSV) # Extraction des trois plans

# 1.2.3 Affichage des trois canaux séparéments

plt.figure()
plt.subplot(131)
plt.imshow(h, cmap='gray')
plt.xticks([]),plt.yticks([])
plt.title("Mon image H teinte")
plt.subplot(132)
plt.imshow(s, cmap='gray')
plt.xticks([]),plt.yticks([])
plt.title("Mon image S Saturation")
plt.subplot(133)
plt.imshow(v, cmap='gray')
plt.xticks([]),plt.yticks([])
plt.title("Mon image Valeur")

# 1.3.2 Conversion HSV et modification de H
# Se souvenir que la teinte est un angle entre 0 et 360° convertie sous OpenCV
# valeur entre 0 et 179° qui boucle
I_new_HSV1 = imgHSV.copy()
h, s, v = cv2.split(imgHSV)
H_new = h + 60 # H+60 une rotation des couleurs : rouge --> vert
H_new[H_new>180] = H_new[H_new>180]-160

I_new_HSV1[:,:,0] = H_new
I_new = cv2.cvtColor(I_new_HSV1, cv2.COLOR_HSV2BGR)

#h_min =
#s_min =
#h_max =

#def binariseHSV():
    #lower = np.array([h_min, s_min, v_min])
    #upper = np.array([h_max, s_max, v_max])
    #print("Seuil Bas HSV:",lower)
    #print("Seuil Haut HSV", )


# 4.2 - Implémentation d’une binarisation par seuillage dans l’espace RGB - algorithme très simplifié

# Chargement de l'image
img = cv2.imread('/Users/melvindubee/Documents/ENSTA/Traitement-image/DATA_TE6/crayons.jpg')




plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()




