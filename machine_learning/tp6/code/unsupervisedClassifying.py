#%% package
import numpy as np
from sklearn.cluster import KMeans


#%% def unsupervisedClassifying
def unsupervisedClassifying(model, feat):
    ''' classement/prédiction à partir d'un modèle de classement non supervisé
    feat est la matrice du jeu de données à classer
    label est la classe prédite
    '''
    height, width, channels = feat.shape
    feat_matrix = feat.reshape((height * width, channels))
    label = model.predict(feat_matrix)

    return label




