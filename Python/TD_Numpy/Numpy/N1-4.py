import numpy as np
from numpy import *
from scipy.linalg import inv
import matplotlib.pyplot as plt

A = matrix([[8,2,1,1,5],[1,9,1,3,2],[3,5,42,28,5],[1,9,1,-50,12],[6,5,3,12,-38]])
B = [42,12,28,90,32]

rank = np.linalg.matrix_rank(A)

eigenvalues, eigenvectors = linalg.eig(A)

P=eigenvectors
Pi=inv(P)
D=np.diag(np.array(eigenvalues))

A2=P*D*Pi

print(allclose(A,A2))

X = np.linalg.solve(A,B)
B2 = A.dot(X)
print(B2)