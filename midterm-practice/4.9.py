import numpy as np

E = np.eye(3)
E[[1,2]] = E[[2,1]]
A = np.array([[1,2,3], [0,3,4], [0,0,5]])
EA = np.matmul(E, A)

print(np.linalg.det(EA))
print(np.linalg.det(E) * np.linalg.det(A))