import numpy as np
from sigmoid import sigmoid


def costFunctionReg(theta, X, y, Lambda):
    """
    Compute cost and gradient for logistic regression with regularization

    computes the cost of using theta as the parameter for regularized logistic regression and the
    gradient of the cost w.r.t. to the parameters.
    """
    # Initialize some useful values
    m,n = X.shape   # number of training examples and parameters
    theta = theta.reshape((n,1)) # due to the use of fmin_tnc

    J = 0.

    # ====================== YOUR CODE HERE ======================
    # Instructions: Compute the cost of a particular choice of theta.
    #               You should set J to the cost.
    #               Compute the partial derivatives and set grad to the partial
    #               derivatives of the cost w.r.t. each parameter in theta

    # =============================================================
    # Compute hypothesis
    hypothesis = sigmoid(np.dot(X, theta))

    # Compute cost
    J = (1 / m) * np.sum(-y * np.log(hypothesis) - (1 - y) * np.log(1 - hypothesis)) + (( Lambda / (2 * m)) * np.sum(theta[1:] ** 2))


    
    # =============================================================
    
    return J
