def primes(n):
    primes_list = []
    for i in range(2, n + 1):
        if all(i % p != 0 for p in primes_list):
            primes_list.append(i)
    return primes_list

def pfz(n):
    factors = {}
    for p in primes(n):
        while n % p == 0:
            factors[p] = factors.get(p, 0) + 1
            n //= p
        if n == 1:
            break
    return factors

print(pfz(360))