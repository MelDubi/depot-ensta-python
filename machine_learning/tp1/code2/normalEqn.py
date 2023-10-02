import numpy as np


def normalEqn(X,y):
    """ Computes the closed-form solution to linear regression
       normalEqn(X,y) computes the closed-form solution to linear
       regression using the normal equations.
    """

    # Initialize some useful values
    theta = np.linalg.inv(X.T @ X) @ X.T @ y
    # ==============================================================

    return theta
