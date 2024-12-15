import numpy as np

print("np.vstack method")
v1 = np.array([1,2,3])
v2 = np.array([4,5,6])
v3 = np.array([7,8,9])

A = np.vstack([v1, v2, v3])
print(A)

B = np.column_stack([v1,v2,v3])
print(B)

C = np.array([[1,2],[3,4],[5,6]])

D = np.column_stack([C, v3])
print(D)