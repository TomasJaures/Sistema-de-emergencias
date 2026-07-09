from structures.Heap import Heap

class PriorityQueue:

    # arr[nodeIdx] > arr[parentIdx]
    # Considerar esto al crear la clase que se inserte en PriorityQueue
    def __init__(self):
        self.heap = Heap() #Heap creado!


    def push(self, element):
        return self.heap.insert(element)

    def pop(self):
        return self.heap.extract()

    def peek(self):
        return self.heap._btree[0]

    def isEmpty(self):
        return (len(self.heap._btree) == 0)

    def getSize(self) -> int:
        return (len(self.heap._btree))

    def pushAll(self, arr: list):
        self.heap.buildHeap(arr)
    
    def top(self, k: int) -> list:
        return self.heap.topK(k)
    
    def updateElement(self, e):
        self.heap.updateElement(e)