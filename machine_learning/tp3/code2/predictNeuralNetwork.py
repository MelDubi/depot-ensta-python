import numpy as np

from sigmoid import sigmoid

def predictNeuralNetwork(Theta1, Theta2, X):

# Useful values
    m, _ = X.shape
    num_labels, _ = Theta2.shape
    # Input Layer
    a1 = X

    # Hidden Layer
    z2 = a1 @ Theta1.T
    a2 = sigmoid(z2)
    
    # Add column 1's 
    a2 = np.hstack((np.ones((a2.shape[0], 1)), a2))

    # Output Layer
    z3 = a2 @ Theta2.T
    hypothesis = np.argmax(sigmoid(z3), axis=1) + 1 # on ajoute 1 pour faire l'offset
    
    return hypothesis

