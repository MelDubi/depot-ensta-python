# ---------------------------------------->
# import useful packages
import numpy as np
from numpy.random import rand
import scipy as sp
from scipy import interp
import pandas as pd
pd.options.display.max_colwidth = 600

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn import metrics
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
from sklearn.base import clone
from sklearn.preprocessing import label_binarize
from sklearn.metrics import roc_curve, auc
from sklearn import svm, datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.utils.multiclass import unique_labels





# import image tools
from PIL import Image
from skimage.transform import resize
import scipy.ndimage as spi

#
import warnings
warnings.filterwarnings('ignore')









# ---------------------------------------->
# This function loads raw data from the dataSet directory or scatFeatures from matfile

# PATH des fichiers de données et gestion de l'environnement sous google colab
import sys
IN_COLAB = 'google.colab' in sys.modules
if IN_COLAB:
    DATASET_PATH = 'gdrive/My Drive/Colab Notebooks/ex06_supervised_seabedClassification/dataset/imgs/'
    LABEL_PATH = 'gdrive/My Drive/Colab Notebooks/ex06_supervised_seabedClassification/dataset/labels/labels.csv'
    SCATFEAT_PATH = r'gdrive/My Drive/Colab Notebooks/ex06_supervised_seabedClassification/dataset/imdb_200x200_SmallSonarTex_db_6classes_scatValOnly.mat'
else:
    IN_COLAB = False
    DATASET_PATH = r'./dataset/imgs/'
    LABEL_PATH = r'./dataset/labels/labels.csv'
    SCATFEAT_PATH = r'./dataset/imdb_200x200_SmallSonarTex_db_6classes_scatValOnly.mat'

def importData(feature_type):


    # Charger le fichier CSV
    dataset_df = pd.read_csv(LABEL_PATH)

    # We add another column to the labels dataset to identify image path
    dataset_df['image_path'] = dataset_df.apply(lambda row: (DATASET_PATH + row["id"]), axis=1)

    if (feature_type == 'raw'):

        feature_values = np.array([plt.imread(img).reshape(40000,) for img in dataset_df['image_path'].values.tolist()])
    elif (feature_type == 'scat'):
        # Si on remplace par les descripteurs du scattering operator
        a = sp.io.loadmat(SCATFEAT_PATH)
        feature_values = a['featVal']

    print(feature_values.shape)

    # Récupération des labels
    label_names = dataset_df['seafloor']

    return feature_values, label_names, dataset_df


# ---------------------------------------->
# This function prepares a random batch from the dataset
def load_batch(dataset_df, batch_size = 25):
    batch_df = dataset_df.loc[np.random.permutation(np.arange(0,
                                                              len(dataset_df)))[:batch_size],:]
    return batch_df


# ---------------------------------------->
# This function plots sample images in specified size and in defined grid
def plot_batch(images_df, grid_width, grid_height, im_scale_x, im_scale_y):

    DATASET_PATH = r'./dataset/imgs/'
    LABEL_PATH = r'./dataset/labels/labels.csv'

    f, ax = plt.subplots(grid_width, grid_height)
    f.set_size_inches(6, 6)

    img_idx = 0
    for i in range(0, grid_width):
        for j in range(0, grid_height):
            ax[i][j].axis('off')
            ax[i][j].set_title(images_df.iloc[img_idx]['seafloor'][:10])

            # resize image
            # ttt = sp.misc.imresize(ttt,(im_scale_x,im_scale_y)) # scipy version deprecated

            ttt = plt.imread(DATASET_PATH + images_df.iloc[img_idx]['id'])
            ttt = resize(ttt,(im_scale_x,im_scale_y)) # skimage version


            # ttt = Image.open(DATASET_PATH + images_df.iloc[img_idx]['id'])
            # ttt = ttt.resize((im_scale_x,im_scale_y), Image.ANTIALIAS) # PIL version


            ax[i][j].imshow(ttt)

            img_idx += 1

    # plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0.1)






