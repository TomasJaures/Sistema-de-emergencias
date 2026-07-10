import csv
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
from models.Incident import Incident
from models.EmergencyCenter import EmergencyCenter
from models.RoadNetwork import RoadNetwork
from utils.IncidentState import IncidentState
from utils.IncidentTypes import IncidentTypes
from datetime import datetime

class FormatterCSV:
    @staticmethod
    def tryConvert(value):
        # Intenta convertir un string al tipo de dato mas especifico
        value = value.strip()
        try:
            if '.' in value:
                return float(value)
            return int(value)
        except ValueError:
            return value
        
    @staticmethod
    def loadNodesCSV(filePath):
        """Permite cargar y obtener los nodos y aristas.

        `path`: Direccion del archivo `.csv`.

        **return:** Retorna tanto los nodos, como las aristas
        """
        nodesSet = set()
        edgesList = []
        
        with open(filePath, mode='r', encoding='utf-8') as csvFile:
            reader = csv.reader(csvFile)
            header = [column.strip().lower() for column in next(reader)]
            isWeighted = "peso" in header

            for row in reader:
                if not row or len(row) < 2:
                    continue
                
                origin = FormatterCSV.tryConvert(row[0])
                destination = FormatterCSV.tryConvert(row[1])
                
                nodesSet.add(origin)
                nodesSet.add(destination)
                
                if isWeighted and len(row) >= 3:
                    weight = FormatterCSV.tryConvert(row[2])
                else:
                    weight = 1
                    
                edgesList.append((origin, destination, weight))
        
        nodesList = sorted(list(nodesSet))
        return nodesList, edgesList
    
    @staticmethod
    def loadCenters(path) -> list[EmergencyCenter]:
        """Permite cargar y obtener los centros de ayuda,

        `path`: Direccion del archivo `.csv`.

        **return:** La lista de los centros de ayuda cargados
        """
        centers = []
        
        with open(path, mode='r', encoding='utf-8') as csvFile:
            reader = csv.reader(csvFile)
            next(reader) # Saltar encabezado
            
            for row in reader:
                if not row:
                    continue

                id = int(row[0].strip())
                name = row[1].strip()
                zone = row[3].strip()
                location = row[2].strip()
                
                centers.append(EmergencyCenter(id, name, zone, location))
                
        return centers

    @staticmethod
    def loadIncidents(path) -> list[Incident]:
        """Permite cargar y obtener los incidentes,

        `path`: Direccion del archivo `.csv`.

        **return:** La lista de los incidentes cargados
        """
        incidents = []
        
        with open(path, mode='r', encoding='utf-8') as csvFile:
            reader = csv.reader(csvFile)
            next(reader) # Saltar encabezado
            
            for row in reader:
                if not row:
                    continue

                id = int(row[0].strip())
                zone = row[2].strip()
                location = row[1].strip()
                incidentState = IncidentState[row[4].strip().upper()].name
                incidentType = IncidentTypes[row[5].strip().upper()].name
                severity = int(row[3].strip())
                date = datetime.strptime(row[6].strip(), "%Y-%m-%d %H:%M:%S")
                
                incidents.append(
                    Incident(id, zone, location, incidentType, incidentState, severity, date)
                )
                
        return incidents