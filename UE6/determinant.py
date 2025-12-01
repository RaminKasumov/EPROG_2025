def submatrix(matrix, col_to_remove):
    return [
        [matrix[i][j] for j in range(len(matrix)) if j != col_to_remove]
        for i in range(1, len(matrix))
    ]

def determinant(matrix):
    n = len(matrix)

    if n == 1:
        return matrix[0][0]

    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for j in range(n):
        sign = (-1) ** (1 + (j + 1))
        det += sign * matrix[0][j] * determinant(submatrix(matrix, j))

    return det

A = [[1, 2, 3],
     [0, 4, 5],
     [1, 0, 6]]

print(determinant(A))