from pathlib import Path
from utils.CSVReader import CSVReader
from models.RoadNetwork import RoadNetwork

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

class EmergencyCenter:
    def __init__(self, id, name, place):
        self.id = id
        self.name = name
        self.place = place # Lugar en el nodo

def main():
    path = Path(__file__).parent.parent / "docs" / "graphs" / "graph1.csv"
    graph = CSVReader.getMatrizFromCsv(path)
    # print(matriz)

    center = EmergencyCenter(1, "Cruz roja", 12)
    incident = Incident(1, 3)
    network = RoadNetwork(graph)

    network.run()


    # 12: Centro
    # 3: Incidente
    
if __name__ == "__main__":
    main()
