import numpy as np
A = np.array([[3, 2],
[6, 5]])
B = np.array([[4, 8],
[2, 5]])
C = np.array([[0, 3],
[7, 1]])
O = np.zeros([2, 2])
M = np.block([[A, O],
[C, B]])

print(np.linalg.det(A) * np.linalg.det(B))
print(np.linalg.det(M))