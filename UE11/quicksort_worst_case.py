import matplotlib.pyplot as plt
import time

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    pivot = arr[mid]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

sizes = list(range(200, 2200, 200))
times = []

for n in sizes:
    arr = list(range(n))
    start = time.time()
    quicksort(arr)
    end = time.time()
    times.append(end - start)

plt.plot(sizes, times, marker='o')
plt.xlabel("Input size n")
plt.ylabel("Time (seconds)")
plt.title("QuickSort (middle pivot) — avoids worst case on sorted input")
plt.grid(True)
plt.show()