# ---------------------------------------->
#
def plot_confusion_matrix(y_true, y_pred, classes,
                          normalize=False,
                          title=None,
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if not title:
        if normalize:
            title = 'Normalized confusion matrix'
        else:
            title = 'Confusion matrix, without normalization'

    # Compute confusion matrix
    cm = confusion_matrix(y_true, y_pred)
    # Only use the labels that appear in the data
    classes = classes[unique_labels(y_true, y_pred)]
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    fig, ax = plt.subplots()
    im = ax.imshow(cm, interpolation='nearest', cmap=cmap)
    ax.figure.colorbar(im, ax=ax)
    # We want to show all ticks...
    ax.set(xticks=np.arange(cm.shape[1]),
           yticks=np.arange(cm.shape[0]),
           # ... and label them with the respective list entries
           xticklabels=classes, yticklabels=classes,
           title=title,
           ylabel='True label',
           xlabel='Predicted label')

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, format(cm[i, j], fmt),
                    ha="center", va="center",
                    color="white" if cm[i, j] > thresh else "black")
    fig.tight_layout()
    return ax


# ---------------------------------------->

def get_metrics(true_labels, predicted_labels):
    print('Accuracy:', np.round(
        metrics.accuracy_score(true_labels,
                               predicted_labels),
        4))
    print('Precision:', np.round(
        metrics.precision_score(true_labels,
                                predicted_labels,
                                average='weighted'),
        4))
    print('Recall:', np.round(
        metrics.recall_score(true_labels,
                             predicted_labels,
                             average='weighted'),
        4))
    print('F1 Score:', np.round(
        metrics.f1_score(true_labels,
                         predicted_labels,
                         average='weighted'),
        4))

# ---------------------------------------->
#
def train_predict_model(classifier,
                        train_features, train_labels,
                        test_features, test_labels):
    # build model
    classifier.fit(train_features, train_labels)
    # predict using model
    predictions = classifier.predict(test_features)
    return predictions

# ---------------------------------------->
#
def display_confusion_matrix(true_labels, predicted_labels, classes=[1, 0]):
    total_classes = len(classes)
    level_labels = [total_classes * [0], list(range(total_classes))]

    cm = metrics.confusion_matrix(y_true=true_labels, y_pred=predicted_labels,
                                  labels=classes)
    cm_frame = pd.DataFrame(data=cm,
                            columns=pd.MultiIndex(levels=[['Predicted:'], classes],
                                                  labels=level_labels),
                            index=pd.MultiIndex(levels=[['Actual:'], classes],
                                                labels=level_labels))
    print(cm_frame)

# ---------------------------------------->
#

def display_classification_report(true_labels, predicted_labels, classes=[1, 0]):
    report = metrics.classification_report(y_true=true_labels,
                                           y_pred=predicted_labels,
                                           labels=classes)
    print(report)

# ---------------------------------------->
#

def display_model_performance_metrics(true_labels, predicted_labels, classes=[1, 0]):
    print('Model Performance metrics:')
    print('-' * 30)
    get_metrics(true_labels=true_labels, predicted_labels=predicted_labels)
    print('\nModel Classification report:')
    print('-' * 30)
    display_classification_report(true_labels=true_labels, predicted_labels=predicted_labels,
                                  classes=classes)
    print('\nPrediction Confusion Matrix:')
    print('-' * 30)
    display_confusion_matrix(true_labels=true_labels, predicted_labels=predicted_labels,
                             classes=classes)



# ---------------------------------------->
#
if __name__ == '__main__':

    feature_type = 'raw'  # 'raw' | 'scat'
    feature_values, label_names, dataset_df = importData(feature_type)


    # Récupération des labels
    label_names = dataset_df['seafloor']
    label_names_unique = label_names.unique()

    #  transformation des labels selon différents codages
    # indices
    le = preprocessing.LabelEncoder()
    le.fit(label_names_unique)
    labelIndices_unique = le.transform(label_names_unique)
    labelIndices = le.transform(label_names)


    # enc indices to  one-hot-encoding
    encInd2Ohe = preprocessing.OneHotEncoder(sparse=False)
    encInd2Ohe.fit(labelIndices_unique.reshape(-1, 1))
    labelOhe = encInd2Ohe.transform(labelIndices.reshape(-1, 1))

    # enc labelNames to  one-hot-encoding
    encName2Ohe = preprocessing.OneHotEncoder(sparse=False)
    encName2Ohe.fit(label_names_unique.reshape(-1, 1))
    labelOhe2 = encName2Ohe.transform(label_names.reset_index(drop=True).values.reshape(-1, 1))

    # one-hot-encoding avec pandas
    label_ohe = pd.get_dummies(label_names.reset_index(drop=True)).values

