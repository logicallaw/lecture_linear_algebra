import numpy as np

#Practice 3-18
A = np.array([[1,2], [3,4]])
B = np.array([[-2,4], [1,3]])

# Sol

## Problem 1
print(A)
print(A.T.T)

## Problem 2
print((A + B).T)
print(A.T + B.T)

## Problem 3
print(np.matmul(A, B).T)
print(np.matmul(B.T, A.T))

## Problem 4
print((3 * A).T)
print(3 * A.T)

## Problem 5
print(np.linalg.inv(A.T))
print((np.linalg.inv(A)).T)