def reverse_rows_shared(matrix):
    return matrix[::-1]

def reverse_rows_independent(matrix):
    return [row[:] for row in matrix[::-1]]

A = [[1,2],
     [3,4],
     [5,6]]

B = reverse_rows_shared(A)
C = reverse_rows_independent(A)

A[0][0] = 99

print("A:", A)
print("B (shared reference):", B)
print("C (independent copy):", C)