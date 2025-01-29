import random
import time
import matplotlib.pyplot as plt # imported matplotlib library using pip command 

# Sorting algorithms
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Function to benchmark sorting algorithms
def benchmark_sort(arr_func, size):
    arr = [random.randint(0, 1000) for _ in range(size)]
    start_time = time.perf_counter()
    arr_func(arr)
    end_time = time.perf_counter()
    return end_time - start_time

# Different array sizes
sizes = [5, 10, 20, 50, 100, 200, 500, 1000, 2000]
times_insertion = []
times_selection = []
times_bubble = []

# Benchmark each sorting algorithm
for size in sizes:
    times_insertion.append(benchmark_sort(insertion_sort, size))
    times_selection.append(benchmark_sort(selection_sort, size))
    times_bubble.append(benchmark_sort(bubble_sort, size))

# Print results
print("Insertion Sort Times:", times_insertion)
print("Selection Sort Times:", times_selection)
print("Bubble Sort Times:", times_bubble)

# Plot results
plt.figure(figsize=(10, 5))
plt.plot(sizes, times_insertion, marker='o', label='Insertion Sort')
plt.plot(sizes, times_selection, marker='o', label='Selection Sort')
plt.plot(sizes, times_bubble, marker='o', label='Bubble Sort')
plt.xlabel('Array Size')
plt.ylabel('Time (seconds)')
plt.title('Sorting Algorithm Performance')
plt.legend()
plt.grid(True)
plt.show()

