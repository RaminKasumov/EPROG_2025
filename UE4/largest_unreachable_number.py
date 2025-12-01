def largest_unreachable(a, b, c):
    limit = a * b * c
    reachable = {a*i + b*j + c*k for i in range(limit//a + 1)
                 for j in range(limit//b + 1)
                 for k in range(limit//c + 1)}
    return max(set(range(limit)) - reachable)

print(largest_unreachable(7, 11, 13))