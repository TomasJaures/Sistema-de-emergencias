from structures.HashTable import HashTable
# from collections import deque
from structures.Graphs.Graph import Graph
from structures.Graphs.Node import Node


class RoadNetwork:

    def __init__(self, isAddressed=False):
        self.graph = Graph()
        self.isAddressed = isAddressed
        self.nodes = HashTable(1000)
    
    def addNode(self, id):
        newNode = Node(id)
        self.graph.addNode(newNode)
        self.nodes.insert(id, newNode)
    
    def addNodes(self, ids: list):
        for id in ids:
            self.addNode(id)

    def addEdge(self, originId, targetId, weight):
        origin = self.nodes.search(originId)
        target = self.nodes.search(targetId)
        if origin is None or target is None:
            raise ValueError("Nodo objetivo o destino, aun no se ha creado!")
        self.graph.addEdge(origin, target, weight, self.isAddressed)
    
    def addEdges(self, edges: list[tuple] ):
        for origin, target, weight in edges:
            self.addEdge(origin, target, weight)
