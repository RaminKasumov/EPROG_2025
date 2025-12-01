def matrix_properties(a):
    row_sum_norm = max(sum(abs(aij) for aij in row) for row in a)
    col_sum_norm = max(sum(abs(a[i][j]) for i in range(len(a))) for j in range(len(a[0])))
    trace = sum(a[i][i] for i in range(len(a)))
    return row_sum_norm, col_sum_norm, trace

A = [[1, -2, 3],
     [4, 5, -6],
     [-7, 8, 9]]

print(matrix_properties(A))