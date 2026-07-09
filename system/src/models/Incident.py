class Incident:
    def __init__(self, id, place, severity):
        self.id = id # int
        self.place = place # Lugar en el nodo
        self.priority = -1 # severity * timeFactor
        self.severity = severity
        # self.type
        # self.date
        # self.state

    def setPriority(self, priority):
        self.priority = priority

    def calculatePriority(self, timeFactor):
        self.priority = self.severity * timeFactor

    def __str__(self):
        return (
            f"Incident ID: {self.id}\n"
            f"Place: {self.place}\n"
            f"Severity: {self.severity}\n"
            f"Priority: {self.priority}"
        )