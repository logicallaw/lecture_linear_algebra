import numpy as np

I = np.eye(3)
I[[0,1]] = I[[1,0]]
E1 = I
print(np.linalg.det(E1))

I = np.eye(4)
I[2] = 5 * I[2]
E2 = I
print(E2)
print(np.linalg.det(E2))

I = np.eye(4)
I[2,] = I[2] + 3*I[0]
E3 = I
print(np.linalg.det(E3))