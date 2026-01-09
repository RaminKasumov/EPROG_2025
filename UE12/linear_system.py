import numpy as np

A = np.array([
    [1, 1, 2],
    [2, 3, 1],
    [7, 9, -3]
])

b = np.array([3, 5, 0])

x_direct = np.linalg.solve(A, b)

x_inverse = np.linalg.inv(A) @ b

print("Direct solution:", x_direct)
print("Inverse solution:", x_inverse)

print("Check A @ x:", A @ x_direct)
print("Check A @ x:", A @ x_inverse)