import sys
import os
import csv
import random
from datetime import datetime, timedelta
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from services.Arrays import Arrays


class DatasetManager:
    """Clase auxiliara para crear los Dataset's del sistema de emergencias.

    Puede crear los archivos ``.csv`` de los nodos, centros y incidentes en base a la configuracion que desee el desarrollador.
    """

    def __init__(self, path: str):
        if not os.path.exists(path):
            raise FileNotFoundError(f"La ruta especificada no existe: {path}")
            
        self.path = path
        self.nodes = []
        self.edges = [] 
        self.zones = [chr(i) for i in range(65, 91)] #Por defecto: [A, B, C, ..., Z]
        self.canCoincide = False # Define si incidente y centro pueden coincidir en ubicacion
        self.suffix = "" # Define los sufijo de los archivos CSV
        self.deltaDate = timedelta(days=10) # Define que tan al pasado puede estar un incidente

    def setZones(self, zones: list[str]):
        """Define en que zonas/sectores de la red vial, pueden estar contenidos los nodos.

        `zones`: Lista de zonas en los que caeran.
        """
        if not zones:
            raise ValueError("La lista de zonas no puede estar vacia")
        self.zones = zones

    def setCanCoincide(self, canCoincide: bool):
        """Define si un incidente y un centro de emergencia pueden compartir la misma ubicacion en el grafo

        `canCoincide`: Si estos pueden coincidir ubicacion
        """
        self.canCoincide = canCoincide

    def setSuffix(self, suffix: str):
        """Define el sufijo que tendra cada archivo CSV

        `suffix`: Sufijo designado.
        """
        self.suffix = suffix

    def setDeltaDate(self, days: int):
        """Define la cantidad de tiempo que puede haber pasado tras un incidente
        
        `days int`: Cantidad de dias.
        """
        if days < 0:
            raise ValueError("Los dias de deltaDate no pueden ser negativos")
        self.deltaDate = timedelta(days=days)

    
    def generateNetworkData(self, cantNodes: int, cantEdges: int, isWeighted: bool = True):
        """Genera y define la estructura de los nodos y aristas de la clase

        `cantNodes`: Cantidad de nodos.
        `cantEdges`: Cantidad de aristas.
        `isWeighted`: Si el grafo es Ponderado.
        """
        # Esta funcion calcula y genera toda la estructura del grafo en memoria
        if cantNodes < 2:
            raise ValueError("Se necesitan al menos 2 nodos para construir un grafo")
        if cantEdges < cantNodes - 1:
            raise ValueError(f"Para que el grafo sea conexo, cantEdges debe ser al menos {cantNodes - 1}")
        
        maxPossibleEdges = (cantNodes * (cantNodes - 1)) // 2
        if cantEdges > maxPossibleEdges:
            raise ValueError(f"La cantidad maxima de aristas posibles para {cantNodes} nodos es {maxPossibleEdges}")

        # Generacion de ID's de nodos
        self.nodes = []
        for z in range(min(len(self.zones), cantNodes)):
            for i in range(cantNodes // len(self.zones)):
                self.nodes.append( f"{self.zones[z].lower()}{i}")

        # Algoritmo para garantizar que el grafo sea conexo
        edgesSet = set()
        shuffledNodes = list(self.nodes)
        random.shuffle(shuffledNodes)
        
        for i in range(1, len(shuffledNodes)):
            nodeA = shuffledNodes[i]
            nodeB = random.choice(shuffledNodes[:i])
            edge = (nodeA, nodeB) if nodeA < nodeB else (nodeB, nodeA)
            edgesSet.add(edge)

        # Agregar aristas restantes de forma aleatoria
        while len(edgesSet) < cantEdges:
            nodeA = random.choice(self.nodes)
            nodeB = random.choice(self.nodes)
            if nodeA != nodeB:
                edge = (nodeA, nodeB) if nodeA < nodeB else (nodeB, nodeA)
                edgesSet.add(edge)

        # Estructuramos las aristas con su peso correspondiente
        self.edges = []
        for nodeA, nodeB in edgesSet:
            weight = random.randint(1, 10) if isWeighted else 1
            self.edges.append((nodeA, nodeB, weight))
        Arrays.quickSort(self.edges)
        #TODO: ASD
    
    def setNodesId(self, hasUnderscore: bool, isCamelCase: bool):
        self.hasUnderscore = hasUnderscore
        self.isCamelCase = isCamelCase

    def createNodesCSV(self, isWeighted: bool = True):
        """Crea el archivo ``.csv`` los nodos.

        ``isWeighted``: Define el archivo `.csv` se creara en un formato que almacene los pesos
        """
        if not self.nodes or not self.edges:
            raise ValueError("Primero debes ejecutar generateNetworkData() para crear los datos en memoria")

        fileName = f"nodes{self.suffix}.csv"
        fullPath = os.path.join(self.path, fileName)
        
        with open(fullPath, mode='w', newline='', encoding='utf-8') as csvFile:
            writer = csv.writer(csvFile)
            if isWeighted:
                # En español para ser compatible con "FormatterCSV.py
                writer.writerow(["origen", "destino", "peso"])
                for nodeA, nodeB, weight in self.edges:
                    writer.writerow([nodeA, nodeB, weight])
            else:
                writer.writerow(["origen", "destino"])
                for nodeA, nodeB, _ in self.edges:
                    writer.writerow([nodeA, nodeB])
                    
        print(f"Archivo de nodos creado de manera exitosa en: {fullPath}")

    def createIncidentsCSV(self, cantIncidents: int, incidentStates: list[str], incidentTypes: list[str]):
        """Genera y define el archivo `.csv` de los incidentes
        
        `cantIncidents`: Define la cantidad de incidentes
        `incidentStates`: Define en que estados se puede encontrar un incidente
        `incidentTypes`: Define en que tipo puede caer un incidente
        """

        if not self.nodes:
            raise ValueError("Primero debes ejecutar generateNetworkData() para inicializar los nodos")
        if not incidentStates or not incidentTypes:
            raise ValueError("Las listas de estados y tipos no pueden estar vacias")

        fileName = f"incidents{self.suffix}.csv"
        fullPath = os.path.join(self.path, fileName)

        with open(fullPath, mode='w', newline='', encoding='utf-8') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(["id", "location", "zone", "severity", "state", "type", "date"])
            
            usedLocations = set()
            now = datetime.now()

            for i in range(1, cantIncidents + 1):
                if not self.canCoincide and len(usedLocations) < len(self.nodes):
                    availableNodes = [n for n in self.nodes if n not in usedLocations]
                    location = random.choice(availableNodes)
                    usedLocations.add(location)
                else:
                    location = random.choice(self.nodes)

                zone = location.upper()[0]
                severity = random.randint(1, 10)
                state = random.choice(incidentStates)
                incidentType = random.choice(incidentTypes)
                
                randomSeconds = random.randint(0, int(self.deltaDate.total_seconds()))
                randomDate = now - timedelta(seconds=randomSeconds)
                dateStr = randomDate.strftime("%Y-%m-%d %H:%M:%S")

                writer.writerow([i, location, zone, severity, state, incidentType, dateStr])

        print(f"Archivo de incidentes creado de manera exitosa en: {fullPath}")

    def createCentersCSV(self, cantCenters: int):
        """Genera y define el archivo `.csv` de los centros de emergencia
        
        `cantCenters`: Define la cantidad de centros
        """
        if not self.nodes:
            raise ValueError("Primero debes ejecutar generateNetworkData() para inicializar los nodos")
            
        fileName = f"centers{self.suffix}.csv"
        fullPath = os.path.join(self.path, fileName)

        with open(fullPath, mode='w', newline='', encoding='utf-8') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(["id", "name", "location", "zone"])
            
            usedLocations = set()
            for i in range(1, cantCenters + 1):
                if not self.canCoincide and len(usedLocations) < len(self.nodes):
                    availableNodes = [n for n in self.nodes if n not in usedLocations]
                    location = random.choice(availableNodes)
                    usedLocations.add(location)
                else:
                    location = random.choice(self.nodes)

                zone = location[0].upper()
                name = f"Centro_{zone}{i}"

                writer.writerow([i, name, location, zone])

        print(f"Archivo de centros creado de manera exitosa en: {fullPath}")