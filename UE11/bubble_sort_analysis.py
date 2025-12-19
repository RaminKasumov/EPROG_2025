import random
import time
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

sizes = list(range(100, 2100, 200))
times = []

for n in sizes:
    data = [random.randint(0, n) for _ in range(n)]
    start = time.time()
    bubble_sort(data)
    end = time.time()
    times.append(end - start)

plt.plot(sizes, times, marker='o')
plt.xlabel("Input size n")
plt.ylabel("Time (seconds)")
plt.title("Bubble Sort Time Complexity")
plt.grid(True)
plt.show()