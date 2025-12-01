from math import sqrt

def fibonacci_list(n=20):
    phi = (1 + sqrt(5)) / 2
    return [round((phi**k - (-phi)**(-k)) / sqrt(5)) for k in range(1, n+1)]

fib = fibonacci_list()
check = all(fib[i] == fib[i - 1] + fib[i - 2] for i in range(2, len(fib)))

print(fib)
print("Fibonacci property holds:", check)