def recaman_iterative(n):
    seq = [0]
    used = {0}

    for i in range(1, n + 1):
        candidate = seq[-1] - i
        if candidate > 0 and candidate not in used:
            seq.append(candidate)
        else:
            seq.append(seq[-1] + i)
        used.add(seq[-1])
    return seq[n]

def recaman_recursive(n, seq=None, used=None):
    if seq is None:
        seq = [0]
        used = {0}

    if len(seq) > n:
        return seq[n]

    i = len(seq)
    candidate = seq[-1] - i
    if candidate > 0 and candidate not in used:
        seq.append(candidate)
    else:
        seq.append(seq[-1] + i)
    used.add(seq[-1])

    return recaman_recursive(n, seq, used)

# Which version handles larger n?
# → iterative version, because recursive calls hit recursion depth limit.