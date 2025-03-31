# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 09:31:54 2017
Mis à jour le 05 mai 2021
@author: thomashe
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

# exemple d'initialisation pour détecter les objets verts de crayons.jpg  :
# valeurs à affiner avec des trackbars,  fonction de l'image
Smin, Smax = 0, 255;
Vmin, Vmax = 0, 255;
Hmin, Hmax = 40, 85;


# Attention : les valeurs de teinte sont divisées par 2 sous OpenCV !
# 0: rouge; 30:jaune, 60 : vert, 90:cyan, 120 :bleu et 150 : magenta


def binariseHSV():
    # Implémentation seuillage HSV selon l'algo donné dans l'énoncé, Q2.2.3
    maxVal = S.max();
    Smin = (int)(0.1 * (maxVal));

    lower_bound = np.array([Hmin, Smin, Vmin]);
    upper_bound = np.array([Hmax, Smax, Vmax]);
    BinaryHSV = cv2.inRange(imgHSV, lower_bound, upper_bound);

    ImgC_res = cv2.bitwise_and(img, img, mask=BinaryHSV);

    cv2.namedWindow("Binary with HSV topo", 1);
    cv2.imshow("Binary with HSV topo", BinaryHSV);
    cv2.imshow("Image Couleur résultat", ImgC_res);


#    plt.subplot(132),plt.imshow(BinaryHSV,cmap='gray'),plt.title('image binaire'),plt.show()
#    plt.subplot(133),plt.imshow(cv2.cvtColor(ImgC_res,cv2.COLOR_BGR2RGB)),
#    plt.title('Image couleur résultat'),plt.show()


def binariseHSV_trackbar(pos):
    # solution pour 2.2.6
    maxVal = S.max();
    Smin = (int)(0.1 * (maxVal));

    lower_bound = np.array([cv2.getTrackbarPos("Hmin", "Binary with HSV trackbar"), Smin, Vmin])
    upper_bound = np.array([cv2.getTrackbarPos("Hmax", "Binary with HSV trackbar"), Smax, Vmax])
    BinaryHSV = cv2.inRange(imgHSV, lower_bound, upper_bound);

    ImgC_res = cv2.bitwise_and(img, img, mask=BinaryHSV);

    cv2.namedWindow("Binary with HSV trackbar", 1);
    cv2.imshow("Binary with HSV trackbar", BinaryHSV);
    cv2.imshow("Image Couleur résultat", ImgC_res);


#    plt.subplot(132),plt.imshow(BinaryHSV,cmap='gray'),plt.title('image binaire'),plt.show()
#    plt.subplot(133),plt.imshow(cv2.cvtColor(ImgC_res,cv2.COLOR_BGR2RGB)),
#    plt.title('Image couleur résultat'),plt.show()

# %% 1.1 - Affichage d'images couleur

img = cv2.imread('../DATA/house.jpg');
# img=cv2.imread('../DATA/Maya-and-Mantra.jpg');

B = img[:, :, 0];
print('B : min={0} max={1}'.format(np.min(B), np.max(B)));
G = img[:, :, 1];
print('G : min={0} max={1}'.format(np.min(G), np.max(G)))
R = img[:, :, 2];
print('R : min={0} max={1}'.format(np.min(R), np.max(R)))
print('format de B,G et R :', B.dtype)

cv2.imshow('Image initiale', img);
res = np.concatenate((B, G, R), axis=1)
cv2.namedWindow('Canaux Bleu, Vert et Rouge', 0)
cv2.imshow('Canaux Bleu, Vert et Rouge', res)
cv2.waitKey(0)

# Visualisation avec les fonctions de matplotlib : attention  à ne pas oublier
# de convertir l'image au format RGB avant de la visualiser en couleur avec
# la fonction plt.imshow (imshow affiche l'image avec la table des couleurs RGB)!!
plt.figure()
plt.subplot(2, 2, 1)
imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB);
plt.imshow(imgRGB), plt.xlabel('image couleur');
plt.text(40, -35, 'visualisation image originale + 3 canaux séparés')
plt.subplot(2, 2, 2)
plt.imshow(B, cmap='gray'), plt.xlabel('canal bleu'), plt.colorbar()
# on spécifie une palette de gris pour cmap pour bien mettre en
# évidence le fait que chaque plan couleur est scalaire
plt.subplot(2, 2, 3)
plt.imshow(G, cmap='gray'), plt.xlabel('canal vert'), plt.colorbar()
plt.subplot(2, 2, 4)
plt.imshow(R, cmap='gray'), plt.xlabel('canal rouge'), plt.colorbar()
plt.show()

