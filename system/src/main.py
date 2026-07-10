from pathlib import Path

BASE_DIR = Path(__file__).parent

from models.RoadNetwork import RoadNetwork
from models.Incident import Incident
from models.EmergencyCenter import EmergencyCenter
from datetime import datetime
from utils.IncidentState import IncidentState
from EmergencySystem import EmergencySystem
from utils.CSV.FormatterCSV import FormatterCSV

def main():
    print(f"BASEDIR: {BASE_DIR}")
    datasetPath = BASE_DIR / "data" / "dataset_1"
    nodes, edges = FormatterCSV.loadNodesCSV(datasetPath / "nodes.csv")
    centers = FormatterCSV.loadCenters(datasetPath / "centers.csv")
    incidents = FormatterCSV.loadIncidents(datasetPath / "incidents.csv")

    rn = RoadNetwork(False)
    rn.addNodes(nodes)
    rn.addEdges(edges)

    system = EmergencySystem(rn)

    for center in centers:
        system.insertCenter(center)
    
    for incident in incidents:
        system.insertIncident(incident)
    
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
        print(f"Tiempo: {i.date}")
    
    print("Incidentes por prioridad")
    for i in system.getIncidentsByPriority():
        print(f"Prioridad: {i.priority}")

    print("Desde algun centro al incidente: ")
    routeFound, visitedNodes, totalDistance = system.mostEfficientRouteFromCenterToIncident(centers[2], incidents[8])
    print(f"ruta encontrada: {routeFound}")
    print(f"Nodos visitados: {visitedNodes}")
    print(f"Distancia total: {totalDistance}")
    
    print()

    print(f"Ruta mas eficiente segun BFS: {system.mostEfficientRouteToIncidentByBFS(incidents[8])}")
    print(f"Ruta mas eficiente segun Djikstra: {system.mostEfficientRouteToIncidentByDjikstra(incidents[8])}")
        


    
    

if __name__ == "__main__":
    main()

