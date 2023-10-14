import numpy as np
from sigmoid import sigmoid

def lrCostFunction(theta, X, y, Lambda):
    """computes the cost of using
    theta as the parameter for regularized logistic regression.
    """

    # preambule
    m,n = X.shape # 5,4
    theta = theta.reshape((n,1)) # (4,1)

    # ====================== YOUR CODE HERE ======================
    # Instructions: Compute the cost of a particular choice of theta.
    #               You should set J to the cost.
    #
    # Hint: The computation of the cost function and gradients can be
    #       efficiently vectorized. For example, consider the computation
    #
    #           sigmoid(X @ theta) or np.dot(X, theta)
    #
    #       Each row of the resulting matrix will contain the value of the
    #       prediction for that example. You can make use of this to vectorize
    #       the cost function and gradient computations. 
    #
    hypothesis = sigmoid(np.dot(X, theta))

    # Compute cost
    J = (1 / m) * np.sum(-y * np.log(hypothesis) - (1 - y) * np.log(1 - hypothesis)) + (( Lambda / (2 * m)) * np.sum(theta[1:] ** 2))

    # =============================================================

    return J
