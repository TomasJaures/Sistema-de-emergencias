class Incident:
    def __init__(self, id, place):
        self.id = id # int
        self.place = place # Lugar en el nodo
        self.priority = -1 # severity * timeFactor
        # self.type
        # self.date
        # self.state

    def setPriority(self, priority):
        self.priority = priority