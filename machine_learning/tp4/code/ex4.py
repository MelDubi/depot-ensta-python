#%% Import package
import scipy.io
import matplotlib.pyplot as plt
import numpy as np

from linearRegCostFunction import linearRegCostFunction
from trainLinearReg import trainLinearReg
from learningCurve import learningCurve
from polyFeatures import polyFeatures
from featureNormalize import featureNormalize
from plotFit import plotFit
from validationCurve import validationCurve




#%% Machine Learning Online Class
#  Exercise 4 | Regularized Linear Regression and Bias-Variance
#
#  Instructions
#  ------------
# 
#  This file contains code that helps you get started on the
#  exercise. You will need to complete the following functions:
#
#     linearRegCostFunction.py
#     learningCurve.py
#     validationCurve.py
#
#  For this exercise, you will not need to change any code in this file,
#  or any other files other than those mentioned above.
#

#%% =========== Part 1: Loading and Visualizing Data =============
#  We start the exercise by first loading and visualizing the dataset. 
#  The following code will load the dataset into your environment and plot
#  the data.
#

# Load Training Data
print('Loading and Visualizing Data ...')

# Load from ex4data1: 
# You will have X, y, Xval, yval, Xtest, ytest in your environment
data = scipy.io.loadmat('ex4data1.mat')
X = data['X']  # Dimensions de X, y, etc..????
y = data['y']  #
Xval = data['Xval']
yval = data['yval']
Xtest = data['Xtest']
ytest = data['ytest']

# m = Number of examples
m,n = X.shape

# Plot training data
plt.figure()
plt.scatter(X, y, marker='x', s=60, edgecolor='r', lw=1.5)
plt.ylabel('Water flowing out of the dam (y)')            # Set the y-axis label
plt.xlabel('Change in water level (x)')     # Set the x-axis label
plt.grid()
plt.show()



#%% =========== Part 2: Regularized Linear Regression Cost =============
#  You should now implement the cost function for regularized linear 
#  regression. 
#

# initialisation: theta, Lambda
theta = np.array([[1, 1]]).T
Lambda = 1

# Add intercept
X_stack = np.column_stack((np.ones(m), X))

# Cost
J = linearRegCostFunction(X_stack, y, theta, Lambda)[0]

print('Cost at theta = [1  1]: %f \n(this value should be about 303.993192)\n' % J)





#%% =========== Part 3: Regularized Linear Regression Gradient =============
#  You should now implement the gradient for regularized linear 
#  regression.
#


# initialisation: theta, Lambda
theta = np.array([[1, 1]]).T
Lambda = 1

# Add intercept
X_stack = np.column_stack((np.ones(m), X))

# Cost
J, grad = linearRegCostFunction(X_stack, y, theta, Lambda)

print('Gradient at theta = [1  1]:  [%f %f] \n(this value should be about [-15.303016 598.250744])\n' %(grad[0], grad[1]))






#%% =========== Part 4: Train Linear Regression =============
#  Once you have implemented the cost and gradient correctly, the
#  trainLinearReg function will use your cost function to train 
#  regularized linear regression.
# 
#  Write Up Note: The data is non-linear, so this will not give a great 
#                 fit.
#

#  Train linear regression with Lambda = 0
Lambda = 0
X_stack = np.column_stack((np.ones(m), X))
theta = trainLinearReg(X_stack, y, Lambda)

#  Prediction from the learned model
pred = X_stack.dot(theta)

#  Plot fit over the data
plt.figure()
plt.scatter(X, y, marker='x', s=20, edgecolor='r', lw=1.5)
plt.ylabel('Water flowing out of the dam (y)')            # Set the y-axis label
plt.xlabel('Change in water level (x)')     # Set the x-axis label
plt.plot(X, pred, '--r', lw=2.0)
plt.grid()
plt.show()






#%% =========== Part 5: Learning Curve for Linear Regression =============
#  Next, you should implement the learningCurve function. 
#
#  Write Up Note: Since the model is underfitting the data, we expect to
#                 see a graph with "high bias" in course slides
#

Lambda = 0
X_stack = np.column_stack((np.ones(m), X))
Xval_stack = np.column_stack((np.ones(Xval.shape[0]), Xval))

error_train, error_val = learningCurve(X_stack, y, Xval_stack, yval, Lambda)

# display
plt.figure()
plt.plot(range(1,m+1), error_train, color='b', lw=2, label='Train')
plt.plot(range(1,m+1), error_val, color='r', lw=2, label='Validation')
plt.title('Learning curve for linear regression')
plt.grid()
plt.xlabel('Number of training examples')
plt.ylabel('Error')
plt.xlim(0, 13)
plt.ylim(0, 150)
plt.legend(loc='upper right', shadow=True, fontsize='x-large', numpoints=1)
plt.show()

print('Training Examples\tTrain Error\tvalidation Error')
for i in range(m):
    print('  \t%d\t\t%f\t%f' % (i, error_train[i], error_val[i]))






#%% =========== Part 6: Feature Mapping for Polynomial Regression =============
#  One solution to this is to use polynomial regression. You should now
#  complete polyFeatures to map each example into its powers
#

# set the max polynomial degree
p = 8

# Map X onto Polynomial Features and Normalize
X_poly = polyFeatures(X, p)

 # Normalize
X_poly, mu, sigma = featureNormalize(X_poly) 

# Add Ones
X_poly = np.column_stack((np.ones(m), X_poly))                   

