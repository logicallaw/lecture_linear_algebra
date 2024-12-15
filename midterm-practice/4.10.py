import numpy as np

A = np.array([[1,2,1], [3,2,1], [1,3,5]])
B = np.array([[3,1,2], [2,4,1], [4,5,1]])
AB = np.matmul(A, B)
print(np.linalg.det(AB))
print(np.linalg.det(A) * np.linalg.det(B))