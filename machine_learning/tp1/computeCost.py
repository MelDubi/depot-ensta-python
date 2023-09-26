import numpy as np

def computeCost(X, y, theta):  
    """
       computes the cost of using theta as the parameter for linear 
       regression to fit the data points in X and y
    """
    m = y.size
    J = 0

    # ====================== YOUR CODE HERE ======================
    # Instructions: Compute the cost of a particular choice of theta
    
    res = 0
    for i in range(0, m):
        res += ((theta[0]+theta[1]*(X[i][1])) - y[i])**2

    J = (1/(2*m))*res
	#   ============================================================

    return J