# Map X_poly_test and normalize (using mu and sigma)
X_poly_test = polyFeatures(Xtest, p)
X_poly_test = X_poly_test - mu
X_poly_test = X_poly_test / sigma
X_poly_test = np.column_stack((np.ones(X_poly_test.shape[0]), X_poly_test))        # Add Ones

# Map X_poly_val and normalize (using mu and sigma)
X_poly_val = polyFeatures(Xval, p)
X_poly_val = X_poly_val - mu
X_poly_val = X_poly_val / sigma
X_poly_val = np.column_stack((np.ones(X_poly_test.shape[0]), X_poly_val))           # Add Ones

print('Normalized Training Example 1:')
print(X_poly[0, :])






#%% =========== Part 7: Learning Curve for Polynomial Regression =============
#  Now, you will get to experiment with polynomial regression with multiple
#  values of Lambda. The code below runs polynomial regression with 
#  Lambda = 0. You should try running the code with different values of
#  Lambda to see how the fit and learning curve change.
#

for Lambda in [0, 1, 100]:
    theta = trainLinearReg(X_poly, y, Lambda, maxiter=10)


    # Plot training data and fit
    plt.figure()
    plt.scatter(X, y, marker='x', s=10, edgecolor='r', lw=2)

    plotFit(min(X), max(X), mu, sigma, theta, p)

    plt.xlabel('Change in water level (x)')            # Set the y-axis label
    plt.ylabel('Water flowing out of the dam (y)')     # Set the x-axis label
    # plt.plot(X, np.column_stack((np.ones(m), X)).dot(theta), marker='_',  lw=2.0)
    plt.title('Polynomial Regression Fit (Lambda = %f)' % Lambda)
    plt.grid()
    plt.show()


    # Plot Learning curves (Error vs Number of training examples)
    error_train, error_val = learningCurve(X_poly, y, X_poly_val, yval, Lambda)
    plt.figure()
    plt.plot(range(1,m+1), error_train, color='b', lw=2, label='Train')
    plt.plot(range(1,m+1), error_val, color='r', lw=2, label='Validation')
    plt.title('Polynomial Regression Learning Curve (Lambda = %f)' % Lambda)
    plt.xlabel('Number of training examples')
    plt.ylabel('Error')
    plt.xlim(0, 13)
    plt.ylim(0, 150)
    plt.legend()
    plt.grid()

    print('Polynomial Regression (Lambda = %f)\n\n' % Lambda)
    print('# Training Examples\tTrain Error\tvalidation Error')
    for i in range(m):
        print('  \t%d\t\t%f\t%f' % (i, error_train[i], error_val[i]))





#%% =========== Part 8: Validation for Selecting Lambda =============
#  You will now implement validationCurve to test various values of 
#  Lambda on a validation set. You will then use this to select the
#  "best" Lambda value.
#

Lambda_vec, error_train, error_val = validationCurve(X_poly, y, X_poly_val, yval)

plt.figure()
plt.plot(Lambda_vec, error_train, 'b', lw=2, label='Train')
plt.plot(Lambda_vec, error_val, 'r', lw=2, label='Validation')
plt.legend()#'Train', 'validation'
plt.xlabel('Lambda')
plt.ylabel('Error')
plt.grid()

print('Lambda\tTrain Error\tValidation Error')
for i in range(Lambda_vec.size):
    print(' %f\t%f\t%f' % (Lambda_vec[i], error_train[i], error_val[i]))


#%% =========== Part 9:  Computing test set error =============
# Plot training data
plt.figure()
plt.scatter(Xtest, ytest, marker='x', s=60, edgecolor='r', lw=1.5)
plt.ylabel('Water flowing out of the dam (ytest)')            # Set the y-axis label
plt.xlabel('Change in water level (Xtest)')     # Set the x-axis label
plt.grid()
plt.show()


# calc test error
Lambda = 3
theta = trainLinearReg(X_poly, y, Lambda, maxiter=100)

Jtest, _ = linearRegCostFunction(X_poly_test, ytest, theta, 0)
print("The test set error is:", Jtest)



#%% =========== Part 10:  Plotting learning curves with randomly selected examples =============
num_iterations = 50
Lambda = 0.01
errors_train = []
errors_val = []

i = np.random.randint(5, len(X) + 1)

for _ in range(num_iterations):
    i_train = np.random.choice(len(X), i, replace=False)
    i_val = np.random.choice(len(Xval), i, replace=False)
    
    X_random = X_poly[i_train]  
    y_random = y[i_train]
    X_val_random = X_poly_val[i_val] 
    y_val_random = yval[i_val]

    X_random = np.column_stack((np.ones(X_random.shape[0]), X_random))
    X_val_random = np.column_stack((np.ones(X_val_random.shape[0]), X_val_random))
        
    theta = trainLinearReg(X_random, y_random, Lambda, maxiter=100)
    error_train, error_val = learningCurve(X_random, y_random, X_val_random, y_val_random, Lambda)

    errors_train.append(error_train)
    errors_val.append(error_val)
    
error_train = np.mean(np.array(errors_train), axis=0)
error_val = np.mean(np.array(errors_val), axis=0)

plt.figure()
plt.plot(range(1,i+1), error_train, color='b', lw=2, label='Train')
plt.plot(range(1,i+1), error_val, color='r', lw=2, label='Validation')
plt.title('Polynomial Regression Learning Curve (Lambda = %f)' % Lambda)
plt.xlabel('Number of training examples')
plt.ylabel('Error')
plt.xlim(0, i+1)
plt.ylim(0, 110)
plt.legend()
plt.grid()
# %%
