import time
import random
import matplotlib.pyplot as plt
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from structures.Heap import Heap

def test_insert():
    sizes = [1000, 5000, 10000, 50000, 100000]
    times = []

    for n in sizes:
        heap = Heap()
        values = [random.randint(1, 1000000) for _ in range(n)]

        start = time.perf_counter()
        for value in values:
            heap.insert(value)
        end = time.perf_counter()
        times.append(end - start)
    return sizes, times

def test_extract():
    sizes = [1000, 5000, 10000, 50000, 100000]
    times = []

    for n in sizes:
        values = [random.randint(1, 1000000) for _ in range(n)]

    for n in sizes:
        heap = Heap()
        values = [random.randint(1, 1000000) for _ in range(n)]

        for value in values:
            heap.insert(value)

        start = time.perf_counter()

        for _ in range(n):
            heap.extract()

        end = time.perf_counter()
        times.append(end - start)
    return sizes, times

insertSizes, insertTimes = test_insert()
extract_sizes, extract_times = test_extract()

print("Inserción")
for size, t in zip(insertSizes, insertTimes):
    print(f"n={size}: {t:.6f} segundos")

for size, t in zip(extract_sizes, extract_times):
    print(f"n={size}: {t:.6f} segundos")

plt.figure(figsize=(8,5))

plt.plot(insertSizes, insertTimes, marker="o", label="Insert")
plt.plot(extract_sizes, extract_times, marker="o", label="Extract")

plt.xlabel("Cantidad de elementos (n)")
plt.ylabel("Tiempo (segundos)")
plt.title("Complejidad temporal Heap")
plt.legend()
plt.grid()

plt.show()