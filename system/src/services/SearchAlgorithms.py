from collections import deque
from structures.Graphs.Node import Node
from structures.HashTable import HashTable
from structures.Heap import Heap

class SearchAlgorithms:

    @staticmethod
    def bfs(startNode: Node, condition):
        q = deque([startNode])
        visited = set([startNode])
        visitedDisplay = [startNode]
        # Guarda: nodo -> padre
        record = HashTable(capacity=1000) # En el DataSet del ejercicio, podian haber 500 aristas

        while q:
            current = q.popleft()
            
            if condition(current): # Condición de termino defindido por el usuario
                path = [] # Para reconstruir el camino
                node = current
                while node is not None:
                    path.append(node)
                    node = record.search(node)
                path.reverse()
                return current, path, visitedDisplay

            for adjacency, weight in current.adjacencies:
                if adjacency not in visited:
                    visited.add(adjacency)
                    visitedDisplay.append(adjacency)
                    record.insert(adjacency, current)
                    q.append(adjacency)

        return None

    @staticmethod
    def dijkstra(startNode: Node, condition):
        heap = Heap() # Max heap
        previous = HashTable(capacity=1000)
        distances = HashTable(capacity=1000)
        visited = set()
        visitedDisplay = []

        startNode.currentWeight = 0

        distances.insert(startNode, 0)
        previous.insert(startNode, None)

        heap.insert(startNode)

        while heap.btree:
            current = heap.extract()
            if current in visited:
                continue

            visited.add(current)
            visitedDisplay.append(current)

            if condition(current):
                path = []
                node = current
                while node is not None:
                    path.append(node)
                    node = previous.search(node)
                path.reverse()
                return current, path, visitedDisplay, current.currentWeight

            for adjacency, weight in current.adjacencies:
                newWeight = current.currentWeight + weight
                oldWeight = distances.search(adjacency)

                if oldWeight is None or newWeight < oldWeight:
                    adjacency.currentWeight = newWeight
                    distances.insert(adjacency,newWeight)
                    previous.insert(adjacency,current)
                    heap.insert(adjacency)


        return None