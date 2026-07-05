from estructures.Heap import Heap

class PriorityQueue:
    def __init__(self):
        self.heap = Heap() #Heap creado!

    def push(self, element):
        self.heap.insert(element)

    def pop(self):
        return self.heap.extract()

    def peek(self):
        return self.heap.btree[0]

    def isEmpty(self):
        return (len(self.heap.btree) == 0)

    def size(self):
        return (len(self.heap.btree))

    def top(self, k):
        self.heap.topK(k)