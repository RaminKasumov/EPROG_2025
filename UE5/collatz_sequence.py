def collatz(n, m):
    seq = [n]
    steps_to_one = None

    for i in range(1, m):
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        seq.append(n)
        if n == 1 and steps_to_one is None:
            steps_to_one = i

    return seq, steps_to_one

print(collatz(6, 20))