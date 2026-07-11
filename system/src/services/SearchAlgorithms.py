from collections import deque
from numbers import Number
from typing import Callable
from structures.Graphs.Node import Node
from structures.HashTable import HashTable
from structures.PriorityQueue import PriorityQueue

class SearchAlgorithms:

    @staticmethod
    def bfs(startNode: Node, condition: Callable[[Node], bool]):
        q = deque([startNode])
        visited = HashTable()
        visited.insert(startNode, startNode)
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

            for adjacency, _ in current.adjacencies:
                if adjacency not in visited.getKeys():
                    visited.insert(adjacency, adjacency)
                    visitedDisplay.append(adjacency)
                    record.insert(adjacency, current)
                    q.append(adjacency)
        return None

    

    @staticmethod
    def dijkstra(startNode: Node, condition: Callable[[Node], bool]) -> tuple[Node, list, list, Number]:
        start = startNode
        start.currentWeight = 0
        
        parents = HashTable()
        visited = HashTable()
        visited.insert(start, start)

        obj = None

        pq = PriorityQueue()
        pq.push((0, start))
        
        while pq.getSize() > 0:
            _, node = pq.pop()

            if condition(node):
                obj = node

            for adj, w in node.adjacencies:
                if visited.search(adj) is None and node.currentWeight + w < adj.currentWeight:
                    adj.currentWeight = node.currentWeight + w

                    parents.insert(adj, node)
                    parents.update(adj, node) #Necesario
                    pq.push((adj.currentWeight * -1, adj))

            visited.insert(node, node)
        
        parent = obj
        path = []

        while True:
            parent = parents.search(parent)
            if parent is None:
                break
            path.append(parent)

        restart = visited.getKeys()
        totalDistance = obj.currentWeight
        for v in restart:
            v.currentWeight = float("inf")

        return obj, path, restart, totalDistance