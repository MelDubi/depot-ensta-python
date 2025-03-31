import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("/Users/melvindubee/Documents/ENSTA/Traitement-image/DATA_TE2/Image_epave.jpg", cv2.IMREAD_GRAYSCALE)

plt.figure()
plt.subplot(321)
plt.imshow(img, cmap='gray')
plt.xticks([]), plt.yticks([])
plt.title("Image epave")


taille = 7
kernel = np.ones((taille, taille), np.float32)/(taille**2)
ddepth = -1
img_fil = cv2.filter2D(img, ddepth, kernel)
img_filt2 = cv2.blur(img,(taille, taille))

plt.subplot(322)
plt.imshow(img_filt2, cmap='gray')
plt.title("Filtre Moyenneur with filter2D")

plt.subplot(323)
plt.imshow(img_fil, cmap='gray')
plt.title("Filtre Moyenneur with blur")

# Filtrage Gaussien

taille = 7
img_gauss = cv2.GaussianBlur(img,(taille, taille),0)
img_gauss2 = cv2.GaussianBlur(img,(taille, taille),4,4, cv2.BORDER_DEFAULT)
plt.subplot(324)
plt.imshow(img_gauss, cmap='gray')
plt.title("Filtre Gaussien")
plt.subplot(325)
plt.imshow(img_gauss, cmap='gray')
plt.title("Filtre Gaussien 2")



# Filtrage non-linéaire Median

taille= 7
img_median = cv2.medianBlur(img, taille)

plt.subplot(326)
plt.imshow(img_median, cmap='gray')
plt.title("Image après Median")

plt.show()