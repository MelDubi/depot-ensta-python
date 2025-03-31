
#%% package
import numpy as np
import matplotlib.pyplot as plt

from loadImages import loadImages
from selectFeatureVectors import selectFeatureVectors
from displayFeatures2d import displayFeatures2d
from displayFeatures3d import displayFeatures3d


#%% def preprocessing
def preprocessing():
    img73, img87 = loadImages()

    img73 = img73[60:-40, :, :]
    img87 = img87[60:-40, :, :]

    feat, nbPix, nbFeat = selectFeatureVectors(img73, 500)
    print(f"Number of training data: {nbPix}")
    """ Number of training data: 1714 """

    displayFeatures2d(feat)
    displayFeatures3d(feat)

    return feat, img73, img87
    