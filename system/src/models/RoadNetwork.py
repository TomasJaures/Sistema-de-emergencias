from estructures.HashTable import HashTable


class RoadNetwork:
    def __init__(self, graph):
        self.graph = graph #Matriz de CSV

    def run(self):
        hashTable = HashTable()

        hashTable.insert(1, "Tomas")
        hashTable.insert(2, "Felipe")
        hashTable.insert(3, "Renato")

        
        print(hashTable.search(2))