import numpy as np

A = np.array([[1,2,2], [3,2,4], [2,2,1]])
print(np.linalg.det(A))
print(np.linalg.det(A.T))