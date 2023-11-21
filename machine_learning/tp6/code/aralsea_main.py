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

# Pourcentage de la mer
answer = input('Numero de la classe de la mer ? ')
cl_mer = int(answer)
proportion_mer_img73 = (np.sum(img73_label == cl_mer) / img73_label.size)*100
proportion_mer_img87 = (np.sum(img87_label == cl_mer) / img87_label.size)*100

print("Proportion de la mer dans l'Image 1973:", proportion_mer_img73)
print("Proportion de la mer dans l'Image 1987:", proportion_mer_img87)
print("Une chute du niveau de la mer de:", proportion_mer_img73-proportion_mer_img87)

"""
Proportion de la mer dans l'Image 1973: 27.632828930016085
Proportion de la mer dans l'Image 1987: 21.373769627030974
Une chute du niveau de la mer de: 6.259059302985111
"""



### Approche   non-supervisée  par  GMM
# Apprentissage de la fonction de classement
model = unsupervisedTraining(featLearn, method='gmm')

# prediction des labels sur la base d'apprentissage
labels_predict = model.predict(featLearn)

# Visualisation des resultats
displayFeatures2d(featLearn, labels_predict)
displayFeatures3d(featLearn, labels_predict)


## Classement et estimation de la diminution de surface
# Classifying / Predicting / Testing
labels_prediction_img73 = unsupervisedClassifying(model, img73)
labels_prediction_img87 = unsupervisedClassifying(model, img87)


# mise en forme de l'image de 1973 et 1987 en matrice Num Pixels / Val Pixels
img73_label, img73_plot = displayImageLabel(labels_prediction_img73, img73)
img87_label, img87_plot = displayImageLabel(labels_prediction_img87, img87)

# Pourcentage de la mer
answer = input('Numero de la classe de la mer ? ')
cl_mer = int(answer)
proportion_mer_img73 = (np.sum(img73_label == cl_mer) / img73_label.size)*100
proportion_mer_img87 = (np.sum(img87_label == cl_mer) / img87_label.size)*100

print("Proportion de la mer dans l'Image 1973:", proportion_mer_img73)
print("Proportion de la mer dans l'Image 1987:", proportion_mer_img87)
print("Une chute du niveau de la mer de:", proportion_mer_img73-proportion_mer_img87)

"""
Proportion de la mer dans l'Image 1973: 24.335534408428973
Proportion de la mer dans l'Image 1987: 19.05388782686432
Une chute du niveau de la mer de: 5.2816465815646545
"""
