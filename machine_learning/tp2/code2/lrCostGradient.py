import numpy as np
from sigmoid import sigmoid

def lrCostGradient(theta, X, y, Lambda):
    """computes the gradient of the cost  w.r.t. to the parameters 
    theta for regularized logistic regression .
    """

    # préambule
    m,n = X.shape # m = 5; n = 4
    theta = theta.reshape((n,1)) # (4,1)
    gradient = 0


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

    hypothesis = sigmoid(X @ theta)
    
    gradient = (1 / m) * (X.T @ (hypothesis - y))

    gradient[1:] += (1 / m) * (Lambda * theta[1:])
    

    # =============================================================

    return gradient.flatten() # ATTENTION: à conserver pour utiliser scipy.optimization.fmin_cg
