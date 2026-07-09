from structures.Heap import Heap

class Arrays:

    @staticmethod
    def heapSort(arr: list) -> list:
        result = []
        heap = Heap()
        heap.buildHeap(arr)
        while heap._btree:
            result.append(heap.extract())
        return result[::-1] # De menor a mayor
    
    @staticmethod
    def quickSort(array: list, low=0, high=None) -> list:
        if high is None:
            high = len(array) - 1 # Pivote al final al inicio (Casos completamente desordenados)

        if low < high:
            pivot_index = Arrays._partition(array, low, high)
            Arrays.quickSort(array, low, pivot_index-1)
            Arrays.quickSort(array, pivot_index+1, high)
        return array

    @staticmethod
    def _partition(array, low, high):
        pivot = array[high]
        i = low - 1

        for j in range(low, high):
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i] # Cambio entre i+1 y el numero mas bajo de "j"

        array[i+1], array[high] = array[high], array[i+1] # Cambio del pivote
        return i+1

