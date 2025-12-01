import math

def birthday_probability(number):
    if number > 365:
        return 1.0
    probability = 1 - (math.factorial(365) / (math.factorial(365 - number) * (365 ** number)))
    return probability

n = int(input("Enter the number of people: "))
prob = birthday_probability(n) * 100
print(f"Probability that at least two people share a birthday is {prob:.2f}%.")

n_min = 1
while birthday_probability(n_min) <= 0.5:
    n_min += 1

print(f"For {n_min} or more people, the probability is greater than 50%.")