import numpy as np
import cv2
from matplotlib import pyplot as plt

###############################################################
###################Binarisation manuelle#######################
###############################################################

# Image couleur
img = cv2.imread('/Users/melvindubee/Documents/ENSTA/Traitement-image/DATA_TE3/voilier_oies_blanches.jpg')
cv2.imshow('image en couleur', img)

# Image gris
Img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('image en gris', Img_grey)

#Binarisation
ret,thresh1 = cv2.threshold(Img_grey,127,255,cv2.THRESH_BINARY)
cv2.imshow('image binaire', thresh1)
cv2.waitKey(0)

#Threshold_type

ret,thresh2 = cv2.threshold(Img_grey,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(Img_grey,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(Img_grey,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(Img_grey,127,255,cv2.THRESH_TOZERO_INV)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray',vmin=0,vmax=255)
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])


images = [Img_grey, 0, thresh1]

#Histogramme
plt.figure()
for i in range(3):
    plt.hist(images[0].ravel(),256)
    plt.plot()

###############################################################
############Binarisation manuelle avec trackbar################
###############################################################

# fonction appelée par cv2.createTrackbar()
def Seuillage(x):
    ret, binary = cv2.threshold(Img_grey, cv2.getTrackbarPos("Seuil T", "Binary"), 255, cv2.THRESH_BINARY_INV);

    # cv2.getTrackbarPos("Seuil T","Binary") : renvoie la valeur (position) du curseur
    # nommé "Seuil T" de la fenêtre nommée "Binary" lorsque vous l'avez bougé
    # 255 est la valeur que prennent les pixels dont les niv de gris sont supérieurs
    # ou inférieurs au seuil (selon Type choisi dans cv2.threshold - threshold_type)
    # cv2.THRESH_BINARY_INV : valeur choisie pour threshold_type
    cv2.imshow("Binary", binary);


# Création d'une fenêtre allant contenir l'image binaire
cv2.namedWindow("Binary", 1)
cv2.createTrackbar("Seuil T", "Binary", 100, 255, Seuillage);  # création
# d'un curseur glissant nommé "Seuil T" dans la fenêtre nommée "Binary". La position
# initiale de ce curseur est fixée à une valeur quelconque désignée par la variable seuil(=100),
# la valeur max est 255. L'action à réaliser à chaque fois que la position du curseur
# bouge, est la fonction seuillage.
cv2.waitKey(0)
plt.show


# Binarisation automatique
plt.figure()
# Image voilier oies blanches

# global thresholding
ret1,th1 = cv2.threshold(Img_grey,127,255,cv2.THRESH_BINARY)

# Otsu's thresholding
ret2,th2 = cv2.threshold(Img_grey,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Otsu's thresholding after Gaussian filtering
blur = cv2.GaussianBlur(Img_grey,(5,5),0)
ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# plot all the images and their histograms
images = [img, 0, th1,
          img, 0, th2,
          blur, 0, th3]
titles = ['Original Noisy Image','Histogram','Global Thresholding (v=127)',
          'Original Noisy Image','Histogram',"Otsu's Thresholding",
          'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]
for i in range(3):
    plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
    plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
    plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
    plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
plt.show()


# Image img_ds
