import numpy as np

A = np.array([[2,3,-1], [1,8,1]])
B = np.array([[2,3], [-3,1], [1,-1]])

print(np.trace(np.matmul(A, B)))
print(np.trace(np.matmul(B,A)))