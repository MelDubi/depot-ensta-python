
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

    plt.subplot(2, 2, 1)
    plt.imshow(img73)
    plt.title('Image 1973')

    plt.subplot(2, 2, 2)
    plt.imshow(img87)
    plt.title('Image 1987')

    img73 = img73[60:-40, :, :]
    img87 = img87[60:-40, :, :]

    plt.subplot(2, 2, 3)
    plt.imshow(img73)
    plt.title('Cropped Image 1973')

    plt.subplot(2, 2, 4)
    plt.imshow(img87)
    plt.title('Cropped Image 1987')

    plt.show()

    return 0, img73, img87
    