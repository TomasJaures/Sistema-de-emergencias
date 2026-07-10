from CSV.DatasetManager import  DatasetManager
from IncidentState import IncidentState
from IncidentTypes import IncidentTypes

def main():
    builder = DatasetManager("system/src/data/dataset_1")
    builder.setNodesId(False, False)
    builder.generateNetworkData(80, 200)
    builder.createNodesCSV()
    states = [state.name for state in IncidentState]
    types = [type.name for type in IncidentTypes]
    
    builder.createIncidentsCSV(30, states, types)
    builder.createCentersCSV(5)





if __name__ == "__main__":
    main()

