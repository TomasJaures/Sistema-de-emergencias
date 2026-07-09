from structures.Graphs.Node import Node
from structures.Graphs.Graph import Graph
from services.SearchAlgorithms import SearchAlgorithms
from models.RoadNetwork import RoadNetwork
from models.Incident import Incident
from models.EmergencyCenter import EmergencyCenter
from datetime import datetime
from utils.IncidentState import IncidentState
from EmergencySystem import EmergencySystem

def main():
    # path = Path(__file__).parent.parent / "docs" / "graphs" / "graph1.csv"

    rn = RoadNetwork(True)
    rn.addNodes(["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P"])

    rn.addEdges([
        ("A", "B", 4 ),
        ("B", "C", 2 ),
        ("B", "D", 3 ),
        ("C", "A", 4 ),
        ("G", "C", 6 ),
        ("C", "I", 5 ),
        ("I", "C", 7 ),
        ("L", "I", 4 ),
        ("I", "L", 5 ),
        ("H", "I", 4 ),
        ("D", "E", 4 ),
        ("E", "D", 5 ),
        ("E", "F", 1 ),
        ("E", "G", 7 ),
        ("E", "C", 8 ),
        ("G", "E", 6 ),
        ("G", "H", 1 ),
        ("F", "J", 5 ),
        ("G", "J", 3 ),
        ("J", "K", 2 ),
        ("K", "L", 7 ), 
        ("L", "N", 2 ),
        ("L", "M", 6 ),
        ("M", "N", 6 ),
        ("N", "O", 4 ),
        ("O", "P", 4 ),
        ("P", "N", 5 ),
        ("P", "K", 10)        
    ])


    
    rn.addCenter(EmergencyCenter(0, "Centro A", "P"))
    rn.addIncident(Incident(1, "A", 10, datetime(2026, 7, 4), IncidentState.ACTIVE))
    rn.addIncident(Incident(2, "E", 5, datetime(2026, 7, 4), IncidentState.ACTIVE))
    rn.addIncident(Incident(3, "I", 7, datetime(2026, 7, 4), IncidentState.ACTIVE))

    pq = rn.calculateAllIncidentSeverity()

    system = EmergencySystem(rn)


    # datetime(año, mes, día, hora, minuto, segundo)
    date = datetime(2026, 7, 9, 15, 30, 0)
    date = datetime(2026, 7, 3, 15, 30, 0)
    # Buscar la ruta óptima desde el centro de emergencia más cercano.    
    #- Incidentes más antiguos: Ordenados por tiempo.
    # - Incidentes más críticos: Ordenados por prioridad.
    # - Zonas con más incidentes: Ordenadas por frecuencia.


    
    

if __name__ == "__main__":
    main()

