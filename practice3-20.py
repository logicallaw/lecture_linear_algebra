import numpy as np

#Practice 3-20
A = np.array([[5,2,1], [3,6,4], [2,7,2]])
tranA = A.T

#Sol
B = A + A.T
print(B)
print(B.T)

C = A - tranA
print(C)
print(C.T)