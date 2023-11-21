#%% Machine Learning Class - Exercise Aral Sea Surface Estimation

# package
import numpy as np
import matplotlib.pyplot as plt

plt.ioff() # to see figure avant input


# ------------------------------------------------
# YOUR CODE HERE
from preprocessing import preprocessing
from unsupervisedTraining import unsupervisedTraining
from unsupervisedClassifying import unsupervisedClassifying

from displayFeatures2d import displayFeatures2d
from displayFeatures3d import displayFeatures3d
from displayImageLabel import displayImageLabel



# ------------------------------------------------
# ------------------------------------------------





#%% Examen des données, prétraitements et extraction des descripteurs

# Chargement des données et prétraitements
featLearn, img73, img87 = preprocessing()

height, width, channels = img73.shape
print(f"Image img73 dimensions: Height = {height}, Width = {width}, Channels = {channels}")
height, width, channels = img87.shape
print(f"Image img87 dimensions: Height = {height}, Width = {width}, Channels = {channels}")

"""
Image img73 dimensions: Height = 889, Width = 1086, Channels = 3
Image img87 dimensions: Height = 889, Width = 1086, Channels = 3
"""

plt.subplot(1, 2, 1)
plt.imshow(img73)
plt.title('Cropped Image 1973')

plt.subplot(1, 2, 2)
plt.imshow(img87)
plt.title('Cropped Image 1987')

plt.show()



#%% Apprentissage / Learning / Training

# Apprentissage de la fonction de classement
model = unsupervisedTraining(featLearn, method='kmeans')

# prediction des labels sur la base d'apprentissage
labels_predict = model.predict(featLearn)

# Visualisation des resultats
displayFeatures2d(featLearn, labels_predict)
displayFeatures3d(featLearn, labels_predict)


#%% Classement et estimation de la diminution de surface
# Classifying / Predicting / Testing
labels_prediction_img73 = unsupervisedClassifying(model, img73)
labels_prediction_img87 = unsupervisedClassifying(model, img87)


# mise en forme de l'image de 1973 et 1987 en matrice Num Pixels / Val Pixels
img73_label, img73_plot = displayImageLabel(labels_prediction_img73, img73)
img87_label, img87_plot = displayImageLabel(labels_prediction_img87, img87)

plt.subplot(1, 2, 1)
plt.imshow(img73_label)
plt.title('Image 1973 Predicted Labels')

plt.subplot(1, 2, 2)
plt.imshow(img87_label)
plt.title('Image 1987 Predicted Labels')
plt.colorbar()

plt.show()




# ------------------------------------------------
# YOUR CODE HERE















# ------------------------------------------------
# ------------------------------------------------


# Classement des deux jeux de données et visualisation des résultats en image

# ------------------------------------------------
# YOUR CODE HERE


























# ------------------------------------------------
# ------------------------------------------------



#%% Estimation de la surface perdue
answer = input('Numero de la classe de la mer ? ')
cl_mer = int(answer)



# ------------------------------------------------
# YOUR CODE HERE










# ------------------------------------------------
# ------------------------------------------------



