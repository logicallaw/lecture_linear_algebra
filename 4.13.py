import numpy as np

A = np.array([[1,2],[2,5]])
B = np.array([[3,4], [9,7]])
O = np.zeros([2,2])
I = np.eye(2)

M = np.block([[A, B], [O, I]])
print(np.linalg.det(A))
print(np.linalg.det(M))