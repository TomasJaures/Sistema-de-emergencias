class Node:
    def __init__(self, data):
        self.data = data
        self.currentWeight = float("inf") # Para djikstra
        self.adjacencies = []  # Lista de tuplas (Nodo, peso)

    def addAdjacency(self, node, weight):
        self.adjacencies.append((node, weight))

    # Operaciones necesarias para el cumplimiento en varias estructuras de datos
    
    def __str__(self):
        return str(self.data)
    
    def __hash__(self):
        return hash(self.data)
    
    def __repr__(self):
        return str(self.data)
    
    def __eq__(self, other):
        return self.data == other.data
    
    def __gt__(self, other):
        return self.currentWeight < other.currentWeight