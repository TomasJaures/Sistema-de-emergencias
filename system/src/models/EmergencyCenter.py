class EmergencyCenter:
    def __init__(self, id, name, zone, location):
        self.id = id
        self.name = name
        self.zone = zone
        self.location = location # Lugar en el nodo
    
    def __str__(self):
        return self.location

    def getData(self):
        return (
            f"id: {self.id}\n"
            f"name: {self.name}\n"
            f"Ubicacion: {self.location}"
        )