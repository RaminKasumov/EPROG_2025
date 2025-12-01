def primes(n):
    primes_list = []
    for i in range(2, n + 1):
        if all(i % p != 0 for p in primes_list):
            primes_list.append(i)
    return primes_list

print(primes(30))