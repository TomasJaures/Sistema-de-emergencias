from pathlib import Path

from models.RoadNetwork import RoadNetwork
from models.Incident import Incident
from models.EmergencyCenter import EmergencyCenter
from datetime import datetime
from utils.IncidentState import IncidentState
from EmergencySystem import EmergencySystem
from utils.CSV.FormatterCSV import FormatterCSV

def main():
    path = Path(__file__).parent.parent / "docs" / "graphs" / "graph1.csv"

    nodes, edges = FormatterCSV.loadCSV(path)

    rn = RoadNetwork(True)
    rn.addNodes(nodes)
    rn.addEdges(edges)

    system = EmergencySystem(rn)

    center1 = EmergencyCenter(0, "Centro A", "P")
    incident1 = Incident(1, "A", 10, datetime(2026, 7, 4), IncidentState.ACTIVE)
    system.insertCenter(center1)
    system.insertIncident(incident1)
    system.insertIncident(Incident(2, "E", 5, datetime(2026, 5, 1), IncidentState.ACTIVE))
    system.insertIncident(Incident(3, "I", 7, datetime(2026, 6, 2), IncidentState.ACTIVE))
    
    print(system.searchIncident(1).toString())
    system.updateIncidentState(1, IncidentState.CLOSED)
    print(system.searchIncident(1).toString())
    
    # removedIncident = system.removeIncident(1)
    # if removedIncident is not None:
    #     print("=== ELIMINADO ===")
    #     print(removedIncident.toString())
    #     system.insertIncident(Incident(1, "A", 10, datetime(2026, 7, 4), IncidentState.ACTIVE))
    # else:
    #     print("=== ERROR ===")
    
    print(f"Tabla hash de incidentes\n{system.getIncidentsHashTableStats()}")

    print(f"Incidente mas urgente:\n {system.getMostUrgentIncident().toString()}")

    print(f"K incidentes mas criticos")
    for i in system.getKIncidentsMostCritic(3):
        print(f"Prioridad: {i.priority}")

    print("Incidentes por tiempo: ")
    for i in system.getIncidentsByTime():
        print(f"Tiempo: {i.timestamp}")
    
    print("Incidentes por prioridad")
    for i in system.getIncidentsByPriority():
        print(f"Prioridad: {i.priority}")

    print("Desde algun centro al incidente: ")
    routeFound, visitedNodes, totalDistance = system.mostEfficientRouteFromCenterToIncident(center1, incident1)
    print(f"ruta encontrada: {routeFound}")
    print(f"Nodos visitados: {visitedNodes}")
    print(f"Distancia total: {totalDistance}")
    
    print(f"Ruta mas eficiente segun BFS: {system.mostEfficientRouteToIncidentByBFS(incident1)}")
    print(f"Ruta mas eficiente segun Djikstra: {system.mostEfficientRouteToIncidentByDjikstra(incident1)}")
    


    
    

if __name__ == "__main__":
    main()

