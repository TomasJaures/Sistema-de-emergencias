class Node:
    def __init__(self, data):
        self.data = data
        self.adjacencies = []  # Lista de tuplas (Nodo, peso)

    def addAdjacency(self, node, weight):
        self.adjacencies.append((node, weight))

    def __str__(self):
        return str(self.data)
    
    def __eq__(self, other):
        return self.data == other.data

    def __hash__(self):
        return hash(self.data)

    def __str__(self):
        return str(self.data)
    
    def __repr__(self):
        return str(self.data)