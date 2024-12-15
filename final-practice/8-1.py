import numpy as np

A = np.array([[2,3], [3,-6]])

w, x = np.linalg.eig(A)

print("Eigenvalue of A:", w)
print("Eigenvector of A:", x)