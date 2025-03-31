import numpy as np
import cv2
from matplotlib import pyplot as plt

#Soit l’image pout.jpg convertie en niveaux de gris. Calculer et afficher en console :
# — la luminance (valeur de pixel) minimale de l’image
#— sa luminance maximale
#— sa luminance moyenne
#— l’écart-type des luminances

img = cv2.imread('/Users/melvindubee/Documents/ENSTA/Traitement-image/DATA_TE2/pout.jpg', 0)

img_float = np.float32(img)
lum_min = np.min(img_float)
lum_max = np.max(img_float)
lum_mean = np.mean(img_float)
lum_std = np.std(img_float)

print("Luminance minimale", lum_min, "Luminance maximale", lum_max, "Luminance moyenne", lum_mean,
      "Ecart-type des lumlinances", lum_std)

# Affichage de l'image initiale
plt.figure()
plt.subplot(221)
plt.imshow(img, cmap="gray")
plt.xticks([]), plt.yticks([])
plt.title("Image init")

# Histogramme OpenCV et Numpy
hist = cv2.calcHist([img],[0],None,[256],[0,256])
plt.subplot(222)
plt.plot(np.linspace(0,255,len(hist)),hist)
plt.grid(True)
plt.title("Histogramme with OpenCV")


# Histogramme d'égalisation et Affichage
img2 = cv2.equalizeHist(img)
hist2 = cv2.calcHist([img2],[0],None,[256],[0,256])

# Affichage de l'image égalisé
plt.subplot(223)
plt.imshow(img2, cmap="gray")
plt.xticks([]), plt.yticks([])
plt.title(" Image égalisé")

# Histogramme d'égalisation
plt.subplot(224)
plt.plot(np.linspace(0,256,len(hist2)),hist2)
plt.grid(True)
plt.title("Histogramme d'égalisation")

# Enregistrement de l'image égalisée
cv2.imwrite('ImageEgalize.png', img2)

# Methode CLAHE
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
img_clahe = clahe.apply(img)

plt.figure()
plt.imshow(img_clahe, cmap="gray")
plt.title("Image clahe")

# Enregistrement de l'image CLAHE
cv2.imwrite('ImageCLAHE.png', img_clahe)

plt.show()



