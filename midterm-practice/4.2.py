import numpy as np

A = np.array([[1,2,3], [3,2,1], [4,4,5]])

def minor(M, i, j):
    M = np.delete(M, i-1, 0)
    M = np.delete(M, j-1, 1)
    return M

A11 = minor(A, 1, 1)
A12 = minor(A, 1, 2)
A21 = minor(A, 2, 1)
A22 = minor(A, 2, 2)

print(np.linalg.det(A11))
print(np.linalg.det(A12))
print(np.linalg.det(A21))
print(np.linalg.det(A22))
