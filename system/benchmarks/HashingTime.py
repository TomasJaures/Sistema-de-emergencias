import time
import random
import string
import matplotlib.pyplot as plt
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from structures.HashTable import HashTable


def random_key(size=10):
    return ''.join(random.choice(string.ascii_letters) for _ in range(size))


def test_hashing():
    capacity = 1009  # Tamaño primo para reducir colisiones
    sizes = [100, 500, 1000, 2000, 5000, 8000]

    loadFactors = []
    collisions = []
    insertTimes = []
    searchTimes = []

    for n in sizes:
        table = HashTable(capacity)

        keys = [random_key() for _ in range(n)]
        start = time.perf_counter()

        for i, key in enumerate(keys):
            table.insert(key, i)

        end = time.perf_counter()

        insertTimes.append(end - start)
        loadFactors.append(table.loadFactor())
        collisions.append(table._collisions)

        start = time.perf_counter()

        for key in keys:
            table.search(key)

        end = time.perf_counter()
        searchTimes.append(end - start)


    return (
        sizes,
        loadFactors,
        collisions,
        insertTimes,
        searchTimes
    )


sizes, load, collisions, insert_time, search_time = test_hashing()


# Mostrar resultados
print("Resultados Hash Table\n")

for i in range(len(sizes)):
    print(f"Elementos: {sizes[i]}")
    print(f"Factor de carga: {load[i]:.3f}")
    print(f"Colisiones: {collisions[i]}")
    print(f"Tiempo inserción: {insert_time[i]:.6f}s")
    print(f"Tiempo búsqueda: {search_time[i]:.6f}s")
    print("------------------------")


plt.figure(figsize=(12, 8))

# Factor de carga
plt.subplot(2, 2, 1)
plt.plot(sizes, load, marker="o")
plt.xlabel("Cantidad de elementos")
plt.ylabel("Factor de carga")
plt.title("Factor de carga")
plt.grid()


# Colisiones
plt.subplot(2, 2, 2)
plt.plot(sizes, collisions, marker="o")
plt.xlabel("Cantidad de elementos")
plt.ylabel("Colisiones")
plt.title("Colisiones")
plt.grid()


# insercion
plt.subplot(2, 2, 3)
plt.plot(sizes, insert_time, marker="o")
plt.xlabel("Cantidad de elementos")
plt.ylabel("Tiempo (segundos)")
plt.title("Tiempo de inserción")
plt.grid()


# Busqueda
plt.subplot(2, 2, 4)
plt.plot(sizes, search_time, marker="o")
plt.xlabel("Cantidad de elementos")
plt.ylabel("Tiempo (segundos)")
plt.title("Tiempo de búsqueda")
plt.grid()

plt.tight_layout()
plt.show()