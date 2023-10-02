import numpy as np
from sigmoid import sigmoid

def costFunction(theta, X, y):
    """ computes the cost of using theta as the
    parameter for logistic regression."""

	# Initialize some useful values
    m,n = X.shape   # number of training examples and parameters
    theta = theta.reshape((n,1)) # due to the use of fmin_tnc

    J = 0.
    
    # ====================== YOUR CODE HERE ======================
    # Instructions: Compute the cost of a particular choice of theta.
    #               You should set J to the cost.
    #
    

    
        
    # =============================================================
    
    return J

