from estructures.HashTable import HashTable
from collections import deque

class RoadNetwork:

    def __init__(self, graph):
        self.graph = graph #Matriz de CSV
        self.centers = [] #EmergencyCenter's
        self.hashTable = HashTable()
    
    #==============
    # CENTROS:
    #==============
    def addCenter(self, center):
        self.validatePlaceInGraph(center.place)
        self.centers.append(center)

    #==============
    # INCIDENTS:
    #==============
    def addIncident(self, incident):
        self.validatePlaceInGraph(incident.place)
        self.hashTable.insert(incident.id, incident)

    def getIncident(self, id):
        return self.hashTable.search(id)
    
    def updateIncident(self, id, value):
        self.hashTable.update(id, value)
    
    def removeIncident(self, id):
        self.hashTable.remove(id)
    
    #==============
    # VALIDACIONES:
    #==============
    def validatePlaceInGraph(self, place):
        if (place < 0 or place >= len(self.graph)):
            raise ValueError("La locacion no se encuentra en el grafo")