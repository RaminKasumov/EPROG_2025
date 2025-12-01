from collections import defaultdict

def lucifer_solution():
    pairs = [(x, y) for x in range(2, 100) for y in range(x+1, 100)]

    product_groups = defaultdict(list)
    for x, y in pairs:
        product_groups[x*y].append((x, y))

    pairs = [p for p in pairs if len(product_groups[p[0]*p[1]]) > 1]

    sum_groups = defaultdict(list)
    for x, y in pairs:
        sum_groups[x+y].append((x, y))
    pairs = [p for p in pairs if len(sum_groups[p[0]+p[1]]) > 1]

    product_groups = defaultdict(list)
    for x, y in pairs:
        product_groups[x*y].append((x, y))
    pairs = [p for p in pairs if len(product_groups[p[0]*p[1]]) == 1]

    sum_groups = defaultdict(list)
    for x, y in pairs:
        sum_groups[x+y].append((x, y))
    pairs = [p for p in pairs if len(sum_groups[p[0]+p[1]]) == 1]

    return pairs

print(lucifer_solution())