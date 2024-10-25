import numpy as np

#1
A = np.array([[1,1,2],[1,2,3],[1,1,3]])
b = np.array([[-3],[-4],[-6]])
invA = np.linalg.inv(A)

x = np.matmul(invA, b)
# print(x)

#3
A = np.array([[1,3,-1],[2,5,1],[1,1,1]])
b = np.array([[1],[5],[3]])
invA = np.linalg.inv(A)

x = np.matmul(invA, b)
# print(x)

#4
A = np.array([[2,1,1,-2],[3,-2,1,-6],[1,1,-1,-1],[5,-1,2,-8]])
b = np.array([[1,-2,-1,3]])
invA = np.linalg.inv(A)
b = b.T

x = np.matmul(invA, b)
# print(x)

#5
A = np.array([[1,-3,4],[2,-5,7],[0,-1,2]])
B = np.eye(3)
invA = np.linalg.inv(A)

x = np.matmul(invA, B)
print(x)

#6
A = np.array([[1,1,2], [2,4,-3], [3,6,-5]])
B = np.eye(3)
invA = np.linalg.inv(A)

x = np.matmul(invA, B)
print(x)