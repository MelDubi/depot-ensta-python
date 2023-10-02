#%% ================ Introduction: load packages ================
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

import pandas as pd

from featureNormalize import featureNormalize
from gradientDescentMulti import gradientDescentMulti
from normalEqn import normalEqn



#%% ================ Part 1: Feature Normalization ================

print('\n -------------------------- \n')
print('Loading data ...')

# Load Data
path = 'ex1data2.txt'  
data = pd.read_csv(path, header=None, names=['HouseSize', 'NbOfBedrooms', 'Price'])  
data.head()  

# Résumé des données
data.describe()  

# set X (training data) and y (target variable)
nbCol = data.shape[1]  
X = data.iloc[:,0:nbCol-1]  
y = data.iloc[:,nbCol-1:nbCol]  

# convert from data frames to numpy arrays
X = np.array(X.values)  
y = np.array(y.values)
m = X.shape[0]



# Print out some data points
print('\n -------------------------- \n')
print('First 10 examples from the dataset:')
print(np.column_stack( (X[:10], y[:10]) ))


# Scale features and set them to zero mean
print('\n -------------------------- \n')
print('Normalizing Features ...')

X, mu, sigma = featureNormalize(X)
print('[mu] [sigma]')
print(mu, sigma)

# Add intercept term to X
X = np.concatenate((np.ones((m, 1)), X), axis=1)


#%% ================ Part 2: Gradient Descent ================
#
# ====================== YOUR CODE HERE ======================
# Instructions: We have provided you with the following starter
#               code that runs gradient descent with a particular
#               learning rate (alpha).
#
#               Your task is to first make sure that your functions -
#               computeCost and gradientDescent already work with
#               this starter code and support multiple variables.
#
#               After that, try running gradient descent with
#               different values of alpha and see which one gives
#               you the best result.
#
#               Finally, you should complete the code at the end
#               to predict the price of a 1650 sq-ft, 3 br house.
#
#
# Hint: At prediction, make sure you do the same feature normalization.
#

print('\n -------------------------- \n')
print('Running gradient descent ...')

# Choose some alpha value (Learning rate)
num_iters = 50

# J1
alpha_J1 = 0.07

# J2
alpha_J2 = 0.052

# J3
alpha_J3 = 0.09


# Init Theta
n = X.shape[1]
theta = np.zeros((n,1))
theta2 = np.zeros((n,1))
theta3 = np.zeros((n,1))

# Run Gradient Descent with alpha_J1
theta, cost_history, theta_history = gradientDescentMulti(X, y, theta, alpha_J1, num_iters)

# Run Gradient Descent with alpha_J1
theta2, cost_history2, theta_history2 = gradientDescentMulti(X, y, theta2, alpha_J2, num_iters)

# Run Gradient Descent with alpha_J1
theta3, cost_history3, theta_history3 = gradientDescentMulti(X, y, theta3, alpha_J3, num_iters)

# Plot the convergence graph
fig = plt.figure()
ax = plt.gca()
ax.plot(np.arange(num_iters), cost_history, color="red", linewidth=2.0, linestyle="-")
ax.plot(np.arange(num_iters), cost_history2, color="green", linewidth=2.0, linestyle="-")
ax.plot(np.arange(num_iters), cost_history3, color="blue", linewidth=2.0, linestyle="-")
ax.grid()
ax.set_xlabel('iteration number')  
ax.set_ylabel(r'Cost J($\theta$)')  
ax.set_title('Error vs. Training Epoch (number of iters)')  
fig.show()


# Display gradient descent's result
print('\n -------------------------- \n')
print('Theta computed from gradient descent: ')
print(theta2)

# Estimate the price of a 1650 sq-ft, 3 br house
new_house = np.array([[1650, 3]])
norm_newHouse = (new_house-mu)/sigma
norm_newHouse = np.concatenate((np.ones((1,1)),norm_newHouse), axis=1)
price = norm_newHouse.dot(theta2)


# price = np.array(price).dot(theta)

print('\n -------------------------- \n')
print('Predicted price of a 1650 sq-ft, 3 br house')
print('(using gradient descent): ')
print(price)





#%% ================ Part 3: Normal Equations ================

# ====================== YOUR CODE HERE ======================
# Instructions: The following code computes the closed form
#               solution for linear regression using the normal
#               equations. You should complete the code in
#               normalEqn.py
#
#               After doing so, you should complete this code
#               to predict the price of a 1650 sq-ft, 3 br house.
#
print('\n -------------------------- \n')
print('Solving with normal equations...')

# Load Data
data = np.loadtxt('ex1data2.txt', delimiter=',')
path = 'ex1data2.txt'  
data = pd.read_csv(path, header=None, names=['HouseSize', 'NbOfBedrooms', 'Price'])  
data.head()  


# set X (training data) and y (target variable)
nbCol = data.shape[1]  
X = data.iloc[:,0:nbCol-1]  
y = data.iloc[:,nbCol-1:nbCol]  

# convert from data frames to numpy arrays
X = np.array(X.values)  
y = np.array(y.values)
m = X.shape[0]


# Add intercept term to X
X = np.concatenate((np.ones((m, 1)), X), axis=1)

# Calculate the parameters from the normal equation
theta = normalEqn(X, y)

# Display normal equation's result
print('Theta computed from the normal equations:')
print(' %s \n' % theta)

# Estimate the price of a 1650 sq-ft, 3 br house
price = np.array([[1, 1650, 3 ]]).dot(theta)


print("Predicted price of a 1650 sq-ft, 3 br house ")
print('(using normal equations):\n $%f\n' % price[:, 1])
# ============================================================
