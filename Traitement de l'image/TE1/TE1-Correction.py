# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 09:31:54 2017
@author: thomashe

Nom du programme TE2F.py
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Transformée de Fourier et interprétation
# voir tutoriaux python-OpenCV

plt.close('all')
I = cv2.imread('../../DATA/bibliotheque.jpg', 0)
plt.figure()
plt.imshow(I, cmap='gray'), plt.title('image bibliotheque'), plt.xlabel('indice colonne n'), plt.ylabel(
    'indice ligne m')

# %% calcul de la TFD-2D avec numpy
TFD_I = np.fft.fft2(I);
# la transformée de Fourier est calculée pour des fréquences horizontale u et verticale v normalisées
# entre 0 et 1 -
# (fréquence horizontale (resp. verticale) <=> variation de niveaux de gris selon x
# (y respectivement))
# calcul du spectre d'amplitude:
# le spectre d'amplitude  défini pour des fréquences u et v
# normalisées et tq 0<u<1 et 0<v<1 est donc donné par:
magnitude_spectrum = np.abs(TFD_I);
# visualisation du spectre
plt.figure()
plt.subplot(121), plt.imshow(I, cmap='gray')
plt.title('I'), plt.xlabel('n - axe x'), plt.ylabel('m - axe y')
plt.subplot(122), plt.imshow(np.log2(1 + magnitude_spectrum), origin=('upper'), extent=(0, 1, 1, 0), cmap='jet')
# sans extent(0,1,1,0), les axes sont référencés en nombre de points et non pas
# en fréquences normalisées entre 0 et 1 pour chaque axe. Bien renseigner ce
# champ extent est essentiel pour bien interpréter le spectre
# Bien noter que la syntaxe pour extent est (left, right, bottom, top). Comme
# l'axe y va vers le bas il faut saisir extent(0,1,1,0) et non pas extent(0,1,0,1)
plt.title('Spectre d''amplitude avec numpy'), plt.xlabel('u'), plt.ylabel('v')
plt.show()

# %%

# visualisation du spectre centré pour une meilleure interprétation
# décalage du spectre d'amplitude (spectre dit centré):
# le spectre d'amplitude est défini pour des fréquences u et v
# normalisées et tq -1/2<u<1/2 et -1/2<v<1/2
TFD_I = np.fft.fft2(I);  # rappelé uniquement par souci de clareté mais inutile car déjà fait au dessus
magnitude_spectrum = np.abs(np.fft.fftshift(TFD_I))
plt.figure()
plt.subplot(121), plt.imshow(I, cmap='gray')
plt.title('I'), plt.xlabel('n - axe x'), plt.ylabel('m - axe y')
plt.subplot(122), plt.imshow(np.log2(1 + magnitude_spectrum), origin=('upper'), extent=(-0.5, 0.5, 0.5, -0.5),
                             cmap='jet')
# attention à bien renseigner le paramètre extent.
# Bien saisir extent=(-0.5,0.5,0.5,-0.5) et non pas l'inverse !!!
plt.title('Spectre d''amplitude centré'), plt.xlabel('u'), plt.ylabel('v')
plt.show()
# Remarque 1 : Ce graphe permet une meilleure visualisation et donc une meilleure
# interpretation car le contenu fréquentiel aux basses fréquences se trouve désormais au centre
# et les hautes fréquences autour.

# %% Zéro-padding : permet de mieux visualiser le spectre en rajoutant des points
# de calcul (i.e. des fréquences))dans le calcul de la FFT. Cette opération ne modifie pas le spectre,
# c'est le même sauf qu'en rajoutant des points de calcul, on affiche la TF pour
# des fréquences intermédiaires, ce qui implique une meilleure précision.
TFD_I_512 = np.fft.fft2(I);
magnitude_spectrum512 = np.abs(TFD_I_512);

TFD_I_1024 = np.fft.fft2(I, (1024, 1024));
magnitude_spectrum1024 = np.abs(TFD_I_1024);

