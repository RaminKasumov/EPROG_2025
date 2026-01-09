import numpy as np
import time
import matplotlib.pyplot as plt

sizes = [50, 100, 200, 400, 800]
times = []

for n in sizes:
    A = np.random.rand(n, n)
    B = np.random.rand(n, n)

    start = time.time()
    A @ B
    end = time.time()

    times.append(end - start)

plt.loglog(sizes, times, marker="o")
plt.xlabel("Matrix size n")
plt.ylabel("Time (seconds)")
plt.title("Runtime of matrix-matrix multiplication")
plt.grid(True)
plt.show()