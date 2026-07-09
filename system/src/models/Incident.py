from datetime import datetime
from utils.IncidentState import IncidentState

class Incident:
    def __init__(self, id, location, severity, timestamp: datetime, state: IncidentState):
        self.id = id # int
        self.location = location # Lugar en el nodo
        self.priority = -1 # severity * timeFactor
        self.timestamp = timestamp
        self.state = state

        self.severity = severity
        self.closestPath = None
        self.closestCenter = None

    def setPriority(self, priority):
        self.priority = priority

    def calculatePriority(self, timeFactor):
        self.priority = self.severity * timeFactor

    def __str__(self):
        return self.location

    def getData(self):
        return (
            f"Incident ID: {self.id}\n"
            f"Ubicacion: {self.location}\n"
            f"closestPath: {self.closestPath}\n"
            f"closestPath: {self.closestCenter}\n"
            f"Severity: {self.severity}\n"
            f"Priority: {self.priority}"
        )
    
    
    def __gt__(self, other):
        return self.priority > other.priority