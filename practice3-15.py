import numpy as np

#Practice 3-15
A = np.array([[1,-3], [2,-4]])
B = np.array([[-2,5], [-1,3]])

inverseA = np.linalg.inv(A)
inverseB = np.linalg.inv(B)

multAB = np.matmul(A, B)
inverseMultAB = np.linalg.inv(multAB)

mult4A = 4 * A
inverseMult4A = np.linalg.inv(mult4A)


# Sol
## problem 1
print(inverseA)
print(inverseB)

## problem 2
print(inverseMultAB)

## problem 3
print(inverseMult4A)

## problem 4
print(np.linalg.inv(np.linalg.matrix_power(A, 2)))
print(np.linalg.matrix_power(inverseA, 2))