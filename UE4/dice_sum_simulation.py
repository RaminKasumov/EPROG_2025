import random

def dice_sum(n):
    return sum(random.randint(1, 6) for _ in range(n))

results = [dice_sum(2) for _ in range(1000)]
frequencies = [results.count(i) for i in range(2, 13)]
most_common_sum = frequencies.index(max(frequencies)) + 2

print("Frequencies:", frequencies)
print("Most frequent sum:", most_common_sum)