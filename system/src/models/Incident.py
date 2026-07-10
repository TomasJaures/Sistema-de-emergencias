from datetime import datetime
from utils.IncidentState import IncidentState
from utils.IncidentTypes import IncidentTypes

class Incident:
    """Representa un incidente
    """

    def __init__(self, id, zone, location, incidentType: IncidentTypes, incidentState: IncidentState, severity: int, date: datetime):
        self.id = id
        self.zone = zone
        self.location = location
        self.incidentType = incidentType
        self.incidentState = incidentState
        self.severity = severity
        self.date = date

        self.priority = self.recalculatePriority()

        self.closestPath = None
        self.closestCenter = None

    @staticmethod
    def comparatorByPriority(a: Incident, b: Incident):
        """Comparacion segun la prioridad del incidente
        """
        return a.priority > b.priority

    @staticmethod
    def comparatorByDatetime(a: Incident, b: Incident):
        """Comparacion segun la novedad en que ocurrio el incidente
        """
        return a.date < b.date # Tiempo al revez para que muestre por cercania
    
    comparator = comparatorByPriority

    def recalculatePriority(self):
        """Hace un nuevo calculo para la prioridad del incidente segun el tiempo actual
        """
        deltaTime = datetime.now() - self.date
        timeInMinutes = deltaTime.total_seconds() / (3600 * 24)
        return round(self.severity * timeInMinutes, 1)

    def toString(self) -> str:
        return (
            f"Incident ID: {self.id}\n"
            f"Ubicacion: {self.location}\n"
            f"Estado: {self.incidentState}\n"
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