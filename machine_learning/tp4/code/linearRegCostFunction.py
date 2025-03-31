import numpy as np
def linearRegCostFunction(X, y, theta, Lambda):
    """computes the
    cost of using theta as the parameter for linear regression to fit the
    data points in X and y. Returns the cost in J and the gradient in grad
    """
# Initialize some useful values

    m,n = X.shape # number of training examples
    theta = theta.reshape((n,1)) # in case where theta is a vector (n,) 

    # ====================== YOUR CODE HERE ======================
    # Instructions: Compute the cost and gradient of regularized linear 
    #               regression for a particular choice of theta.
    #
    #               You should set J to the cost and grad to the gradient.
    #

    h = X @ theta
    J = (1/(2*m)) * np.sum((h - y) ** 2) + (Lambda/(2*m)) * np.sum(theta[1:] ** 2)

    grad = (1/m) * (X.T @ (h - y))
    grad[1:] += (Lambda/m * theta[1:])

    # =========================================================================

    return J.flatten(), grad.flatten()