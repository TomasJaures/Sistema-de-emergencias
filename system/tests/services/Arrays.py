import unittest
import sys
import os
## Para importar de otras carpetas
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
from services.Arrays import Arrays

class TestHeapSort(unittest.TestCase):

    ## HEAP SORT

    def test_heap_sort_comun(self):
        arr = [5, 1, 4, 2, 8]
        result = Arrays.heapSort(arr)
        self.assertEqual(result, [1, 2, 4, 5, 8])

    def test_heap_sort_vacio(self):
        self.assertEqual(Arrays.heapSort([]), [])

    def test_heap_sort_ordenado(self):
        self.assertEqual(Arrays.heapSort([1, 2, 3]), [1, 2, 3])

    def test_heap_sort_negativos(self):
        arr = [-1, -5, -3, -8, -9, 0, 5]
        result = Arrays.heapSort(arr)
        self.assertEqual(result, [-9, -8, -5, -3, -1, 0, 5])

    ## QUICKSORT

    def test_quick_sort_comun(self):
        arr = [5, 1, 4, 2, 8]
        result = Arrays.quickSort(arr)
        self.assertEqual(result, [1, 2, 4, 5, 8])

    def test_quick_sort_vacio(self):
        self.assertEqual(Arrays.quickSort([]), [])

    def test_quick_sort_ordenado(self):
        self.assertEqual(Arrays.quickSort([1, 2, 3]), [1, 2, 3])

    def test_quick_sort_negativos(self):
        arr = [-1, -5, -3, -8, -9, 0, 5]
        result = Arrays.quickSort(arr)
        self.assertEqual(result, [-9, -8, -5, -3, -1, 0, 5])
    

# Esto permite correr los tests desde la terminal
if __name__ == '__main__':
    unittest.main()