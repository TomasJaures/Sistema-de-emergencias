import csv

class FormatterCSV:
    @staticmethod
    def tryConvert(value):
        # Intenta convertir un string al tipo de dato mas especifico (int, float o dejarlo en string)
        value = value.strip()
        try:
            if '.' in value:
                return float(value)
            return int(value)
        except ValueError:
            return value

    @staticmethod
    def loadCSV(filePath: str):
        nodesSet = set()
        edgesList = []
        
        with open(filePath, mode='r', encoding='utf-8') as csvFile:
            reader = csv.reader(csvFile)
            
            # Primera linea para analizar el encabezado
            header = [column.strip().lower() for column in next(reader)]
            isWeighted = "peso" in header or "weight" in header

            for row in reader:
                if not row or len(row) < 2:
                    continue  # Saltar lineas vacias o incompletas
                
                # Convertir los datos de la fila a sus tipos correspondientes
                origin = FormatterCSV.tryConvert(row[0])
                destination = FormatterCSV.tryConvert(row[1])
                
                # Agregar nodos al conjunto para evitar duplicados
                nodesSet.add(origin)
                nodesSet.add(destination)
                
                # Procesar el peso segun el formato del grafo
                if isWeighted and len(row) >= 3:
                    weight = FormatterCSV.tryConvert(row[2])
                else:
                    weight = 1 # Valor por defecto si no es ponderado
                    
                edgesList.append((origin, destination, weight))
        
        # Ordenar lista para que quede bien
        nodesList = sorted(list(nodesSet))
        
        return nodesList, edgesList