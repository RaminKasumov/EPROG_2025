def derivative(c):
    return [i * c[i] for i in range(1, len(c))]

print(derivative([1, 2, 3, 4]))