# 1.1.3 en amenant la souris sur les couleurs verte, rouge, jaune, bleue, noire, blanche
# de l'image house par exemple, on vérifie que les coordonnées RGB de ces couleurs
# sont cohérentes. On note cependant par exemple qu'un objet d'apparence bleue
# peut contenir une proportion non négligeable de vert et de rouge (exemple :
# pourtour de la cheminée bleue de l'image house)

# %% 1.2 - Conversion de format

imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV);
H = imgHSV[:, :, 0];
S = imgHSV[:, :, 1];
V = imgHSV[:, :, 2];

plt.figure()
plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.xlabel('image couleur');
plt.text(40, -35, 'visualisation image originale + 3 canaux séparés H,S,V')
plt.subplot(2, 2, 2)
plt.imshow(H, cmap='gray'), plt.xlabel('teinte');
plt.colorbar()
plt.subplot(2, 2, 3)
plt.imshow(S, cmap='gray'), plt.xlabel('saturation');
plt.colorbar()
plt.subplot(2, 2, 4)
plt.imshow(V, cmap='gray'), plt.xlabel('valeur');
plt.colorbar()
plt.show()

# %remarque : les images de Teinte, Saturation et Valeur sont des scalaires
# % As H varies from 0 to 179 (théoriquement, la teinte est un angle qui varie
# entre 0 et 360°, qui est divisé par 2 sous OpenCV pour pouvoir être codé
# sur 8 bits...), the resulting color varies from red through
# % yellow, green, cyan, blue, and magenta, and returns to red. When S
# % is 0, the colors are unsaturated (i.e., shades of gray). When S is
# % 255, the colors are fully saturated (i.e., they contain no white
# % component). As V varies from 0 to 255, the brightness increases.
# voir Cours également !

# question 1.2.5
# en amenant la souris sur les couleurs verte, rouge, jaune, bleue, noire, blanche
# des plans images H, S et V,on vérifie que les valeurs HSV de ces couleurs
# sont cohérentes. Par exemple pour le blanc, S est proche de 0 et V proche de 255
# pour le jaune, H est proche de 30, ....

# %% 1.3 - Modification des couleurs : H=H+60
# %se souvenir que la teinte est un angle entre 0 et 360° convertie
# sous OpenCV en une valeur entre 0 et 179" qui boucle" - cf poly de cours

# img=cv2.imread('../DATA/riviere.jpg');
img = cv2.imread('../DATA/pipeline3.png');
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV);
H = imgHSV[:, :, 0];
S = imgHSV[:, :, 1];
V = imgHSV[:, :, 2];

Ihsvn = imgHSV.copy();
Hnew = H + 60;  # red->green;green->blue;blue->red;jaune->cyan
Hnew[Hnew > 180] = Hnew[Hnew > 180] - 180;
Ihsvn[:, :, 0] = Hnew;
imgnew = cv2.cvtColor(Ihsvn, cv2.COLOR_HSV2BGR);
plt.figure()
plt.subplot(121), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title('image originale')
plt.subplot(122), plt.imshow(cv2.cvtColor(imgnew, cv2.COLOR_BGR2RGB));
plt.title('image avec H=H+60');
plt.show()
##pour simplifier l'affichage avec plt.imshow, on peut convertir directement en RGB
# imgnew=cv2.cvtColor(Ihsvn,cv2.COLOR_HSV2RGB);
# plt.figure()
# plt.subplot(121),plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB)),plt.title('image originale')
# plt.subplot(122), plt.imshow(imgnew); plt.title('image avec H=H+60');
# plt.show()

