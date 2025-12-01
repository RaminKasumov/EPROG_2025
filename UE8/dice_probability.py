from collections import defaultdict

def probability(n, k):
    dp = defaultdict(int)
    dp[0] = 1

    for i in range(1, n+1):
        faces = i + 1
        new_dp = defaultdict(int)
        for s, count in dp.items():
            for face in range(1, faces+1):
                new_dp[s + face] += count
        dp = new_dp

    total_outcomes = 1
    for i in range(1, n+1):
        total_outcomes *= (i+1)

    return dp[k] / total_outcomes if k in dp else 0

print(probability(3, 7))