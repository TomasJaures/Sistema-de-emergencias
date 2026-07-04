class HashTable:
    def __init__(self, capacity=101):
        self.capacity = capacity
        self.buckets = [[] for _ in range(capacity)]

        self.elementSize = 0
        self.collisions = 0
        self.usedBuckets = 0

    # Hashpolinomial
    def hash(self, key):
        key = str(key)
        h = 0
        base = 31

        for c in key:
            h = (h * base + ord(c)) % self.capacity

        return h

    def loadFactor(self):
        return self.elementSize / self.capacity

    def insert(self, key, value):
        bucket = self.buckets[self.hash(key)]

        if len(bucket) == 0:
            self.usedBuckets += 1
        else:
            # Cada vez que un elemento caiga en una lista no vacia, se suma una colision
            self.collisions += 1

        #Se inserta la clave y el valor (Tupla)
        bucket.append((key, value))
        self.elementSize += 1

    def search(self, key):
        bucket = self.buckets[self.hash(key)]

        for k, v in bucket:
            if k == key:
                return v

        return None

    def update(self, key, value):
        bucket = self.buckets[self.hash(key)]

        # idx, (clave, valor)
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return True

        return False

    def remove(self, key):
        bucket = self.buckets[self.hash(key)]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self.elementSize -= 1

                # Si el bucket estaba vacio, restar un userBuckets
                if len(bucket) == 0:    
                    self.usedBuckets -= 1

                return v
        return None

    def maxBuckEtelementSize(self):
        max = 0

        for bucket in self.buckets:
            if len(bucket) >= max:
                max = len(bucket)

        return max
    

class RoadNetwork:
    def __init__(self, graph):
        self.graph = graph #Matriz de CSV

    def run(self):

        

        print("Hello")