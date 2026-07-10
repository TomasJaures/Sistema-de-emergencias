import os
import csv
import random
from datetime import datetime, timedelta

class DatasetManager:
    def __init__(self, path: str):
        # Valida que la ruta de la carpeta exista inmediatamente al inicializar
        if not os.path.exists(path):
            raise FileNotFoundError(f"La ruta especificada no existe: {path}")
            
        self.path = path
        self.nodes = []
        self.zones = [chr(i) for i in range(65, 91)]  # Abecedario de la A a la Z por defecto
        self.canCoincide = False
        self.suffix = ""
        self.deltaDate = timedelta(days=10)  # Delta por defecto como objeto timedelta

    def setZones(self, zones: list[str]):
        if not zones:
            raise ValueError("La lista de zonas no puede estar vacia")
        self.zones = zones

    def setCanCoincide(self, canCoincide: bool):
        self.canCoincide = canCoincide

    def setSuffix(self, suffix: str):
        self.suffix = suffix

    def setDeltaDate(self, days: int):
        if days < 0:
            raise ValueError("Los dias de deltaDate no pueden ser negativos")
        self.deltaDate = timedelta(days=days)

    def createNodesCSV(self, cantNodes: int, cantEdges: int, isWeighted: bool = True):
        # Validaciones de consistencia para crear un grafo conexo
        if cantNodes < 2:
            raise ValueError("Se necesitan al menos 2 nodos para construir un grafo")
        if cantEdges < cantNodes - 1:
            raise ValueError(f"Para que el grafo sea conexo, cantEdges debe ser al menos {cantNodes - 1}")
        
        maxPossibleEdges = (cantNodes * (cantNodes - 1)) // 2
        if cantEdges > maxPossibleEdges:
            raise ValueError(f"La cantidad maxima de aristas posibles para {cantNodes} nodos es {maxPossibleEdges}")

        # 1. Generar los identificadores de nodos usando las zonas equitativamente
        self.nodes = []
        for i in range(cantNodes):
            zone = self.zones[i % len(self.zones)]
            nodeId = f"{zone}_{i + 1}"
            self.nodes.append(nodeId)

        # 2. Generar adyacencias inteligentes garantizando que el grafo sea conexo
        edgesSet = set()
        shuffledNodes = list(self.nodes)
        random.shuffle(shuffledNodes)
        
        # Algoritmo de arbol de expansion para asegurar conectividad inicial
        for i in range(1, len(shuffledNodes)):
            nodeA = shuffledNodes[i]
            nodeB = random.choice(shuffledNodes[:i])  # Se conecta a un nodo ya conectado
            # Guardamos con orden alfabetico para evitar duplicados en grafos no dirigidos
            edge = (nodeA, nodeB) if nodeA < nodeB else (nodeB, nodeA)
            edgesSet.add(edge)

        # Llenamos el resto de las aristas solicitadas de forma aleatoria
        while len(edgesSet) < cantEdges:
            nodeA = random.choice(self.nodes)
            nodeB = random.choice(self.nodes)
            if nodeA != nodeB:
                edge = (nodeA, nodeB) if nodeA < nodeB else (nodeB, nodeA)
                edgesSet.add(edge)

        # 3. Escritura del archivo CSV
        fileName = f"nodes{self.suffix}.csv"
        fullPath = os.path.join(self.path, fileName)
        
        with open(fullPath, mode='w', newline='', encoding='utf-8') as csvFile:
            writer = csv.writer(csvFile)
            if isWeighted:
                writer.writerow(["origen", "destino", "peso"])
                for nodeA, nodeB in edgesSet:
                    weight = random.randint(1, 10)  # Pesos aleatorios entre 1 y 10
                    writer.writerow([nodeA, nodeB, weight])
            else:
                writer.writerow(["origen", "destino"])
                for nodeA, nodeB in edgesSet:
                    writer.writerow([nodeA, nodeB])
                    
        print(f"Archivo de nodos creado de manera exitosa en: {fullPath}")

    def createIncidentsCSV(self, cantIncidents: int, incidentStates: list[str], incidentTypes: list[str]):
        if not self.nodes:
            raise ValueError("Primero debes ejecutar createNodesCSV() para inicializar los nodos")
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
                # Filtrado de ubicacion inteligente segun coincidencia permitida
                if not self.canCoincide and len(usedLocations) < len(self.nodes):
                    availableNodes = [n for n in self.nodes if n not in usedLocations]
                    location = random.choice(availableNodes)
                    usedLocations.add(location)
                else:
                    location = random.choice(self.nodes)

                # Extrae el prefijo de la zona directamente desde el ID del nodo
                zone = location.split('_')[0]
                severity = random.randint(1, 10)
                state = random.choice(incidentStates)
                incidentType = random.choice(incidentTypes)
                
                # Calculo de la fecha aleatoria hacia el pasado usando deltaDate
                randomSeconds = random.randint(0, int(self.deltaDate.total_seconds()))
                randomDate = now - timedelta(seconds=randomSeconds)
                dateStr = randomDate.strftime("%Y-%m-%d")

                writer.writerow([i, location, zone, severity, state, incidentType, dateStr])

        print(f"Archivo de incidentes creado de manera exitosa en: {fullPath}")

    def createCentersCSV(self, cantCenters: int):
        if not self.nodes:
            raise ValueError("Primero debes ejecutar createNodesCSV() para inicializar los nodos")
            
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

                zone = location.split('_')[0]
                name = f"Centro{zone}_{i}"

                writer.writerow([i, name, location, zone])

        print(f"Archivo de centros creado de manera exitosa en: {fullPath}")