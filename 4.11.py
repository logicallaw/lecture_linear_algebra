import numpy as np

A = np.array([[1, 0, 0, 0, 0],
[-1, 3, 0, 0, 0],
[-2,
-6, 2, 0, 0],
[-3,
-3, 2, 5, 0],
[-5, 7,
-3,
-2, 2]])

print(np.linalg.det(A))