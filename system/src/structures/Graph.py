from collections.abc import Callable
from collections import deque
from warnings import deprecated

@deprecated("Clase solo util con matriz de adyacencia")
class Graph:
    def __init__(self, matrix: list[list[int]]):
        self.matrix = matrix
    
    """
    Stop condition: La condicion para que se detenga BFS
    """
    def bfs(self, started_node: int, stop_condition):
        visited = [False] * len(self.matrix)
        q = deque([started_node])
        visited[started_node] = True

        while q:
            current = q.popleft()

            if stop_condition(current):
                return current

            for neighbor in self.matrix[current]:
                if neighbor != 0 and not visited[neighbor]:
                    visited[neighbor] = True
                    q.append(neighbor)

        return None
    

    def DFS(self, starterNode: int, endNode: int):

        

        print()

    def bfs(self, graph, NodeId):
        a = self.hashTable.search(NodeId) #Accident
        visited = [False] * len(graph)
        q = deque([a.place]) #Queue con solo nums
        
        while q:
            current = q.pop()

            if current in self.centers:
                return current
        
            arr = graph[current]
            for n in arr:
                if n != 0 and not visited[n]:
                    visited[n] = True
                    q.append(n)
                

                    # print(graph[current][i])
            current
        
        return None