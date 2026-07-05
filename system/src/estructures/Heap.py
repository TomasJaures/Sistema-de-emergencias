import math

#Max heap
class Heap:
    def __init__(self):
        self.btree = []

    def topK(self, k):
        result = []
        for _ in range(min(k, len(self.btree))):
            result.append(self.extract())
        return result

    def insert(self, value):
        self.btree.append(value)
        nodeIdx = len(self.btree) - 1

        while nodeIdx > 0: # Con NodeIdx 0 o 1 da 0 o -1, por lo tanto parentIdx nunca se podria salir del arreglo.
            parentIdx = (nodeIdx - 1) // 2 # Indice del padre
            if not self.siftUp(nodeIdx, parentIdx):
                break
            nodeIdx = parentIdx # Si hubo switch, re asignar nuevos indices

    def siftUp(self, nodeIdx, parentIdx):
        arr = self.btree
        if arr[nodeIdx] > arr[parentIdx]:
            arr[nodeIdx], arr[parentIdx] = arr[parentIdx], arr[nodeIdx] # Switch
            return True
        return False

    def extract(self):
        # No hay elementos
        if not self.btree:
            return None

        # Solo hay un elemento
        if len(self.btree) == 1:
            return self.btree.pop()

        # Cambio entre root y el elemento al final
        max = self.btree[0]
        self.btree[0] = self.btree.pop()

        self.siftDown(0)

        return max
    
    def siftDown(self, parent):
        arr = self.btree
        n = len(arr)

        while True:
            left = 2 * parent + 1
            right = 2 * parent + 2
            largest = parent

            # No se sale del arreglo y si es mayor que parent
            if left < n and arr[left] > arr[largest]:
                largest = left # Switch
            # No se sale del arreglo y si es mayor que parent
            if right < n and arr[right] > arr[largest]:
                largest = right 
            # Si parent es el mas grande
            if largest == parent:
                break

            arr[parent], arr[largest] = arr[largest], arr[parent] # Switch
            parent = largest

    def buildHeap(self, arr):
        self.btree = arr.copy()
        self.heapify()

    def heapify(self):
        n = len(self.btree)

        # Ultimo nodo no hoja
        lastParent = (n // 2) - 1 # Division entera

        for i in range(lastParent, -1, -1): # Recorrido inverso
            self.siftDown(i)