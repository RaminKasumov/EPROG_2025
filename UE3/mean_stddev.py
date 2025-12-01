import math

def mean_and_stddev(x1, x2, x3):
    numbers = [x1, x2, x3]
    mean = sum(numbers) / len(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / (len(numbers) - 1)
    stddev = math.sqrt(variance)
    return mean, stddev

print(mean_and_stddev(7, 2, 5))