# %5.b - Modification des couleurs : S=S/3
Ihsvn = imgHSV.copy();
Ihsvn[:, :, 1] = S / 3;
imgnew = cv2.cvtColor(Ihsvn, cv2.COLOR_HSV2BGR);
plt.figure()
plt.subplot(121), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title('image originale')
plt.subplot(122), plt.imshow(cv2.cvtColor(imgnew, cv2.COLOR_BGR2RGB));
plt.title('image avec S=S/3');
plt.show()
# l'aspect délavé et surtout perte de couleur est visible
##comparaison des canaux de saturation pour s'en convaincre
# plt.figure()
# plt.subplot(121),plt.imshow(S,cmap='gray'),plt.title('canal S'),plt.colorbar()
# plt.subplot(122), plt.imshow(Ihsvn[:,:,1],cmap='gray'); plt.title('canal S/3'),plt.colorbar();
# plt.show()
# même si les images semblent identiques (adaptation de la dynamique par imshow)
# on se rend compte à l'aide de la colorbar que les pixels qui tendent à perdre
# leur couleur sont des pixels pour lesquels la saturation tend vers 0 'exemple :
# pierres qui semblent passer d'un jaune à un gris

# %5.a - Modification des couleurs : S=S*2
Ihsvn = imgHSV.copy();
Ihsvn[:, :, 1] = np.minimum(2.0 * S, 255);  # il faut bien mettre 2.0 et non 2!!!
imgnew = cv2.cvtColor(Ihsvn, cv2.COLOR_HSV2BGR);
plt.figure()
plt.subplot(121), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title('image originale')
plt.subplot(122), plt.imshow(cv2.cvtColor(imgnew, cv2.COLOR_BGR2RGB));
plt.title('image avec S=S*2');
plt.show()
# les couleurs sont plus marquées (bien écrire 2.0*S sinon troncature et résultat
# incohérent)

# %5.c - Modification des couleurs : V=V*1.5
Ihsvn = imgHSV.copy();
Ihsvn[:, :, 2] = np.minimum(V * 1.5, 255);
imgnew = cv2.cvtColor(Ihsvn, cv2.COLOR_HSV2BGR);
plt.figure()
plt.subplot(121), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title('image originale')
plt.subplot(122), plt.imshow(cv2.cvtColor(imgnew, cv2.COLOR_BGR2RGB));
plt.title('image avec V=1.5*V');
plt.show()
# résultat cohérent : l'image est plus lumineuse
cv2.waitKey(0)
cv2.destroyAllWindows()
plt.close('all')

# %% Partie 2 : binarisation d'une image couleur
# https://docs.opencv.org/3.2.0/df/d9d/tutorial_py_colorspaces.html
img = cv2.imread('../DATA/crayons.jpg');
cv2.namedWindow('Image source', 1)
cv2.imshow('Image source', img)
# plt.figure()
# plt.subplot(131),plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB)),
# plt.title('Image source'), plt.show()

# question 2.2.3 : binarisation dans le domaine HSV selon le topo de l'énoncé
# pour détecter des pixels de couleur définie par H et S
# solution sans la fonction binariseHSV
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV);
lower_bound = np.array([Hmin, Smin, Vmin]);
upper_bound = np.array([Hmax, Smax, Vmax]);
BinaryHSV = cv2.inRange(imgHSV, lower_bound, upper_bound);
cv2.imshow("ImageBinaire (HSV)", BinaryHSV);
key = cv2.waitKey(0)
if (key == ord('q')):
    cv2.destroyAllWindows()

# solution avec utilisation de la fonction binariseHSV
binariseHSV()
cv2.waitKey(0)
cv2.destroyAllWindows()

# question 2.2.6
# binarisation dans le domaine HSV avec des trackbars
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV);
S = imgHSV[:, :, 1];

binariseHSV_trackbar(0);
cv2.createTrackbar("Hmin", "Binary with HSV trackbar", Hmin, 180, binariseHSV_trackbar);
cv2.createTrackbar("Hmax", "Binary with HSV trackbar", Hmax, 180, binariseHSV_trackbar);
cv2.waitKey(0)
cv2.destroyAllWindows();
plt.close('all')
# fin de la binarisation dans le domaine HSV selon le topo de l'énoncé pour détecter des
# pixels verts (pour le rouge, c'est un peu plus compliqué : teinte proche de 0+ et/ou 0-)

