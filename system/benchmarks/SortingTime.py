import random
import time
import matplotlib.pyplot as plt
import os
import sys
sys.setrecursionlimit(200000) # Importante para que no salga error de limite de recursiones
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from services.Arrays import Arrays


def generate_arrays(size):
    return {
        "Aleatorio": [random.randint(0, 1000000) for _ in range(size)],
        "Ordenado": list(range(size)),
        "Inverso": list(range(size, 0, -1))
    }


def test_sorting():
    sizes = [100, 500, 1000, 2000, 5000]

    results = {
        "HeapSort": {
            "Aleatorio": [],
            "Ordenado": [],
            "Inverso": []
        },
        "QuickSort": {
            "Aleatorio": [],
            "Ordenado": [],
            "Inverso": []
        }
    }

    for size in sizes:
        arrays = generate_arrays(size)

        for case, array in arrays.items():

            # HEAP SORT
            copy_array = array.copy()

            start = time.perf_counter()
            Arrays.heapSort(copy_array)
            end = time.perf_counter()

            results["HeapSort"][case].append(end - start)


            # QUICK SORT
            copy_array = array.copy()

            start = time.perf_counter()
            Arrays.quickSort(copy_array)
            end = time.perf_counter()

            results["QuickSort"][case].append(end - start)

    return sizes, results


sizes, results = test_sorting()


# Mostrar resultados
for algorithm in results:
    print("\n", algorithm)

    for case in results[algorithm]:
        print(case)

        for size, time_value in zip(sizes, results[algorithm][case]):
            print(f"n={size}: {time_value:.6f}s")


# Graficos
plt.figure(figsize=(12, 8))

# Comparación general aleatoria
plt.subplot(2, 2, 1)

plt.plot(
    sizes,
    results["HeapSort"]["Aleatorio"],
    marker="o",
    label="HeapSort"
)

plt.plot(
    sizes,
    results["QuickSort"]["Aleatorio"],
    marker="o",
    label="QuickSort"
)

plt.title("Caso aleatorio")
plt.xlabel("Cantidad de elementos")
plt.ylabel("Tiempo (s)")
plt.legend()
plt.grid()


# Caso ordenado
plt.subplot(2, 2, 2)

plt.plot(
    sizes,
    results["HeapSort"]["Ordenado"],
    marker="o",
    label="HeapSort"
)

plt.plot(
    sizes,
    results["QuickSort"]["Ordenado"],
    marker="o",
    label="QuickSort"
)

plt.title("Caso ordenado")
plt.xlabel("Cantidad de elementos")
plt.ylabel("Tiempo (s)")
plt.legend()
plt.grid()


# Caso inverso
plt.subplot(2, 2, 3)

plt.plot(
    sizes,
    results["HeapSort"]["Inverso"],
    marker="o",
    label="HeapSort"
)

plt.plot(
    sizes,
    results["QuickSort"]["Inverso"],
    marker="o",
    label="QuickSort"
)

plt.title("Caso inverso")
plt.xlabel("Cantidad de elementos")
plt.ylabel("Tiempo (s)")
plt.legend()
plt.grid()


plt.tight_layout()
plt.show()