magnitude_spectrum_shifted_512 = np.fft.fftshift(magnitude_spectrum512);
magnitude_spectrum_shifted_1024 = np.fft.fftshift(magnitude_spectrum1024);

plt.figure()
plt.subplot(121), plt.imshow(np.log2(1 + magnitude_spectrum_shifted_512), extent=(-0.5, 0.5, 0.5, -0.5), cmap='jet')
plt.title('Spectre d\'amplitude centré sur 512 pts'),  # plt.colorbar()
plt.xlabel('u'), plt.ylabel('v');

plt.subplot(122), plt.imshow(np.log2(1 + magnitude_spectrum_shifted_1024), extent=(-0.5, 0.5, 0.5, -0.5), cmap='jet')
plt.title('Spectre d\'amplitude centré avec zero-padding'),  # plt.colorbar()
plt.xlabel('u'), plt.ylabel('v');
plt.show()

# %% Interprétation - images présentant des périodicités
im1 = cv2.imread('../../DATA/D1.tif', 0);
im2 = cv2.imread('../../DATA/D4.tif', 0);
# im1=cv2.imread('../DATA/crayons.jpg',0);
# im2=cv2.imread('../DATA/bibliotheque.jpg',0);
# im3=cv2.imread('pollen.jpg',0);
# im2=cv2.imread('../DATA/neige.JPG',0);

TF1 = np.fft.fft2(im1);
spectre1s = np.abs(np.fft.fftshift(TF1))
TF2 = np.fft.fft2(im2);
spectre2s = np.abs(np.fft.fftshift(TF2))

plt.figure()
plt.subplot(221), plt.imshow(im1, cmap='gray')
plt.title('Input image')
plt.subplot(222), plt.imshow(np.log2(1 + spectre1s), extent=(-0.5, 0.5, 0.5, -0.5), cmap='jet')
plt.title('Spectre d\'amplitude'), plt.colorbar()
plt.subplot(223), plt.imshow(im2, cmap='gray')
plt.title('Input image')
plt.subplot(224), plt.imshow(np.log2(1 + spectre2s), extent=(-0.5, 0.5, 0.5, -0.5), cmap='jet')
plt.title('Spectre d''amplitude'), plt.colorbar()
plt.show()

#   - le spectre d'amplitude de l'image crayons présente 3 particularités.
# Tout d'abord une très forte concentration de l'énergie pour des couples de
# fréquences (u,v) multiples de (0.13,-0.09) ce qui laisse supposer une périodicité
# dans l'image de périodes spatiales (1/0.13, 1/0.09) pixels dans la direction "45°"
# soit 7.7 pixels selon x et 11.1 pixels selon y dans la direction "45°" ce qui
# correspond vraisemblablement aux crayons de couleur. Deuxièmement, on décèle deux
# traits lumineux, l'un en u=0 et l'autre en v=0. Or d'après le cours, on en déuit
# que l'on a deux "lames lumineuses" dans l'image. Celles-ci sont dues aux bords de
# l'image qui présentent de fortes variations si on considère les 1ère et dernière
# lignes et 1ères et dernières colonnes. Enfin, on remarque des sortes de croix composées
# de petites lames "parallèles" d'énergie qui se répètent, croix centrées autour des
# fréquences multiples de (0.13,-0.09). On peut les relier aux pointes des crayons.

#   - le spectre de l'image bibliothèque présente également un spectre de raies
# d'espacement v=0.03 environ ce qui laisse supposer une périodicité spatiale de
# période 1/0.03 pixels soit 33 pixels verticalement et effectivement les étagères
# sont espacées d'a peu près 30 pixels ! on devine également une bande diagonale d'énergie,
# que l'on peut assoscier aux livres qui sont penchés. On remarque ensuite deux pics
# d'énergie en u=0.18 cycles par pixel et v=0 ce qui correspond à une périodicité
# selon x de 5 pixels environ, que l'on peut associer aux livres verticaux dont la
# taille est environ de 5 pixels.




