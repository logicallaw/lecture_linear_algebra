import numpy as np

A = np.array([[2,3], [4,1]])
B = np.array([[2,3], [4,6]])
C = np.array([[1,2,3], [3,2,1], [4,4,5]])
D = np.array([[1,2,3], [3,2,4], [2,4,6]])

print(np.linalg.det(A))
print(np.linalg.det(B))
print(np.linalg.det(C))
print(np.linalg.det(D))