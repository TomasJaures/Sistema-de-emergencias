from pathlib import Path
from utils.CSVReader import CSVReader

class Incident:
    def __init__(self, id):
        self.id = id # int
        self.place # Lugar en el nodo
        self.priority
        self.type
        self.date
        self.state

class EmergencyCenter:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.place # Lugar en el nodo

class RoadNetwork:
    def __init__(self):
        pass

def main():
    path = Path(__file__).parent.parent / "docs" / "graphs" / "graph1.csv"
    matriz = CSVReader.getMatrizFromCsv(path)
    print(matriz)
    
if __name__ == "__main__":
    main()
