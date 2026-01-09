import numpy as np

def tridiagonal_A(n):
    A = 4 * np.eye(n)
    A += -1 * np.eye(n, k=1)
    A += -1 * np.eye(n, k=-1)
    return A

def block_matrix(n):
    A = tridiagonal_A(n)
    I = np.eye(n)

    C = np.zeros((n*n, n*n))

    for i in range(n):
        C[i*n:(i+1)*n, i*n:(i+1)*n] = A
        if i > 0:
            C[i*n:(i+1)*n, (i-1)*n:i*n] = -I
        if i < n-1:
            C[i*n:(i+1)*n, (i+1)*n:(i+2)*n] = -I

    return C