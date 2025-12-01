def sieve_of_eratosthenes(n):
    if n < 2:
        return []

    numbers = list(range(2, n+1))
    primes = []

    while numbers:
        p = numbers.pop(0)
        primes.append(p)
        numbers = [x for x in numbers if x % p != 0]

    return primes

print(sieve_of_eratosthenes(50))