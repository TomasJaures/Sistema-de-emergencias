class HashTable:
    def __init__(self, capacity=101):
        self.capacity = capacity
        self._buckets = [[] for _ in range(capacity)]

        self._elementSize = 0
        self._collisions = 0
        self._usedBuckets = 0

    # _hashpolinomial
    def _hash(self, key):
        key = str(key)
        h = 0
        base = 31

        for c in key:
            h = (h * base + ord(c)) % self.capacity

        return h

    def loadFactor(self):
        return self._elementSize / self.capacity

    def insert(self, key, value):
        bucket = self._buckets[self._hash(key)]

        if len(bucket) == 0:
            self._usedBuckets += 1
        else:
            # Cada vez que un elemento caiga en una lista no vacia, se suma una colision
            self.collisions += 1

        #Se inserta la clave y el valor (Tupla)
        bucket.append((key, value))
        self._elementSize += 1

    def search(self, key):
        bucket = self._buckets[self._hash(key)]

        for k, v in bucket:
            if k == key:
                return v

        return None

    def update(self, key, value):
        bucket = self._buckets[self._hash(key)]

        # idx, (clave, valor)
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return True

        return False

    def remove(self, key):
        bucket = self._buckets[self._hash(key)]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self.elementSize -= 1

                # Si el bucket estaba vacio, restar un userBuckets
                if len(bucket) == 0:    
                    self._usedBuckets -= 1

                return v
        return None

    def maxBuckEtelementSize(self):
        max = 0

        for bucket in self._buckets:
            if len(bucket) >= max:
                max = len(bucket)

        return max
    
    def generateReport():
        # TODO: Hacer reporte
        print("[!] Falta hacer esta parte del codigo...")    
