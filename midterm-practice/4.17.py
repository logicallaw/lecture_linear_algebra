import numpy as np

A = np.array([[1,4,3],[2,3,2],[4,2,5]])
print(np.linalg.det(A) * np.eye(3))