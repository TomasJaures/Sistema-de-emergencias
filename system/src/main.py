from structures.Graphs.Node import Node
from structures.Graphs.Graph import Graph
from services.SearchAlgorithms import SearchAlgorithms
from models.RoadNetwork import RoadNetwork
from models.Incident import Incident
from models.EmergencyCenter import EmergencyCenter

def main():
    # path = Path(__file__).parent.parent / "docs" / "graphs" / "graph1.csv"

    map = RoadNetwork(True)
    map.addNodes(["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P"])

    map.addEdges([
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

    map.addCenter(0, "Centro A", "P")
    map.addIncident(1, "A", 10)
    print(map.calculateIncidentSeverity(1))


    
    

if __name__ == "__main__":
    main()

