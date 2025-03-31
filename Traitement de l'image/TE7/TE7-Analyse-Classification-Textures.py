import cv2
from matplotlib import pyplot as plt
from OutilsTNI import divide
from OutilsTNI import formate_resultat
import numpy as np
from skimage import feature
from sklearn.cluster import KMeans

# Chargement des images
Tex1 = cv2.imread('/Users/melvindubee/Documents/DATA_TE7_python/D1.tif', cv2.IMREAD_GRAYSCALE)
Tex2 = cv2.imread('/Users/melvindubee/Documents/DATA_TE7_python/D4.tif', cv2.IMREAD_GRAYSCALE)

# Génération des deux classes
Class1 = divide(Tex1,128)
Class2 = divide(Tex2,128)

# Définition des n imagette
n = 24 # imagette n d'une classe (n doit être entre 1 et la longueur de Class1 et Class2, soit 25 ici)

plt.figure()
plt.subplot(121)
plt.imshow(Class1[n],cmap='gray')
plt.title('imagette %d issue de Tex1'%n)
plt.subplot(122)
plt.imshow(Class2[n],cmap='gray')
plt.title('imagette %d issue de Tex2'%n)

# Matrices de co-occurence
glcm1=[]
glcm2=[]
for patch in Class1:
    glcm1.append(feature.graycomatrix(patch, distances=[1],
          angles=[0,np.pi/4], levels=256,
          symmetric=True, normed=True))
for patch in Class2:
    glcm2.append(feature.graycomatrix(patch, distances=[1],
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
for i in range(6):
    plt.subplot(2,3,i+1)
    plt.plot(x1[i,:],'b*--',label='Tex1')
    plt.plot(x2[i, :], 'r*--',label='Tex2')
    plt.title('paramètre : {}'.format(i+1))

# Vecteurs de paramètres
p1=1
p2=3
p3=4
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(x1[p1,:], x1[p2,:], x1[p3,:],marker='o',label='D1')
ax.scatter(x2[p1,:], x2[p2,:], x2[p3,:],marker='x',label='D4')


# La figure tracé permet de distinguer deux clusters de points
# ils représentent deux textures distinctes, plus ils sont éloignés
# plus on a réussi à dinstinguer les deux textures.
# Au niveau des points du cluster, plus ils sont eloignés
# plus ils sont sensibles à la luminosité et au changement de couleur.

# Reconnaisance manuelle
xTest = np.zeros(6)
Tex3 = cv2.imread('/Users/melvindubee/Documents/DATA_TE7_python/Test.tif', cv2.IMREAD_GRAYSCALE)
glcmTest = feature.graycomatrix(patch, distances=[1], angles=[0],
                             levels=256, symmetric=True, normed=True)
xTest[0] = feature.graycoprops(glcmTest, 'contrast')[0, 0]  # Contrast
xTest[1] = feature.graycoprops(glcmTest, 'homogeneity')[0, 0]  # Homogénéité
xTest[2] = feature.graycoprops(glcmTest, 'dissimilarity')[0, 0]
xTest[3] = feature.graycoprops(glcmTest, 'ASM')[0, 0]
xTest[4] = feature.graycoprops(glcmTest, 'energy')[0, 0]  # Uniformité de l'énergie
xTest[5] = feature.graycoprops(glcmTest, 'correlation')[0, 0]  # Corrélation
ax.scatter(x2[p1,:], x2[p2,:], x2[p3,:],marker='+',label='Test')
ax.set_xlabel('p %d' % p1)
ax.set_ylabel('p %d' % p2)
ax.set_zlabel('p %d' % p3)
plt.legend()

# D'après ce que l'on obtient, l'imagette test appartient à la class 2

# Segmentation non supervisée
Tex4 = cv2.imread('/Users/melvindubee/Documents/DATA_TE7_python/img_tex_1.tif', cv2.IMREAD_GRAYSCALE)

# Découpage en sous-image
# Génération des deux classes
Class3 = divide(Tex4,128)

# Définition des n imagette
n = 15 # imagette n d'une classe (n doit être entre 1 et la longueur de Class1 et Class2, soit 25 ici)

plt.figure()
plt.imshow(Class3[n],cmap='gray')
plt.title('imagette %d issue de Tex4'%n)

# Matrices de co-occurence
glcm3=[]

for patch in Class3:
    glcm3.append(feature.graycomatrix(patch, distances=[1],
                 angles=[0, np.pi / 4], levels=256,
                 symmetric=True, normed=True))

# Paramètres d'Haralick
x3 = np.zeros((6,len(Class3)))
for i,patch in enumerate(Class3):
    glcm = feature.graycomatrix(patch, distances=[1], angles=[0],
          levels=256, symmetric=True, normed=True)
    x3[0,i]=feature.graycoprops(glcm, 'contrast')[0, 0] # Contrast
    x3[1,i]=feature.graycoprops(glcm, 'homogeneity')[0, 0] # Homogénéité
    x3[2,i]=feature.graycoprops(glcm, 'dissimilarity')[0, 0]
    x3[3,i]=feature.graycoprops(glcm, 'ASM')[0, 0]
    x3[4,i]=feature.graycoprops(glcm, 'energy')[0, 0] # Uniformité de l'énergie
    x3[5,i]=feature.graycoprops(glcm, 'correlation')[0, 0] # Corrélation
plt.figure()

# Vecteurs de paramètres
p1=1
p2=3
p3=4
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(x2[p1,:], x2[p2,:], x2[p3,:],marker='o',label='Tex4')

# Algorithme des k-moyennes
kmeans = KMeans(n_clusters=2).fit(x1.T[:,(p1,p2,p3)])

# Position des clusters
ax.scatter(kmeans.cluster_centers_[0,0],
kmeans.cluster_centers_[0,1],
kmeans.cluster_centers_[0,2],marker='+',c='k')
ax.scatter(kmeans.cluster_centers_[1,0],
kmeans.cluster_centers_[1,1],
kmeans.cluster_centers_[1,2],marker='x',c='k')

# Image segmentée
img_rh=formate_resultat(Tex4,len(Tex4),kmeans.labels_)

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()