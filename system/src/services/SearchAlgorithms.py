from collections import deque
from structures.Graphs.Node import Node
from structures.HashTable import HashTable


class SearchAlgorithm:

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