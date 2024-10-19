import numpy as np

A = np.array([[1,2,3], [4,1,5],[2,5,6]])
B = np.array([[1,3,3],[4,2,5],[2,1,6]])
C = np.array([[1,2,3], [1,5,2], [2,5,6]])
print("det(D) is ", (np.linalg.det(A) + np.linalg.det(B)))
print("det(E) is ", (np.linalg.det(A) + np.linalg.det(C)))
