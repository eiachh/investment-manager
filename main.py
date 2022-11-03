from glob import glob
import json
import math
from common_lib.const import constants
from flask import Flask,request

class investmentManager():
    def __init__(self):
        self.request_data = ''


    def getPreferredInvestmentJson(self):
        nextInvestment = self.getManagerOptions()
        nextInvestment = {'investmentManager': nextInvestment}
        return nextInvestment


    def getManagerOptions(self):
        researchManagerOption = self.request_data['researchManager']    
        buildingManagerOption = self.request_data['buildingManager']
        progressionManagerOption = self.request_data['progressionManager']
        finalOption = self.getBestInvestment(researchManagerOption , buildingManagerOption , progressionManagerOption)
        return finalOption
    
        
    #TODO check if constructable suggestion fits in next to the research within the resource hardcap
    def getBestInvestment(self, research, building, progression):
        # Apes together strong
        if self.isProgressive(progression):
            if(self.isConstructionOngoing()):
                progression['constructable']['buildingID'] = -1
                progression['constructable']['buildingLevel'] = -1
            if(self.isResearchOngoing()):
                progression['researchable']['researchID'] = -1
                progression['researchable']['researchLevel'] = -1
            return progression
        elif self.isResearchable(research):
            return {**research, "constructible" : {"buildingID" : -1,"buildingLevel" : -1}}
        elif self.isConstructable(building):
            return {**building, 'researchable' : {'researchID' : -1, 'researchLevel' : -1}}
        else: 
            return {'constructable' : {'buildingID': -1, 'buildingLevel': -1},
                'researchable' : {'researchID' : -1, 'researchLevel' : -1}}

    def isResearchable(self, research):
        return (research['researchable']['researchID'] != -1 and self.isResearchOngoing())

    def isResearchOngoing(self):
        return self.request_data['ongoingConstructionsAndResearch']['ResearchID'] == 0
            
    def isConstructable(self, building):
        return (building['constructable']['buildingID'] != -1 and self.isConstructionOngoing())

    def isConstructionOngoing(self):
        return self.request_data['ongoingConstructionsAndResearch']['BuildingID'] == 0

    def isProgressive(self, progression):                     
        progBuilding = progression['constructable']
        progResearch = progression['researchable']
        return (progBuilding['buildingID'] != -1 or progResearch['researchID'] != -1)
            

    
        
        

        



    #def isReasonable(self, ogameID, ogameLvl):
        

            

investManager = investmentManager()

port = 5004
app = Flask(__name__)

@app.route('/get_investment', methods=['GET'])
def getInvestmentEndpoint(): 
    investManager.request_data = request.get_json()
    respData = investManager.getPreferredInvestmentJson()
    return respData


@app.route('/ready', methods=['GET'])
def getInvestmentReadiness():
    return "{Status: OK}"


app.run(host='0.0.0.0', port = port)
