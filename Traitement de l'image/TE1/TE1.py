import numpy as np
import cv2
import matplotlib.pyplot as plt

# Part 1
#Question.1
# Load a color image in grayscale with OpenCV
img = cv2.imread('/Users/melvindubee/iCloud Drive (archives)/Documents/ENSTA/Traitement-image/DATA_TE1/voilier_oies_blanches.jpg', 0)
cv2.imshow('image', img)
cv2.waitKey(1000) #time in ms
cv2.destroyAllWindows()

#Question.2
# -largeur et la hauteur de l’image en nombre de pixels
# -quantification, c’est-à-dire le nombre d’octets utilisés pour coder la valeur des pixels
# et le type
print("Largeur et hauteur de l'image en nombre de pixels", np.shape(img))
print("La quantification de l'image", img.itemsize)
print("Type des pixels", img.dtype)
print("Dimension de l'image", img.ndim)

#Question.3
# Matplotlib
plt.figure()
plt.imshow(img, cmap='gray'), plt.title('image voilier oies blanches'), plt.xlabel('indice colonne n'), plt.ylabel(
    'indice ligne m')
plt.show()

#Part 2 - Transformée de Fourier discrète 2D

# Calcul d’une TFD-2D

#Question.1
# Lire et convertir en niveaux de gris l’image bibliotheque.jpg
img2 = cv2.imread('/Users/melvindubee/iCloud Drive (archives)/Documents/ENSTA/Traitement-image/DATA_TE1/bibliotheque.jpg', 0)
cv2.imshow('image', img2)
cv2.waitKey(1000) #time in ms
cv2.destroyAllWindows()

#Question.2
# La visualiser en utilisant les fonctions de matplotlib, insérer un titre et en renseigner les axes
plt.imshow(img2, cmap="gray")
plt.title("Image Bibliothèque"), plt.xlabel('indice colonne n'), plt.ylabel(
    'indice ligne m')
plt.show()

#Question.3
# calcul de la TFD-2D avec numpy
fft2 = np.fft.fft2(img2)
print("fft2 de l'image", fft2)

#Question.4 et 5
# Spectre d’amplitude pour des fréquences spatiales u et v entre 0 et 1
Spectre_Amplitude = abs(fft2)
plt.imshow(np.log2(1+Spectre_Amplitude), extent=(0, 1, 1, 0), cmap='jet')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Spectre d’amplitude")
plt.colorbar()
plt.figure()
plt.show()

# la transformée de Fourier est calculée pour des fréquences horizontale u et verticale v normalisées
# entre 0 et 1
# (fréquence horizontale (resp. verticale) <=> variation de niveaux de gris selon x
# (y respectivement))


#Question.6 et 7
# spectre d’amplitude pour les fréquences spatiales u et v entre -0.5 et 0.5 en s’appuyant sur la fonction complémentaire utile fft.fftshift())
Spectre_Amplitude2 = np.abs(np.fft.fftshift(fft2))
plt.imshow(np.log2(1+Spectre_Amplitude2), extent=(-0.5, 0.5, -0.5, 0.5), cmap='jet')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Spectre d’amplitude centré")
plt.colorbar()
plt.figure()
plt.show()

# Question.8
# En quoi ce graphe permet-il une meilleure interprétation que le précédent ?

# Ce graphe permet une meilleure visualisation et donc une meilleure
# interpretation car le contenu fréquentiel aux basses fréquences se trouve désormais au centre
# et les hautes fréquences autour.

#Question.9
# Spectre d’amplitude sur plus depoints fréquentiels, par exemple sur 1024*1024 points, le visualiser et commenter.
Spectre_Amplitude3 = np.abs(np.fft.fft2(fft2, (1024, 1024)))
Spectre_Amplitude3_shifted_1024 = np.fft.fftshift(Spectre_Amplitude3);
plt.imshow(np.log2(1+Spectre_Amplitude3_shifted_1024), extent=(-0.5, 0.5, -0.5, 0.5), cmap='jet')
plt.title('Spectre d\'amplitude centré avec zero-padding'),
plt.xlabel('u'), plt.ylabel('v');
plt.colorbar()
plt.figure()
plt.show()

# Comment s’appelle cette "opération" ?

# %% Zéro-padding : permet de mieux visualiser le spectre en rajoutant des points
# de calcul (i.e. des fréquences))dans le calcul de la FFT. Cette opération ne modifie pas le spectre,
# c'est le même sauf qu'en rajoutant des points de calcul, on affiche la TF pour
# des fréquences intermédiaires, ce qui implique une meilleure précision.


# Interprétation

