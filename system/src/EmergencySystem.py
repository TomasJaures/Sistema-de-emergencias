from utils.IncidentState import IncidentState
from models.Incident import Incident
from models.EmergencyCenter import EmergencyCenter
from models.RoadNetwork import RoadNetwork
from structures.HashTable import HashTable

class EmergencySystem:
    def __init__(self, roadNetwork: EmergencyCenter):
        self.roadNetwork = roadNetwork
        self.incidents = HashTable(1000)

    # HASHING
    def insertIncident(self, incident: Incident):
        self.incidents.insert(incident.id, incident)
    
    def searchIncident(self, id):
        return self.incidents.search(id)
        
    
    def updateIncidentState(self, id):
        self.incidents.search(id)