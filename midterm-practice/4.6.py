import numpy as np

A = np.array([[1,2,3],[4,1,5],[2,5,6]])
print(np.linalg.det(A))
A[1,] = A[0,] + A[1,]
print(np.linalg.det(A))

A = np.array([[1,2,3],[4,1,5],[2,5,6]])
print(np.linalg.det(A))
A[:,2] = 2 * A[:,1] + A[:,2]
print(np.linalg.det(A))