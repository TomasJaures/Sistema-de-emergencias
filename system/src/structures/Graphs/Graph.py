from .Node import Node
from structures.HashTable import HashTable

class Graph:
    def __init__(self):
        self.nodes = set()
        self.nodesDisplay = [] # No se usara para la logica, solo para mostrar los datos

    def addNode(self, node: Node):
        if node not in self.nodes:
            self.nodesDisplay.append(node)
            self.nodes.add(node)

    def addNodes(self, nodes: list):
        for node in nodes:
            self.addNode(node)

    def addEdge(self, origin: Node, target: Node, weight, addressed=False):
        origin.addAdjacency(target, weight)

        # Si no es dirigido, agregamos la conexion inversa tambien
        if not addressed:
            target.addAdjacency(origin, weight)
    
    def show(self):
        for node in self.nodesDisplay:
            print(f"Nodo {node.data}: ", end="")
            for adjacency, weight in node.adjacencies:
                print(f"({adjacency.data}, {weight}) ", end="")
            print()
            
            