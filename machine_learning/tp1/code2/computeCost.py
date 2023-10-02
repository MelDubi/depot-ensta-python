import numpy as np

def computeCost(X, y, theta):  
    """
       computes the cost of using theta as the parameter for linear 
       regression to fit the data points in X and y
    """

    # ====================== YOUR CODE HERE ======================
    # Instructions: Compute the cost of a particular choice of theta
    m = y.size

    # Compute hypothesis
    hypothesis = np.dot(X, theta)

    # Compute error between hypothesis and prediction
    error = (hypothesis-y) ** 2

    # Compute Cost
    J = (1 / (2 * m)) * np.sum(error)

#   ============================================================

    return J
