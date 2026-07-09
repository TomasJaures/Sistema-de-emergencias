from datetime import datetime
from utils.IncidentState import IncidentState

class Incident:

    def __init__(self, id, location, severity, timestamp: datetime, state: IncidentState):
        self.id = id # int
        self.location = location # Lugar en el nodo
        self.timestamp = timestamp
        self.state = state
        self.severity = severity
        
        self.priority = self.recalculatePriority()

        
        self.closestPath = None
        self.closestCenter = None

    @staticmethod
    def comparatorByPriority(a: Incident, b: Incident):
        return a.priority > b.priority

    @staticmethod
    def comparatorByTimestamp(a: Incident, b: Incident):
        return a.timestamp < b.timestamp # Tiempo al revez para que muestre por cercania
    
    comparator = comparatorByPriority

    def recalculatePriority(self):
        deltaTime = datetime.now() - self.timestamp
        timeInMinutes = deltaTime.total_seconds() / 60
        return self.severity * timeInMinutes

    def toString(self) -> str:
        return (
            f"Incident ID: {self.id}\n"
            f"Ubicacion: {self.location}\n"
            f"Estado: {self.state.name}\n"
            f"Priority: {self.priority}\n"
        )        

    def getData(self):
        return (
            f"Incident ID: {self.id}\n"
            f"Ubicacion: {self.location}\n"
            f"closestPath: {self.closestPath}\n"
            f"closestPath: {self.closestCenter}\n"
            f"Severity: {self.severity}\n"
            f"Priority: {self.priority}"
        )
    
    def __str__(self):
        return self.location
    
    def __gt__(self, other):
        return Incident.comparator(self, other)