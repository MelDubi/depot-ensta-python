import numpy as np
from computeCost import computeCost

def gradientDescent(X, y, theta, alpha, num_iters):  
    """
     Performs gradient descent to learn theta
       theta, cost_history, theta_history = gradientDescent(X, y, theta, alpha, num_iters) updates theta by
       taking num_iters gradient steps with learning rate alpha
    """
    # Initialize some useful values
    m = y.size  # number of training examples
    n = theta.size # number of parameters
    cost_history = np.zeros(num_iters) # cost over iters
    theta_history = np.zeros((n,num_iters)) # theta over iters

    for n_iter in range(num_iters):
    #   ====================== YOUR CODE HERE ======================
    # Instructions: Perform a single gradient step on the parameter vector
    #               theta.
    #
    # Hint: While debugging, it can be useful to print out the values
    #       of the cost function (computeCost) and gradient here.
        
        for j in range(n):
            res = 0
            for i in range(m):
                res += (X[i].T @ theta - y[i]) * X[i][j]
            
            theta[j] = theta[j] - alpha * (1/m) * res

        cost_history[n_iter] = computeCost(X, y, theta)
        theta_history[:,n_iter] = theta.reshape((2,))
    
    #   ============================================================

    return theta, cost_history, theta_history
