import csv
class CSVReader:
    @staticmethod
    def getMatrizFromCsv(path=""):
        matriz = []

        try:
            with open(path, newline="", encoding="utf-8") as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    matriz.append([int(x) for x in row])
            return matriz
        except FileNotFoundError:
            print("El archivo no existe.")
            return None