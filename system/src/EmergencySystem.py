from utils.IncidentState import IncidentState
from models.Incident import Incident
from models.EmergencyCenter import EmergencyCenter
from models.RoadNetwork import RoadNetwork
from structures.HashTable import HashTable
from structures.PriorityQueue import PriorityQueue
from services.Arrays import Arrays
from services.SearchAlgorithms import SearchAlgorithms

class EmergencySystem:
    def __init__(self, roadNetwork: RoadNetwork):
        self.roadNetwork = roadNetwork
        self.incidents = HashTable(1000)
        self.incidentsByPriority = PriorityQueue()
        self.centers = HashTable()

    def insertCenter(self, center: EmergencyCenter):
        wasPut = self.centers.insert(center.id, center)
        node = self.roadNetwork.nodes.search(center.location)
        node.data = center
        self.roadNetwork.nodes.update(center.location, node)

        if not wasPut:
            raise ValueError("El centro ya se encuentra registrado")

    # Insercion en hashTable y PriorityQueue
    def insertIncident(self, incident: Incident):
        node = self.roadNetwork.nodes.search(incident.location)
        node.data = incident
        self.roadNetwork.nodes.update(incident.location, node)
        wasPutInHash = self.incidents.insert(incident.id, incident)
        wasPutInPQ = self.incidentsByPriority.push(incident)
        if not wasPutInHash or not wasPutInPQ:
            raise ValueError("El incidente ya se encuentra registrado")

    # HASHING
    def searchIncident(self, id) -> Incident | None:
        incident = self.incidents.search(id)
        return incident

    def updateIncidentState(self, id, incidentState: IncidentState):
        incident = self.incidents.search(id)
        if incident is None:
            raise ValueError("El incidente no se encuentra en la tabla hash")
        else:
            incident.state = incidentState
            self.incidents.update(id, incident)
    
    def removeIncident(self, id) -> Incident | None:
        # TODO: Falta eliminar en la PQ
        return self.incidents.remove(id)
    
    def getIncidentsHashTableStats(self) -> str:
        return (
            f"=== Estadisticas de la Tabla HASH de INCIDENTES ===\n"
            f"{self.incidents.getStats()}\n"
            f"=================================================="
        )
    
    # HEAP y PRIORITY QUEUE
    def getMostUrgentIncident(self) -> Incident:
        return self.incidentsByPriority.peek()

    def getKIncidentsMostCritic(self, k: int) -> list[Incident]:
        return self.incidentsByPriority.top(k)

    def updateIncidentPriority(self, id, newPriority):
        # MEJORAR TIEMPOD DE EJECUCION
        incident = self.searchIncident(id)
        incident.priority = newPriority
        self.incidentsByPriority.updateElement(incident)

    # SORTS

    def getIncidentsByTime(self) -> list[Incident]:
        incidents = self.incidentsByPriority.heap._btree.copy() #Sacar arreglo desde el heap
        Incident.comparator = Incident.comparatorByDatetime
        # No usaremos QUICKSORT, debido a que los datos van a estar algo ordenados debido a que el tiempo es un factor clave para la severidad, por ende, los datos van a estar algo ordenados
        incidentsByTime = Arrays.heapSort(incidents) 
        Incident.comparator = Incident.comparatorByPriority
        return incidentsByTime
    
    def getIncidentsByPriority(self) -> list[Incident]:
        k = self.incidentsByPriority.getSize()
        return self.incidentsByPriority.top(k).copy()

    def getIncidentsByZone(self):
        # TODO: Implementar algoritmo quicksort
        pass
    
    # ======================
    # ALGORITMOS DE BUSQUEDA
    # ======================

    # DJIKSTRA
    def mostEfficientRouteFromCenterToIncident(self, center: EmergencyCenter, incident: Incident) -> tuple:
        startNode = self.roadNetwork.nodes.search(center.location)
        endNode = self.roadNetwork.nodes.search(incident.location)
        
        # - Nodos visitados
        # - Ruta encontrada
        # - Distancia total
        # - Costo acumulado
        result = SearchAlgorithms.dijkstra(startNode, lambda current: current == endNode)
        if result is not None:
            _, routeFound, visitedNodes, totalDistance = result
            return routeFound, visitedNodes, totalDistance
        else:
            return [], [], float("inf")

    # BFS
    def mostEfficientRouteToIncidentByBFS(self, incident: Incident) -> list:
        startNode = self.roadNetwork.nodes.search(incident.location)
        result = SearchAlgorithms.bfs(startNode, lambda current: isinstance(current.data, EmergencyCenter))

        if result is not None:
            _, routeFound, _ = result
            routeFound.reverse()
            return routeFound
        else:
            return []
    
    # DJIKSTRA
    def mostEfficientRouteToIncidentByDjikstra(self, incident: Incident) -> list:
        startNode = self.roadNetwork.nodes.search(incident.location)
        
        result = SearchAlgorithms.dijkstra(startNode, lambda current: isinstance(current.data, EmergencyCenter))

        if result is not None:
            _, routeFound, _, _ = result
            routeFound.reverse()
            return routeFound
        else:
            return []