#Question.1
# Afficher les deux images D1.tif et D4.tif
img_d1 = cv2.imread('/Users/melvindubee/iCloud Drive (archives)/Documents/ENSTA/Traitement-image/DATA_TE1/D1.tif', 0)
plt.figure()
plt.subplot(121)
plt.imshow(img_d1, cmap='gray'), plt.title('image D1'), plt.xlabel('indice colonne n'), plt.ylabel(
    'indice ligne m')

img_d4 = cv2.imread('/Users/melvindubee/iCloud Drive (archives)/Documents/ENSTA/Traitement-image/DATA_TE1/D4.tif', 0)
plt.subplot(122)
plt.imshow(img_d4, cmap='gray'), plt.title('image D4'), plt.xlabel('indice colonne n')
plt.show()

#Question.2
# Calculer leur transformée de Fourier discrète et leur spectre d’amplitude

TFD_D1 = np.fft.fft2(img_d1)
Spectre_Amplitude_D1 = np.abs(np.fft.fftshift(TFD_D1))

TFD_D4 = np.fft.fft2(img_d4)
Spectre_Amplitude_D4 = np.abs(np.fft.fftshift(TFD_D4))

# Affichage spectre d'amplitude D1
plt.figure()
plt.subplot(121)
plt.imshow(np.log2(1+Spectre_Amplitude_D1), extent=(-0.5, 0.5, -0.5, 0.5), cmap='jet')
plt.title('Spectre d\'amplitude centré D1'),
plt.xlabel('u'), plt.ylabel('v');

# Affichage spectre d'amplitude D4
plt.subplot(122)
plt.imshow(np.log2(1+Spectre_Amplitude_D4), extent=(-0.5, 0.5, -0.5, 0.5), cmap='jet')
plt.title('Spectre d\'amplitude centré D4'),
plt.xlabel('u')
plt.show()

#Question.3
# Comment peut-on expliquer ces spectres d’amplitude ?
# Le spectre d'amplitude de D1 et D4 ne présente pas de forte variation de fréquence. Ceci pourrait être dû à leurs
# périodicité mais également aux niveaux de gris où il n'y a pas de pique de contraste.

#Question.4
# A votre avis, pourrait-on différencier D1 et D4 à partir de leur transformée de Fourier ?
# Oui, on remarque les niveaux de gris sur D1 sont bien plus prononcé à certains endroit, et c'est changement sont net
# contrairement à l'image D4 présente des niveaux gris plus fondu. On imagine donc facilement que le premier spectre
# d'amplitude est D1, les variations de fréquences sont plus spontané contrairement au spectre d'amplitude de D4 ou
# la transition est plus douce.

#Question.5
# Afficher les deux images crayons.jpg et bibliotheque.jpg après les avoir converties en ni- veaux de gris !

img_pen = cv2.imread("/Users/melvindubee/iCloud Drive (archives)/Documents/ENSTA/Traitement-image/DATA_TE1/crayons.jpg", cv2.IMREAD_GRAYSCALE)
img_bib = cv2.imread("/Users/melvindubee/iCloud Drive (archives)/Documents/ENSTA/Traitement-image/DATA_TE1/bibliotheque.jpg", cv2.IMREAD_GRAYSCALE)

plt.figure()
plt.subplot(121)
plt.title('crayons.jpg')
plt.imshow(img_pen, cmap='gray')
plt.subplot(122)
plt.title('bibliotheque.jpg')
plt.imshow(img_bib, cmap='gray')
plt.show()

#Question.6
# Calculer leur transformée de Fourier discrète et leur spectre d’amplitude
fft_pen = np.fft.fft2(img_pen)
magnitude_spectrum_pen = np.abs(np.fft.fftshift(fft_pen))

fft_bib = np.fft.fft2(img_bib)
magnitude_spectrum_bib = np.abs(np.fft.fftshift(fft_bib))

plt.figure()
plt.subplot(211)
plt.title("|F(u,v)| crayons")
plt.xlabel('u')
plt.ylabel('v')
plt.imshow(np.log2(1+magnitude_spectrum_pen), extent=(-0.5,0.5,0.5,-0.5), cmap='jet')
plt.colorbar()
plt.subplot(212)
plt.title("|F(u,v)| bibliotheque")
plt.xlabel('u')
plt.ylabel('v')
plt.imshow(np.log2(1+magnitude_spectrum_bib), extent=(-0.5,0.5,0.5,-0.5), cmap='jet')
plt.colorbar()
plt.show()

#Question.7
# Interpréter leur contenu au regard du contenu spatial et de vos connaissances

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
# que l'on peut associer aux livres qui sont penchés. On remarque ensuite deux pics
# d'énergie en u=0.18 cycles par pixel et v=0 ce qui correspond à une périodicité
# selon x de 5 pixels environ, que l'on peut associer aux livres verticaux dont la
# taille est environ de 5 pixels.








