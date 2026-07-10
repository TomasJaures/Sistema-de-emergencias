"""
MAX HEAP
"""
class Heap:
    def __init__(self):
        self._btree = []
    
    # Al ser un heap, la busqueda de un elemento toma un tiempo de O(n) :(
    def updateElement(self, element):
        for i in range(len(self._btree)):
            if self._btree[i] == element:
                self._btree[i] = element
                self._siftDown(i)
                nodeIdx = i
                while nodeIdx > 0:
                    parentIdx = (nodeIdx - 1) // 2
                    if not self._siftUp(nodeIdx, parentIdx):
                        break
                    nodeIdx = parentIdx
                return True
        return False

    def topK(self, k:int) -> list:
        result = []
        tmp = Heap()
        tmp.insert((self._btree[0], 0))
        for _ in range(min(k, len(self._btree))):
            value, idx = tmp.extract()
            result.append(value)

            left = 2 * idx + 1 # Nodo hijo
            right = 2 * idx + 2 # Nodo padre

            if left < len(self._btree):
                tmp.insert((self._btree[left], left))

            if right < len(self._btree):
                tmp.insert((self._btree[right], right))
        return result

    def insert(self, value):
        self._btree.append(value)
        nodeIdx = len(self._btree) - 1

        while nodeIdx > 0: # Con NodeIdx 0 o 1 da 0 o -1, por lo tanto parentIdx nunca se podria salir del arreglo.
            parentIdx = (nodeIdx - 1) // 2 # Indice del padre
            if not self._siftUp(nodeIdx, parentIdx):
                break
            nodeIdx = parentIdx # Si hubo switch, re asignar nuevos indices
        return True

    def _siftUp(self, nodeIdx, parentIdx):
        arr = self._btree
        if arr[nodeIdx] > arr[parentIdx]:
            arr[nodeIdx], arr[parentIdx] = arr[parentIdx], arr[nodeIdx] # Switch
            return True
        return False

    def extract(self):
        # No hay elementos
        if not self._btree:
            return None

        # Solo hay un elemento
        if len(self._btree) == 1:
            return self._btree.pop()

        # Cambio entre root y el elemento al final
        max = self._btree[0]
        self._btree[0] = self._btree.pop()

        self._siftDown(0)

        return max
    
    def _siftDown(self, parent):
        arr = self._btree
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
        self._btree = arr.copy()
        self.heapify()

    def heapify(self):
        n = len(self._btree)

        # Ultimo nodo no hoja
        lastParent = (n // 2) - 1 # Division entera

        for i in range(lastParent, -1, -1): # Recorrido inverso
            self._siftDown(i)