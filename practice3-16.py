import numpy as np

#Practice 3-16
A = np.array([[3,1], [5,2]])
B = np.array([[1,2], [3,4]])

inverseA = np.linalg.inv(A)

X = np.matmul(inverseA, B)
print(X)