from structures.HashTable import HashTable
# from collections import deque
from structures.PriorityQueue import PriorityQueue
from structures.Graphs.Graph import Graph
from structures.Graphs.Node import Node
from .EmergencyCenter import EmergencyCenter
from .Incident import Incident
# from services.Arrays import Arrays
from services.SearchAlgorithms import SearchAlgorithms


class RoadNetwork:

    def __init__(self, isAddressed=False):
        self.graph = Graph()
        self.isAddressed = isAddressed

        self.nodes = HashTable(1000)
        self.incidents = HashTable(1000)
        self.worstIncidents = PriorityQueue()
        self.centers = HashTable(1000)
    
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
    
    def addCenter(self, id, name: str, place):
        center = EmergencyCenter(id, name, place)
        self.centers.insert(id, center)
        node = self.nodes.search(place)
        node.data = center
    
    def addIncident(self, id, place, severity):
        incident = Incident(id, place, severity)
        self.incidents.insert(id, incident)
        node = self.nodes.search(place)
        node.data = incident

    def calculateIncidentSeverity(self, id) -> Incident:
        incident = self.incidents.search(id)
        node = self.nodes.search(incident.place)

        _, _, _, weight = SearchAlgorithms.dijkstra(node, lambda current: isinstance(current.data, EmergencyCenter))
        incident.calculatePriority(weight)
        self.worstIncidents.push(incident)
        return incident
        
    def calculateAllIncidentSeverity(self) -> PriorityQueue:
        keys = self.incidents.getKeys()
        incidents = []
        for key in keys:
            incidents.append(self.calculateIncidentSeverity(key))
        self.worstIncidents.pushAll(incidents) # Heapify
        return self.worstIncidents
        