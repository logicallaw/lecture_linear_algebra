import numpy as np

A = np.array([[1,2,3],[4,1,5],[2,5,6]])
B = np.array([[3,6,9], [4,1,5],[2,5,6]])
C = np.array([[3,2,3],[12,1,5],[6,5,6]])

print("B is ", 3 * (np.linalg.det(A)))
print("C is ", 3 * (np.linalg.det(A)))