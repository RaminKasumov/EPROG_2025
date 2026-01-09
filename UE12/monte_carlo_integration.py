import numpy as np
import matplotlib.pyplot as plt

def monte_carlo_integral(f, a, b, n):
    x = np.random.uniform(a, b, n)
    return (b - a) * np.mean(f(x))

f = lambda x: x**2
exact_value = 1.0 / 3.0

ns = np.logspace(2, 5, 10, dtype=int)

repetitions = 20
errors = []

for n in ns:
    estimates = []
    for _ in range(repetitions):
        estimate = monte_carlo_integral(f, 0.0, 1.0, n)
        estimates.append(estimate)

    mean_error = np.mean(np.abs(np.array(estimates) - exact_value))
    errors.append(mean_error)

plt.loglog(ns, errors, marker="o")
plt.xlabel("Number of samples n")
plt.ylabel("Mean absolute error")
plt.title("Monte Carlo integration error")
plt.grid(True)
plt.show()