class HashTable:
    def __init__(self, capacity=101):
        self.capacity = capacity
        self._buckets = [[] for _ in range(capacity)]

        self._elementSize = 0
        self._collisions = 0
        self._usedBuckets = 0
        self.keys = set()

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

        if key in self.keys:
            return False #Si ya se encuentra la llave

        self.keys.add(key)
        bucket = self._buckets[self._hash(key)]

        if len(bucket) == 0:
            self._usedBuckets += 1
        else:
            # Cada vez que un elemento caiga en una lista no vacia, se suma una colision
            self._collisions += 1
        
        #Se inserta la clave y el valor (Tupla)
        bucket.append((key, value))
        self._elementSize += 1
        return True

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
                self.keys.remove(key)
                self._elementSize -= 1

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
    
    def getKeys(self) -> set:
        return self.keys

    def getStats(self):
        # TODO: Hacer reporte
        # loadFactor = self.loadFactor()
        # maxBucketSize = self.maxBuckEtelementSize()
        return (
            f"Factor de carga: {self.loadFactor()}\n"
            f"Colisiones: {self._collisions}\n"
            f"Buckets utilizados: {self._usedBuckets}\n"
            f"Máximo tamaño de bucket: {self.maxBuckEtelementSize()}"
        )
        

    