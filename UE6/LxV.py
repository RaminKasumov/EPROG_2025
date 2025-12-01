def LxV(L, vector):
    n = len(L)
    result = [0] * n

    for i in range(n):
        s = 0
        for j in range(i + 1):
            s += L[i][j] * vector[j]
        result[i] = s

    return result

L = [[2, 0, 0],
     [3, 1, 0],
     [4, 2, 5]]

vector = [1, 2, 3]

print(LxV(L, vector))