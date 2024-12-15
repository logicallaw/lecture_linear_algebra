import numpy as np

A = np.array([[5,2], [2,5]])
D = np.array([[7,0], [1,8]])
O = np.zeros([2,2])
B = np.array([[4,2], [5,3]])

M = np.block([[A, D], [O, B]])

print(np.linalg.det(A) * np.linalg.det(B))
print(np.linalg.det(M))
