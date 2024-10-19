import numpy as np

A = np.diag([3,4,5,2])
B = np.diag([1,3,2,5])
C = np.array([[1,2,3,4], [2,3,4,5], [3,4,2,1], [3,2,1,0]])
print(A + B)
print(np.matmul(A,B))
print(np.matmul(A,C))
